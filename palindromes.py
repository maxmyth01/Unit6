#Max Low
#12-7-17
#palindromes all the same forwards as a backwords in dictionary

dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip
    if word != "":
        letter = []
        for ch in word:
            letter.append(ch)
        if letter == letter.reverse():
            print(word)
