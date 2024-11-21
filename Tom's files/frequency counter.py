import alphabet as a

inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
textstr = textlist[0].lower()

frequencylist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in textstr:
    if i in a.alphabets:
        frequencylist[a.alphabets.index(i)] += 1
counter = 0

newalphabet = ["","","","","","","","","","","","","","","","","","","","","","","","","",""]
sortednums = sorted(frequencylist)
for i in a.alphabets:
    print(newalphabet)
    newalphabet[sortednums.index(frequencylist[a.alphabets.index(i)])] = i


while counter < 26:
    print(newalphabet[counter], sortednums[counter])
    counter += 1
