import http_requests
import web_scraper
import speech_to_text
import text_to_speech
import pi_gui
# import pi_momentory_button
import pen_drive_files_list
import display_list
import context_selector
import settings

# while true:
#     # continually check for a Press of a button
#     pi_momentory_button.button(2)
# context selector



context, wifi_name, wifi_password = settings.read_settings()
context=context.strip()
if context == "null" or context == '':
    print("context==null")
    context = context_selector.context_selection()
    settings.write_settings(context, wifi_name, wifi_password)

while(1):
    #TODO uncomment it afterwards
    # question = speech_to_text.get_question()
    question = "If you can’t remember the exact dates for your log, what to do?"

    # using model hosting inference from hugging face
    answer, confidence = http_requests.request(
        question=question, context=context)
    
    #TODO DELTE THIS 
    confidence=50
    
    if(confidence > 30):
        break

print(answer)
reply = answer + " with " + str(confidence)+"% connfidence"
# TODO prints text on the screen of raspberry pie
pi_gui.print_on_pi(reply)
text_to_speech.say(reply)
