import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('source')
# sys.path.append('main')

from helper import split_audio
import os
def test_min():
    """
    Checks if number of minutes is correctly converted to seconds
    """
    folder = os.getcwd() + "/"
    file = 'audio_files_jackhammer.wav'
    swa = split_audio.splitwavaudio(folder, file)

    assert swa.get_time(1)==60000