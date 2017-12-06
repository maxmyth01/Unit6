#Max Low
#12-6-17
#longestDictionaryWord.py

dictionary = open('engmix.txt')

wordSize = 0
for word in dictionary:
    if len(word) > wordSize:
        wordSize = len(word) 
for word in dictionary:
    if wordSize == len(word):
        print(word)
