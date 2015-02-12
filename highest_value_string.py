# David Phan
# Print string with highest number value

def highestString(filename):
    import re
    import operator
    sentences={}
    sSum = 0
    aSum = {}
    test={}
    f = open(filename)
    inStr = f.read()
    endSentence = re.compile('[.!?][\s]{2}')
    sentenceList = endSentence.split(inStr)
    
    for s in sentenceList:
        test[s] = s.lower()
        test[s] = ''.join(thing for thing in test[s] if thing.islower())
        sentences[s] = list(test[s])
        sSum = 0
        for arr in sentences[s]:
            arr = ord(arr) - 96
            sSum += arr
        aSum[s] = sSum

    a = max(aSum, key=aSum.get)
    print(a, ": ", aSum[a])

highestString('s.txt')

    
    
