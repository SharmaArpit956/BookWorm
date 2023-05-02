import pyttsx3
import os



def say(text):
    #Initialize the Text-to-speech engine using the init() function: 
    engine = pyttsx3.init()

    #Convert your text to speech using the say() function: 
    engine.say(text+"")

    #Run the engine to output the speech: 
    engine.runAndWait()


if __name__ == "__main__":
    say("Hello, how are you?")