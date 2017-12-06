#Max Low
#12-6-17
#fileDemo.py

dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    if 'max' in word:
        print(word.strip())
    wordCount += 1
    
print('There are', wordCount,'words in the dictionary')

