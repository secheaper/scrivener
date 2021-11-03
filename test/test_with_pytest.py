import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('source/main')

from main import helper
from main import summarize
from main.transcribe_yt import TranscribeYtVideo

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
   
# from main.summarize import Summary

def test_Summary():
    assert type(summary.Summarize("the snail smelly old beermongers . the snail stinky old beersmonger's squirmy old")) == str

def test_transcribeVideo():
    assert type(TranscribeYtVideo('https://www.youtube.com/watch?v=yaG9mFlrB8k&ab_channel=9to5Mac').transcribe_yt_video()) == str

# def test_always_fails():
#     assert False
