# David Phan
# Count words in a file

from collections import Counter

# Method for removing punctuation (. and ,) from string
def rmPunc(string):
    ignore = [".", ","] # Things to remove
    for thing in ignore:
        string = string.replace(thing, "") # Remove . and ,
    words = string.lower().split() # To lowercase and puts words into list
    return words

def most_common_word(filename):
    # Initialize Variables
    file2str = ""
    count = {}
    
    file = open(filename, 'r')
    for line in file:
        file2str += line # Puts lines into strings
    words = rmPunc(file2str) # Removes punctuation
    count = Counter(words) # Counts words
    print (count.most_common(1)) # Prints most common word

    file.close() # Close file  


        
    
            
