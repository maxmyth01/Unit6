#Max Low
#12-6-17
#howManyWords.py -- prints out how many words for number of letters

dictionary = open('engmix.txt')

wordnum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in dictionary:
    wordnum[len(word.strip())-1] += 1

i = 0
while i < len(wordnum):
    print('There are', wordnum[i],"words with", i+1,'letters')
    i+=1



