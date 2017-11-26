#Sam Smedinghoff
#11/26/17
#wc.py - counts the lines, words, and characters in a file

fileName = input('What file would you like to open? ')

file = open(fileName)

lines = 0
words = 0
characters = 0
for line in file:
    line = line.strip()
    lines += 1
    if line != '':
        words += line.count(' ') + 1
        characters += len(line) - line.count(' ')

print('Lines =', lines)
print('Words =', words)
print('Characters =', characters)
