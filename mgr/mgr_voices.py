#!/usr/bin/python3
from starterkit.get_smart_answer import get_smart_answer
from mgr.mgr_db import db_loadEnabledModules

# Speech to Text and reverse

from pocketsphinx import LiveSpeech
import pyttsx3

ENABLED_MODULES = db_loadEnabledModules() # do only once for better performance

# OUTPUT / Assistant Voice/Response +++++++++++++++
assistantVoice = pyttsx3.init()

# TODO: Make this dynamic, by saving it to the database and letting the user decide when he wants
def configureAssistantVoice():
    # Set voice
    assistantVoice.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")

    # Set speech rate (slow down so it's clearer [might be too slow/fast for other voices])
    assistantVoice.setProperty('rate',assistantVoice.getProperty('rate')-50)


def getAssistantResponse(phrase):
    haveAnswered = False
    answer = "Unknown error"
    for module in ENABLED_MODULES:
        # text should be always a str, bc. we validated this in main.py
        if any(x in str(phrase) for x in module.getChatKeywords()):
            answer = str(module.getAnswer(phrase))
            haveAnswered = True

    # Outside of for, so if nothing is returned we get a smart answer, but only if nothing answered until now
    if not haveAnswered: answer = str(get_smart_answer.getAnswer(phrase))

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