import re

#returns tuple of the punctuation character found and the position it was found at or -1 if not found
def search_for_punctuation(word, pos = 0):
    pattern = re.compile(r'[.,?!:;()"“”]')
    m = pattern.search(word, pos)
    if m != None:
        mString = m.group()
        mPos = m.start()
        return tuple([mString,mPos])
    else:
        return -1

#this function takes a string as an input and parses it into pig latin, accounting for any punctuation and returns it
def pigWord(word):
    punctList = []
    letter_list = list(word)
    #this loop will search for punctuation in the word, and if there is any
    #store it in a separate list to be reattached to the word after parsing into pig latin
    while search_for_punctuation(word) != -1:
        letter_list = list(word)
        result = search_for_punctuation(word,-1)
        punctList.append(result)

        letter_list.pop(result[1])
        word = "".join(letter_list)

    #for debugging
    #print(punctList)
    #print(word)

    #this block of code actually turns the word into pig latin
    firstLetter = letter_list.pop(0)
    letter_list.insert(len(letter_list), firstLetter)
    letter_list.append('a')
    letter_list.append('y')

    for item in punctList: #insert punctuation into correct spot in string
        if item[1] > (len(letter_list) / 2): #if index of punctuation is more than halfway through word
            letter_list.insert(item[1] + 2 + len(punctList), item[0]) #offset the index by 2 to account for 2 new letters
        else:
            letter_list.insert(item[1], item[0])

    newWord = "".join(letter_list)
    return newWord

#this is the main program that uses above functions to parse to pig latin
stuffToParse = input("Please give me a sentence to translate to pig latin: ")
newStuff = stuffToParse.split()
x = 0
finalStuff = ''
for i in range(0,len(newStuff)):
    finalStuff = finalStuff + (pigWord(newStuff[i])) + " "
print(finalStuff)
