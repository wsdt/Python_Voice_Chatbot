#!/usr/bin/python3
from modules.get_welcome_msg import get_welcome_msg
from modules.get_random_fact.get_random_fact import get_random_fact
from modules.get_random_question.get_random_question import get_random_question
from starterkit.get_smart_answer import get_smart_answer

# Speech to Text and reverse

from pocketsphinx import LiveSpeech
import pyttsx3

# TODO REMOVE AND REPLACE WITH DB (no import)
ENABLED_MODULES = [
    get_welcome_msg,
    get_random_question,
    get_random_fact
]

# OUTPUT / Assistant Voice/Response +++++++++++++++
assistantVoice = pyttsx3.init()

# TODO: Make this dynamic, by saving it to the database and letting the user decide when he wants
def configureAssistantVoice():
    # Set voice
    assistantVoice.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")

    # Set speech rate (slow down so it's clearer [might be too slow/fast for other voices])
    assistantVoice.setProperty('rate',assistantVoice.getProperty('rate')-50)


def getAssistantResponse(phrase):
    for module in ENABLED_MODULES:
        # text should be always a str, bc. we validated this in main.py
        if any(x in str(phrase) for x in module.chat_keywords):
            answer = str(module.getAnswer(phrase))
            break

    # Outside of for, so if nothing is returned we get a smart answer, but only if nothing answered until now
    answer = str(get_smart_answer.getAnswer(phrase))

    print("Assistant response: \""+answer+"\"")
    assistantVoice.say(answer)
    assistantVoice.runAndWait()


# INPUT / Users Voice/Response +++++++++++++++
def liveSpeech():
    for phrase in LiveSpeech():
        print("Users message: '" + str(phrase)+"'")
        # answer as text message
        """t = threading.Thread(target=getAssistantResponse, args=(phrase))
        t.start()
        t.join()"""
        getAssistantResponse(phrase)

        #_thread.start_new_thread(getAssistantResponse, (phrase,))

# CONFIGURATION ++++++++++++++++++++++++++++++
try:
    configureAssistantVoice()
except:
    print("VoiceMgr: Could not configure assistants speech. Using default settings.")