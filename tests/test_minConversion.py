import sys
sys.path.append('C:\\NCSU\\Sem 1\\SE\\Project 2\\transcriptor\\source\\helper')

print(sys.path)

import split_audio

def test_min():
    """
    Checks if number of minutes is correctly converted to seconds
    """

    swa = split_audio.splitwavaudio(r"C:\NCSU\Sem 1\SE\Project 2\transcriptor\test", r"C:\NCSU\Sem 1\SE\Project 2\transcriptor\test\valid video 1.mp4")

    assert swa.get_duration(1) == 60000

test_min()