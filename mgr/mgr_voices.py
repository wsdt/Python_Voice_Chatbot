#!/usr/bin/python3


# Speech to Text and reverse

from pocketsphinx import LiveSpeech
from mgr.mgr_modules import PyChatbot
import pyttsx3

# OUTPUT / Assistant Voice/Response +++++++++++++++
assistantVoice = pyttsx3.init()

# TODO: Make this dynamic, by saving it to the database and letting the user decide when he wants
def configureAssistantVoice():
    # Set voice
    assistantVoice.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")

    # Set speech rate (slow down so it's clearer [might be too slow/fast for other voices])
    assistantVoice.setProperty('rate',assistantVoice.getProperty('rate')-50)


def getAssistantResponse(phrase):
    answer = str(PyChatbot.getAnswer(phrase))
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