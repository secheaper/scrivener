"""
Copyright (C) 2021 SE Transcriptor - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com
"""

from gtts import gTTS

class toAudio():
    def __init(self):
        self.summary = ''

    # The text that you want to convert to audio
    def convert_to_audio(self, mytext):
        try:

            # Language in which you want to convert
            language = 'en' 
            # Passing the text and language to the engine
            myobj = gTTS(text=mytext, lang=language, slow=False)

            # Saving the converted audio in a mp3 file
            myobj.save("converted.mp3")
        except:
            return None
        