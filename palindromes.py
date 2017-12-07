#Max Low
#12-7-17
#palindromesall the same forwards as a backwords in dictionary

dictionary = open('engmix.txt')

for word in dictionary:
    if word == word.reverse():
        print(word)
