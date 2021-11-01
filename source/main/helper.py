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
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    return r.json()['output']