inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
output = 0
for i in textlist:
    textstr = i 

### remove blankspace ###
textstr2 = ""
for i in textstr:
    if not i == " ":
        textstr2 += i

### add spaces ###
count = 0
output = ""
for i in textstr2:
    count += 1
    output += i
    if count % 6 == 0:
        output += ""

print(output)