# import sys
# sys.path.append('C:\\NCSU\\Sem 1\\SE\\Project 2\\transcriptor\\source\\main')


from source.main import helper

def test_string():

    assert helper.formatText("video") == ' Video.'
    assert helper.formatText("video.") == ' Video.'
    assert helper.formatText("Video.") == ' Video.'
    assert helper.formatText(" Video.") == ' Video.'