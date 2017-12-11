#Max low
#12-11-17
#warmup16.py -- words in dictionary start with M and end w/L

dictionary = open('engmix.txt')

Mlist = []
for line in dictionary:
    if line.strip()[0] == 'm':
        Mlist.append(line)
for word in Mlist:
    if word[len(word)-1] == "l":
        print(word)