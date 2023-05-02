import speech_recognition as sr
import pyaudio
import play_audio
import time



def get_question():
    # create a recognizer object
    r = sr.Recognizer()

    # Set up the audio capture settings
    audio = pyaudio.PyAudio()

    # Find the desired microphone device
    device_index = None
    for i in range(audio.get_device_count()):
        dev = audio.get_device_info_by_index(i)
        # print(str(i)+": "+str(dev['name']))
        if 'Headset Microphone (Plantronics' in dev['name']:
            device_index = i
            # print(dev['name'])
            break
    
    while(1):
        # use the microphone as source
        with sr.Microphone(device_index) as source:
            time.sleep(5)
            play_audio.play_audio("mic_start.wav")
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
            continue

if __name__ == "__main__":
    question = get_question()
    print(question)
