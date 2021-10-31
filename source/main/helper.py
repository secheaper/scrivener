def formatText(txt)->str:
    res = ""
    for i in range(len(txt)):
        if i == 0 and txt[i] >= 'a' and txt[i] <= 'z':
            res += chr(ord(txt[i]) - 32)
        elif i > 0 and txt[i-1] == '.' and txt[i] == " ":
            continue
        elif i > 0 and res[-1] == '.' and txt[i] >= 'a' and txt[i] <= 'z':
            res += chr(ord(txt[i]) - 32)
        else:
            res += txt[i]
    
    return res