import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('source/main')

import helper

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
    # assert helper.analyze("")[0] == None
    assert helper.analyze("sad")[0] in sentiments
    assert helper.analyze("very happy")[0] in sentiments
    assert helper.analyze("decent")[0] in sentiments
   
# def test_always_fails():
#     assert False
