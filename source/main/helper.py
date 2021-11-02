"""
Copyright (C) 2021 SE Transcriptor - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com
"""

import requests

def formatText(txt)->str:
    """
    This function formats the summary.
    """
    res = ""
    lines = txt.split(".")

    for line in lines:
        line = line.rstrip()
        line = line.lstrip()
        if len(line) == 0:
            continue
        if line[0] >= 'a' and line[0] <= 'z':
            res += " " + chr(ord(line[0]) - 32) + line[1:] + "."
        else:
            res += " " + line + "."
    
    return res

def analyze(txt):
    r = requests.post(
        "https://api.deepai.org/api/sentiment-analysis",
        data={
            'text': txt,
        },
        headers={'api-key': 'f68ff4f3-ee00-4008-a5dd-685b1e704656'}
    )
    js = r.json()
    try:
        return js['output']
    except KeyError:
        print(js)
        return [None]