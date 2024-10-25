alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabets_frequency = []
for i in range(0,26):
    alphabets_frequency.append(0)
text = "BRXFD QQRWO RVHDK RPLQJ SLJHR Q.LIB RXUKR PLQJS LJHRQ GRHVQ RWFRP HEDFN,WKHQ ZKDWB RXKDY HORVW LVDSL JHRQ."
for i in [*text]:
    try:
        indexs =alphabets.index(i.lower())
        alphabets_frequency[indexs] += 1
    except:
        pass


for index, i in enumerate(alphabets_frequency):
    print(alphabets[index], alphabets_frequency[index])