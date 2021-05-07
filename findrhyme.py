import json

#ァィゥェォ->前の文字を変換orそのまま
smallboinDict2 = {'ァ':'ア', 'ィ':'イ', 'ゥ':'ウ', 'ェ':'エ', 'ォ':'オ'}

#example: ティッシュ ->　エィッイゥ　-> イッウ

def rhymekey(boin):
    altboin = ""
    if any(x in boin for x in list(smallboinDict2.keys())):
        for i in range(len(boin)):
            if boin[i] in list(smallboinDict2.keys()) and i > 1:
                altboin = altboin[:-1]
                altboin += smallboinDict2[boin[i]]
            else:
                altboin += boin[i]
        return altboin
    else:
        return boin




f = open(r'./tangolist.txt', 'r')
lines = f.read().splitlines()
max_lines = len(lines)
f.close()

rhymeDict = {}

#create rhymeDict by appending matching rhymekeys
for i in range(max_lines):
    linetext = lines[i].split(",")
    thiskey = rhymekey(linetext[2])

    if thiskey in list(rhymeDict.keys()):
        rhymeDict[thiskey].append(linetext[0])
    
    else:
        rhymeDict[thiskey] = [linetext[0]]

#delete rhymes which only has a few words
for key in list(rhymeDict):
    if len(rhymeDict[key]) < 4:
        del rhymeDict[key]


nf = open(r'./newrhymelist.json', 'a')
json.dump(rhymeDict, nf, ensure_ascii=False)
nf.close()

print("done!")