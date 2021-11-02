from gtts import gTTS

class toAudio():
    def __init(self):
        self.summary = ''

    # The text that you want to convert to audio
    def convert_to_audio(self, mytext):

    # Language in which you want to convert
        language = 'en' 
        # Passing the text and language to the engine
        myobj = gTTS(text=mytext, lang=language, slow=False)

        # Saving the converted audio in a mp3 file
        myobj.save("converted.mp3")
        