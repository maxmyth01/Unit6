#Max Low
#12-13-17
#quiz6.py -- search dictionary for words with 3c's and 2p's -- number of words that start with r -- for a inputed number print the first word with that many letters -- ask user for letter print out all word w/o that letter -- load dictionary into list print the middle

dictionary = open("engmix.txt")

"""
#1
for word in dictionary:
    c=0
    p=0
    for letter in word:
        if letter == "c":
            c+=1
        elif letter == "p":
            p+=1
    if c == 3 and p == 2:
        print(word)
"""

"""
#2
num =0 
for word in dictionary:
    if word != "":
        if word.strip()[0] == "r":
            num +=1
print(num)
"""

"""
#3
num = int(input("Enter a number: "))
for word in dictionary:
    word = word.strip
    if word != "":
        if len(word) == num:
            print(word)
            break
"""

"""
#4
num =0
l = str(input("Enter a letter:"))
for word in dictionary:
    if l not in word:
        num += 1
print(num,"words do not contain", l)
"""

#5
diction = []
even_odd = False
num =0
for word in dictionary:
    word = word.strip()
    num += 1
    diction.append(word)
if num% 2 == 0:
    even_odd = True
print(even_odd)
print(dictionary[num//2])
    
    
        
        

