#!/usr/bin/python3


# Speech to Text and reverse
# Testing file

from pocketsphinx import LiveSpeech,AudioFile,get_model_path
import urllib
import os
from PyChatbot import PyChatbot
import threading
import pyttsx3

assistantVoice = pyttsx3.init()
LAST_VOICE_FILE = "user_voice_msg.ogg"

def liveSpeech():
    for phrase in LiveSpeech():
        print("Users message: '" + str(phrase)+"'")
        # answer as text message
        """t = threading.Thread(target=getAssistantResponse, args=(phrase))
        t.start()
        t.join()"""
        getAssistantResponse(phrase)

        #_thread.start_new_thread(getAssistantResponse, (phrase,))



def getAssistantResponse(phrase):
    answer = str(PyChatbot.getAnswer(phrase))
    print("Assistant response: \""+answer+"\"")
    #http://pyttsx3.readthedocs.io/en/latest/engine.html
    assistantVoice.say(answer)
    assistantVoice.runAndWait()

def downloadVoiceFile(update):
    filedata = urllib.request.urlopen(str(update.message.voice.get_file().file_path)).read()

    with open('files/'+LAST_VOICE_FILE, 'wb') as f:
        f.write(filedata)

def test(update):
    downloadVoiceFile(update)


    model_path = get_model_path()
    config = {
        'audio_file': os.path.join("files",LAST_VOICE_FILE),
        'verbose': False,
        'buffer_size': 2048,
        'no_search': False,
        'full_utt': False,
        'hmm': os.path.join(model_path, 'en-us'),
        'lm': os.path.join(model_path, 'en-us.lm.bin'),
        'dict': os.path.join(model_path, 'cmudict-en-us.dict')
    }

    for phrase in AudioFile(**config):
        print(phrase)



if __name__ == '__main__':
    liveSpeech()
