inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
output = ""
for i in textlist:
    textstr = i 

groupnum = 6
group = ""
grouplist = ""
grouplist2 = ""

for i in textstr:
    group += i
    if len(group) == groupnum:
        for x in group:
            grouplist += x
        grouplist2 += grouplist[3] + grouplist[0] + grouplist[2] + grouplist[5] + grouplist[1] + grouplist[4]
        output += grouplist2
    grouplist, grouplist2 = [], []
    group = ""
print(output)