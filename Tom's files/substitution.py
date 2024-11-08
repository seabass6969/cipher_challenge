import alphabet as a

inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
output = ""

textstr = textlist[0].lower()

textlist = []
for i in textstr:
    textlist += i

outputlist = []

for i in textlist:
    x = a.alphabets.index(i)
    outputlist += a.shift[x]

for i in outputlist:
    output += i
    
output = ""
print(output)