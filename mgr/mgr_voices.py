#!/usr/bin/python3
from starterkit.fallback_module.get_smart_answer import get_smart_answer
from mgr.mgr_db import db_loadEnabledModules

# Speech to Text and reverse
import speech_recognition as sr
r = sr.Recognizer()
import pyttsx3

ENABLED_MODULES = db_loadEnabledModules() # do only once for better performance
FALLBACK_MODULE = get_smart_answer() # shouldn't be changed, unless you know what you are doing

# OUTPUT / Assistant Voice/Response +++++++++++++++
assistantVoice = pyttsx3.init()

# TODO: Make this dynamic, by saving it to the database and letting the user decide when he wants
def configureAssistantVoice():
    # Set voice
    assistantVoice.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")

    # Set speech rate (slow down so it's clearer [might be too slow/fast for other voices])
    assistantVoice.setProperty('rate',assistantVoice.getProperty('rate')-50)

def getAssistantResponse(phrase):
    have_answered = False
    answer = "Unknown error"
    for module in ENABLED_MODULES:
        # text should be always a str, bc. we validated this in main.py
        if any(x in str(phrase) for x in module.getChatKeywords()):
            answer = str(module.getAnswer(phrase))
            have_answered = True

    # Outside of for, so if nothing is returned we get a smart answer, but only if nothing answered until now
    if not have_answered: answer = str(FALLBACK_MODULE.getAnswer(phrase))

    print("Assistant response: \""+answer+"\"")
    assistantVoice.say(answer)
    assistantVoice.runAndWait()


# INPUT / Users Voice/Response +++++++++++++++
def live_speech():
    print("Starting speech recognition.")

    # https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
    with sr.Microphone() as source:
        while True:
            try:
                audio = r.listen(source,phrase_time_limit=10) # listen to source
                # use testing api key
                text = r.recognize_google(audio, language="en-US")
                print("Users message: '{}'".format(text))
                getAssistantResponse(text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand you.")
            except sr.RequestError:
                print("API call failed. Key valid? Internet connection?")

# CONFIGURATION ++++++++++++++++++++++++++++++
try:
    configureAssistantVoice()
except:
    print("VoiceMgr: Could not configure assistants speech. Using default settings.")