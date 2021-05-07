f = open(r'./tangolist.txt', 'r')
lines = f.read().splitlines()
max_lines = len(lines)
f.close()

for i in range(3):
    linetext = lines[i].split(",")

    
#ァィゥェォ->前の文字を変換orそのまま
smallboinDict2 = {'ァ':'ア', 'ィ':'イ', 'ゥ':'ウ', 'ェ':'エ', 'ォ':'オ'}


def rhymekey(boin):
    altboin = ""
    if any(x in boin for x in list(smallboinDict2.keys())):
        for i in range(len(boin)):
            if boin[i] in list(smallboinDict2.keys()) and i > 1:
                altboin = newboin[:-1]
                altboin += smallboinDict2[boin[i]]
            else:
                altboin += boin[i]
        return [boin, altboin]
    else:
        return [boin]

print(rhymekey("ウオッアウ"))