f = open(r'./VDRJ_Ver1_1_Research_Top60894.csv', 'r')
lines = f.readlines()
f.close()

nf = open(r'./newtangolist.txt', 'w')



for i in range(77-1, 60970):
    linetext = lines[i].split(",")
    if linetext[15] in ["#N/A", "0"] or linetext[14] in ["*", "＊"]:
        continue
    if len(linetext[14])*len(linetext[15]) == 1 and ord(linetext[15]) - ord(linetext[14]) == 96:
        continue
    print(linetext[15])
    nf.write(linetext[14] + "," + linetext[15] + "\n") #14:単語 15:読み（カタカナ）

nf.close() 