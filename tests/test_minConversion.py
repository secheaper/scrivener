import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('source')
# sys.path.append('main')

from helper import split_audio

def test_min():
    """
    Checks if number of minutes is correctly converted to seconds
    """

    swa = split_audio.splitwavaudio('.', 'audio_files_jackhammer.wav')

    assert swa.get_time(1)==60000