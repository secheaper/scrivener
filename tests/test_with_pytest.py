import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('source')
# sys.path.append('main')

from source.main import helper
# from source.main import transcribe_yt
from source.main import summarize

# from main import helper 

def test_always_passes():
    assert True

def test_formatSummary():
    """
    Checks the formatText function
    """
    # print(helper.formatText(""))
    # assert helper.formatText("")[-1] is None
    assert helper.formatText("Robert Frost is taking the right road to summarize your video")[-1] == '.'

def test_analyzeText():
    """
    Checks the analyze function
    """
    sentiments = ["Neutral", "Positive", "Negative"]
    assert helper.analyze("")[0] == None
    assert helper.analyze("sad")[0] in sentiments
    assert helper.analyze("very happy")[0] in sentiments
    assert helper.analyze("decent")[0] in sentiments
   

def test_Summary():
    temp = summarize.Summary("the snail smelly old beermongers . the snail stinky old beersmonger's squirmy old").summarize_text()
    assert type(temp) == list and len(temp) > 0

# def test_transcribeVideo():
#     assert type(TranscribeYtVideo('https://www.youtube.com/watch?v=yaG9mFlrB8k&ab_channel=9to5Mac').transcribe_yt_video()) == str

# def test_always_fails():
#     assert False


# def test_transcribeVideo():
#     temp = transcribe_yt.TranscribeYtVideo('https://www.youtube.com/watch?v=yaG9mFlrB8k&ab_channel=9to5Mac%27')
#     assert type(temp.transcribe_yt_video()) == str

