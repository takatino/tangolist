
boinDict = {'ア':['ア','カ','サ','タ','ナ','ハ','マ','ヤ','ラ','ワ','ガ','ザ','ダ','パ','バ'], 
            'イ':['イ','キ','シ','チ','ニ','ヒ','ミ','リ','ギ','ジ','ヂ','ビ','ピ'],
            'ウ':['ウ','ク','ス','ツ','ヌ','フ','ム','ユ','ル','グ','ズ','ヅ','ブ','プ'],
            'エ':['エ','ケ','セ','テ','ネ','ヘ','メ','レ','ゲ','ゼ','デ','ベ','ペ'],
            'オ':['オ','コ','ソ','ト','ノ','ホ','モ','ヨ','ロ','ヲ','ゴ','ゾ','ド','ボ','ポ']}

smallboinDict = {'ァ':['ァ','ャ'], 'ィ':['ィ'], 'ゥ':['ゥ','ュ'], 'ェ':['ェ'], 'ォ':['ォ','ョ']}

# ァィゥェォャュョ　->　そのままor前の文字をそれに変える
# 'ー' -> 前の文字
# 'ン' -> ン
# 'ッ' -> ッ


def boinnify(word):
    boinnifiedWord = ""
    for i in range(len(word)):

        if word[i] == 'ン' or word[i] == 'ッ':
            boinnifiedWord += word[i]
            continue

        if word[i] == 'ー':
            if boinnifiedWord[i-1] in boinDict.keys(): #previous letter is boin
                boinnifiedWord += boinnifiedWord[i-1]

            elif boinnifiedWord[i-1] in smallboinDict.keys(): #previous letter is small boin
                if boinnifiedWord[i-1] in ['ァ','ャ']:
                    boinnifiedWord += 'ア'
                elif boinnifiedWord[i-1] in ['ィ']:
                    boinnifiedWord += 'イ'
                elif boinnifiedWord[i-1] in ['ゥ','ュ']:
                    boinnifiedWord += 'ウ'
                elif boinnifiedWord[i-1] in ['ェ']:
                    boinnifiedWord += 'エ'
                elif boinnifiedWord[i-1] in ['ォ','ョ']:
                    boinnifiedWord += 'オ'
            continue
    

        smallboin = checkLetterInDict(word[i], smallboinDict)
        boin = checkLetterInDict(word[i], boinDict)

        if smallboin: #letter is smallboin
            boinnifiedWord += smallboin
            continue

        if boin:
            boinnifiedWord += boin
            continue
    
    return boinnifiedWord


def checkLetterInDict(letter, dict):
    for row in list(dict.values()):
        if letter in row:
            return list(dict.keys())[list(dict.values()).index(row)]
    return False

print(boinnify('ミョーウガ'))