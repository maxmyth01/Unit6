#Max Low
#12/7/17
#reverseFile.py -- askes user for file then prints out all lines in reverse
file = open(input('Enter a file name:'))
newline = []
for line in file:
    newline.append(line.strip())
newline.reverse()
print(newline)