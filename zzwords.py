#Max Low
#12-6-17
#zzwords.py -- search ditionary for word containing zz

dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    if 'zz' in word:
        print(word.strip())
    wordCount += 1
    
print('There are', wordCount,'words in the dictionary')

