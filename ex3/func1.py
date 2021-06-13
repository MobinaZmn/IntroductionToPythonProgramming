def func1(s):
    SplitedSentence = []
    tmp = ''
    for c in s:
        if c == ' ':
            SplitedSentence.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        SplitedSentence.append(tmp)
    return SplitedSentence
