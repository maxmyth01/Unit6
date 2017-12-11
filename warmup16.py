#Max low
#12-11-17
#warmup16.py -- words in dictionary start with M and end w/L

dictionary = open('engmix.txt')

for line in dictionary:
    line = line.strip()
    if line != "":
        if line[0] == 'm' and word[len(word)-1] == "l":
            print(line)
