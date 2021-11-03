"""
Copyright (C) 2021 SE Transcriptor - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com
"""

# Import Libraries
import os
import shutil

class Cleanup:
    """
    A class used to clean temporary files generated 
    ...

    Methods
    -------
    delete_temp_files:
        function to delete temporary files that were created while generating
        summary of youtube videos with closed captions.
    """
    
    def __init__(self):
        pass
            
    def delete_temp_files(self):
        """
        function to delete temporary files that were created while generating
        summary.
        """
        try:
            shutil.rmtree(os.getcwd() + "/" + 'temp')
        except OSError as e:
            print(e.strerror)
