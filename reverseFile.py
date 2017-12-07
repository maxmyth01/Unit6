#Max Low
#12/7/17
#reverseFile.py -- askes user for file then prints out all lines in reverse
file = open(input('Enter a file name:'))
for line in file:
    next = -1
    for ch in line:
        newline = []
        ch -= 1
        next += 1 
        newline[next] = line[ch]
    print(newline)