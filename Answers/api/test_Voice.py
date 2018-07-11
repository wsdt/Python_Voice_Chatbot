


# Speech to Text and reverse
# Testing file

from pocketsphinx import LiveSpeech,AudioFile,get_model_path
import urllib
import os

class test_Voice:
    LAST_VOICE_FILE = "user_voice_msg.ogg"

    @staticmethod
    def liveSpeech():
        for phrase in LiveSpeech():
            print(phrase)

    @staticmethod
    def downloadVoiceFile(update):
        filedata = urllib.request.urlopen(str(update.message.voice.get_file().file_path)).read()

        with open('files/'+test_Voice.LAST_VOICE_FILE, 'wb') as f:
            f.write(filedata)

    @staticmethod
    def test(update):
        test_Voice.downloadVoiceFile(update)


        model_path = get_model_path()
        config = {
            'audio_file': os.path.join("files",test_Voice.LAST_VOICE_FILE),
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
    test_Voice.liveSpeech()
