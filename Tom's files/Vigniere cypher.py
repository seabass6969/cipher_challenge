import alphabet as a

inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
for i in textlist:
    textstr = i

textlist = []
for i in textstr:
    textlist += i

textstrnum = []
for i in textstr:
    x = a.alphabets.index(i.lower()) 
    textstrnum.append(x)

key = ["A", "D", "A"]
numkey = []

for i in key:
    x = a.alphabets.index(i.lower()) 
    numkey.append(x)

textstrnum2 = []
count = 0
for i in textstrnum:
    x = i - numkey[count]
    if x < 0:
        x += 26
    textstrnum2.append(x)
    count += 1
    if count == len(numkey):
        count -= len(numkey)

textstr = []
for i in textstrnum2:
    textstr += a.alphabets[i]     

output = ""
 
for i in textstr:
    output += i

print(output)