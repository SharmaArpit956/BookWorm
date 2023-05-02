import json
import requests


API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"


def request(question, context):
    answer = "Can you please rephrase the quesion?"
    payload = {
        "inputs": {
            "question": question,
            "context": context,
        }
    }
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    data = json.loads(response.content.decode("utf-8"))
    try:
        print(data)
        answer = data["answer"]
        confidence = round(data["score"]*100)
    except:
        answer ="Can't find the answer in the given context. Kindly rephrase your question"
        confidence = 0
        
    # print(confidence)
    return answer, confidence


if __name__ == "__main__":
    cxt = '''Personal Track Safety
    Topic 1
    Keeping you safe
    Module 5
    Accessing and Navigating the
    Railway (On or Near the Line)
    Following a safety briefing and before they begin the walk on or near the line to the work site, the team
    must make sure they are wearing the correct PPE.
    As a minimum, everyone working on or near the line must wear all orange high visibility clothing, a safety
    helmet and safety footwear. Depending on the task, the team may also need to wear other items of
    PPE such as gloves or safety glasses.
    Personal Track Safety'''

    answer, confidence = request(
        "what is the colour of the clothing to be worn?", cxt)
    print(answer)
    print(" ")
    print(confidence)
