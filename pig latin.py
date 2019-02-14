import re

#returns tuple of the punctuation character found and the position it was found at or -1 if not found
def search_for_punctuation(word):
    m = re.search(r'[.,?!:;()"“”]', word)
    if m != None:
        mString = m.group()
        mPos = m.start()
        return tuple([mString,mPos])
    else:
        return -1

def pigWord(word):
    punctList = []
    while search_for_punctuation(word) != -1:
        result = search_for_punctuation(word)
        punctList.append(result)
        word = word[result[1] + 1 : len(word)]
    print(punctList)
    print(word)
    #firstLetter = word[0]
    #newWord = word.split(firstLetter)
    #newWord = "".join(newWord) + "".join(firstLetter + 'ay')
    #return newWord


stuffToParse = input("Please give me a sentence to translate to pig latin: ")
newStuff = stuffToParse.split()
x = 0
finalStuff = ''
#for _ in newStuff:
#    finalStuff = finalStuff + (pigWord(newStuff[x])) + " "
#    x=x+1
#print(finalStuff)
#print(search_for_puctuation(stuffToParse))
pigWord(stuffToParse)
