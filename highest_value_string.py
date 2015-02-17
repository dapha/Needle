# David Phan
# Print string with highest number value

def highest_value_string(filename):
    import re
    import operator
# Initialize Variables
    sentences={}
    sSum = 0
    aSum = {}
    letter={}
    f = open(filename) # Read in file
    inStr = f.read()
    endSentence = re.compile('[.!?][\s]{2}') # List of char to remove
    sentenceList = endSentence.split(inStr) # Break up sentences into strings
    
    for s in sentenceList:
        letter[s] = s.lower() # Convert lowercase
        letter[s] = ''.join(thing for thing in letter[s] if thing.islower()) # Merge words into single string with no spaces
        sentences[s] = list(letter[s]) # Break string into char
        sSum = 0 # Initialize count
        for arr in sentences[s]:
            arr = ord(arr) - 96 # Calculate integer value
            sSum += arr # Counter
        aSum[s] = sSum # Results

    a = max(aSum, key=aSum.get) # Find most common
    print(a, ": ", aSum[a]) # Print Most Common

    f.close # Close file

    
    
