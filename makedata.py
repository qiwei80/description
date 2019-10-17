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
    return (mecab_result.split(" "))
def splittext(text):
    des = text.split("\n")
    des2 = []
    for txt in des:
        des2 += txt.split("。")
    return(des2)

#csv_file = open("data/tops.csv","r")
csv_file = open(sys.argv[1],"r")
of = csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="\r\n",quotechar='"',skipinitialspace=True)
#wf1 = open("tops_train.csv","w")
#wf2 = open("tops_tgt.csv","w")
wf = open(sys.argv[2],"w")
header = next(of)
#print (header)
loop = 0
for row in of:
#    print (row)
    #des = splittext(row[11])
    des = splittext(row[12])
    if row[7] == "":
        row[7] = "袖"
    #print (row[3])
    #print (splitword(row[3]))
    for des_text in des:
        for i in range(3,10):
            if i != 6:
              for text in splitword(row[i],-1,""):
    #         print (text)
                if text in des_text and text not in ["\n","、","。","：","(",")"]:
               #     print (row[i].strip("\n"),"|",text,"|",des_text)
                    if len(splitword(row[i],-1,"")) > 1:
                        #wf1.write(" ".join(splitword(row[i],i)))
                        #wf2.write(" ".join(splitword2(des_text)))
                        w_text = " ".join(splitword(row[i],i,sys.argv[3])) + "@@@" + " ".join(splitword2(des_text))
                        wf.write(w_text)
                        break
    #print (des)
    loop += 1
    print (loop)
    #if loop > 10:
    #    exit()
