from alphabet import alphabets

inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
output = 0

textstr = textlist[0].lower()

textlist = []
for i in textstr:
    textlist += i



print(textlist)