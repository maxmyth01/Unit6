#Max Low
#12-6-17
#howManyWords.py -- prints out how many words for number of letters

dictionary = open('engmix.txt')

list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in dictionary:
    list[len(word)] += 1

print(list)

