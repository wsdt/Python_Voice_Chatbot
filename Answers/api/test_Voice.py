


# Speech to Text and reverse
# Testing file

from pocketsphinx import AudioFile
import urllib
import os

class test_Voice:
    LAST_VOICE_FILE = "user_voice_msg.ogg"

    @staticmethod
    def downloadVoiceFile(update):
        filedata = urllib.request.urlopen(str(update.message.voice.get_file().file_path)).read()

        with open('files/'+test_Voice.LAST_VOICE_FILE, 'wb') as f:
            f.write(filedata)

    @staticmethod
    def test(update):
        test_Voice.downloadVoiceFile(update)

        config = {
            'audio_file': os.path.join("files",test_Voice.LAST_VOICE_FILE)
        }

        for phrase in AudioFile(**config):
            print(phrase)



