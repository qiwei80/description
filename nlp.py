import csv
import MeCab
import sys

def splitword(text,i,keyword):
    #mt = MeCab.Tagger("-Owakati")
    mt = MeCab.Tagger()
    mt.parse('')
    if i == 3:
        text = keyword+"の素材は" + text
    if i == 4:
        text = keyword+"の季節は" + text
    if i == 5:
        text = keyword+"の商品名は" + text
    if i == 7:
        text = keyword+"の袖は" + text
    if i == 8:
        text = keyword+"の特徴は" + text
    if i == 9:
        text = keyword+"の色は" + text
    if i == 10:
        text = keyword+"のサイズは" + text
    node = mt.parseToNode(text)
    mecab_result = []
    while node:
        word = node.surface
        pos = node.feature.split(",")
        numflag = False
        if "袖" not in text and pos[1] == "数":
            numflag = True
        
        if pos[0] != '記号' and not numflag and word not in ["%",",",".",""]:
            mecab_result.append(word)
        node = node.next
    mecab_result.append("\n")
    #print (mecab_result)
    #mecab_result = mt.parse(text)
    #return (mecab_result.split(" "))
    return (mecab_result)
def splitword2(text):
    mt = MeCab.Tagger("-Owakati")
    mt.parse("")
    mecab_result = mt.parse(text)
    return (mecab_result)
def splittext(text):
    des = text.split("\n")
    des2 = []
    for txt in des:
        des2 += txt.split("。")
    return(des2)

