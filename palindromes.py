#Max Low
#12-7-17
#palindromesall the same forwards as a backwords in dictionary

dictionary = open('engmix.txt')

for word in dictionary:
    letter = []
    r = []
    for ch in word:
        letter.append(ch)
    for ch in word:
        r.append(ch)
    r.reverse()
    if letter == r:
        print(word)
