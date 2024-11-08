import alphabet as a

inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
textstr = textlist[0].lower()

frequencylist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in textstr:
    if i in a.alphabets:
        frequencylist[a.alphabets.index(i)] += 1
counter = 0
while counter < 25:
    print(a.alphabet[counter], frequencylist[counter])
    counter += 1