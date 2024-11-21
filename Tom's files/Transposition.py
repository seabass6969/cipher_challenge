inputtext = (open("text.txt", "r"))
textlist = inputtext.readlines()
for i in textlist:
    textstr = i 

groupnum = 6
group = ""
grouplist = ""
groupstr = ""
reset = False
output = ""

for i in textstr:
    group += i
    if len(group) == groupnum:
        for x in group:
            grouplist += x
        groupstr += grouplist[4] + grouplist[5] + grouplist[3] + grouplist[1] + grouplist[0] + grouplist[2]
        output += groupstr
        reset = True
    if reset:    
        grouplist, groupstr = [], ""
        group = ""
        reset = False
print(output)