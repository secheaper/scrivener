import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('source/main')

import helper

def test_always_passes():
    assert True

def test_analyzeText():
    """
    Checks the analyze function
    """
    sentiments = ["Neutral", "Positive", "Negative"]
    assert helper.analyze("sad")[0] in sentiments
   
# def test_always_fails():
#     assert False
