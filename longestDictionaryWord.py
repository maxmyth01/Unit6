#Sam Smedinghoff
#11/26/17
#reverseFile.py - reverses the order of the lines in a file

fileName = input('What file would you like to open? ')

file = open(fileName)

lines = []
for line in file:
    lines.append(line)
lines.reverse()

for line in lines:
    print(line)
