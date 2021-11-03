"""
Copyright (C) 2021 SE Transcriptor - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com
"""

# Import Libraries
from transformers import pipeline

class Summary:
    """
    A class used to generate summary text from the transcribed text provided.
    
    ...

    Attributes
    ----------
    transcribed_text : str
        text extracted from video
        
    Methods
    -------
    summarize_text:
        Generate the summary using Hugging Face.
    """
    
    
    def __init__(self,transcribed_text):
        """
        Parameters
        ----------
        transcribed_text : str
            text extracted from video
        """
        self.transcribed_text = transcribed_text
    
    def summarize_text(self):
        """ 
        Generate summary for Youtube videos with Closed Captions
        """
        
        #use summarization model from pipeline object from transfomrers
        summarizer = pipeline('summarization', model="t5-base", tokenizer="t5-base")
        
        #initializing empty list
        summary_text = []
        
        itrs = len(self.transcribed_text) // 1000
        for i in range(itrs+1):
            start = 1000 * i
            end = 1000 * (i + 1) 
            #splitting text into chunks of 1000 characters
            output = summarizer(self.transcribed_text[start:end])[0]['summary_text']
            #appending summary output of each chunk to summary_text list
            summary_text.append(output)
        
        text = ''
        for i in summary_text:
            text += i + '\n'

        f = open('summary.txt', 'a')
        f.write(text)
        f.close()
        
        #return summary_text to calling function
        return summary_text