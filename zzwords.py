#Max Low
#12-6-17
#zzwords.py -- search ditionary for word containing zz

dictionary = open('engmix.txt')

for word in dictionary:
    if 'zz' in word:
        print(word.strip())

