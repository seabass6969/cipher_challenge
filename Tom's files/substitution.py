import alphabet as a

inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()


textstr = textlist[0].lower()

textlist = []
for i in textstr:
    textlist += i

outputlist = []

for i in textlist:
    x = a.alphabets.index(i)
    outputlist += a.shift[x]
output = ""
for i in outputlist:
    output += i

print(output)