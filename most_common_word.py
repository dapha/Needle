# David Phan
# Count words in a file

from collections import Counter

def rmPunc(string):
    ignore = [".", ","]
    for thing in ignore:
        string = string.replace(thing, "")
    words = string.lower().split()
    return words

def mostCommon(filename):
    file2str = ""
    count = {}
    file = open(filename, 'r')
    for line in file:
        file2str += line
    words = rmPunc(file2str)
    count = Counter(words)
    print (count.most_common(1))
        

mostCommon('words.txt')
        
    
            
