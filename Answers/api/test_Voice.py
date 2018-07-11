


# Speech to Text and reverse
# Testing file

from pocketsphinx import AudioFile
import urllib
import os

class test_Voice:

    @staticmethod
    def test(update):
        filedata = urllib.request.urlopen(
            str(update.message.voice.get_file().file_path)
        )

        datatowrite = filedata.read()

        with open('files/test.ogg', 'wb') as f:
            f.write(datatowrite)

        config = {
            'audio_file': os.path.join("files","test.ogg")
        }

        for phrase in AudioFile(**config):
            print(phrase)



