# -*- coding: utf-8 -*-
#import json
#jsonstring = "{\"category1\": \"レディース\", \"category2\": \"トップス\", \"category3\": \"Tシャツ\", \"material\": [\"ナイロン 34%\", \"綿 66%\"], \"season\": [\"春\", \"夏\"], \"name1\": \"\", \"name2\": \"\", \"sleeve\": \"半袖\", \"feature\": \"\", \"color\": [\"ライトブルー\", \"白\"], \"size\": \"L M S\"}"
#string = json.loads(jsonstring)
#print (string)
import codecs
import random
def uniq_text(text,season):
    season_str=["春","夏","秋","冬"]
    for i in range(0,len(text)-1):
        text[i] = text[i].strip("\n")
        for s_w in season_str:
#            print(s_w,text[i])
#            print (text[i].find(s_w))
            if text[i].find(s_w) >= 0 and s_w not in season and len(season) > 0:
                if s_w == "春" and text[i].find("春先") >=0:
                    pass
                else:
                    text[i] = text[i].replace(s_w,"")
        if text[i][-1] != "。":
            text[i] = text[i] + "。"
        for j in range(i+1,len(text)):
            if j == len(text)-1:
                for s_w in season_str:
#                    print(s_w,text[i])
#                    print (text[i].find(s_w))
                    if text[i].find(s_w) >= 0 and s_w not in season and len(season) > 0:
                        if s_w == "春" and text[i].find("春先") >= 0:
                            pass
                        else:
                            text[i] = text[i].replace(s_w,"")
#            print ("i:",text[i])
#            print ("j",text[j])
#            print ("len i:",len(set(text[i])))
#            print ("len j:",len(set(text[j])))
#            print ("len i+j:",len(set(text[i]+text[j])))
            if len(set(text[i]))/len(set(text[i]+text[j])) > 0.7 or len(set(text[j])) /len(set(text[i]+text[j])) > 0.7:
                text[j] = text[i] 
    return (text)
def normalize(of_name,string):
    of = codecs.open(of_name,"r",'utf-8')
    lines = of.readlines()
    text = []
    se_flag = False
    text_s = []
    count = 0
    if len(string["material"]) > 0:
        for i in range(count,count+5):
            if "素材" in lines[i]:
                text.append(lines[i])
                se_flag = True
                break
            if "サイズ" not in lines[i] and "色" not in lines[i] and "カラー" not in lines[i]:
                text_s.append(lines[i])
        if not se_flag and len(string["material"]) > 0:
            if len(string["material"]) == 1:
                text.append("素材は"+" ".join(string["material"])+"です。")
            else:
                text.append("素材は"+",".join(string["material"])+"です。")
        count += 5
    se_flag = False
    season_str=["春","夏","秋","冬"]
    if len(string["season"]) > 0:
        for i in range(count,count+5):
            s_flag = 1
            for s in string["season"]:
                if s not in lines[i]:
                    s_flag = s_flag * 0
            if s_flag == 1 and lines[i].find("発売") == -1:
#                for s_w in season_str:
#                    print(s_w,lines[i])
#                    print (lines[i].find(s_w))
#                    if lines[i].find(s_w) >= 0 and s_w not in string["season"]:
#                        lines[i] = lines[i].replace(s_w,"")
                text.append(lines[i])
                se_flag = True
                break
        if not se_flag:
            for i in range(count,count+5):
                s_flag = 1
                for s in string["season"]:
                    if s in lines[i]:
#                        for s_w in season_str:
#                            print (s_w,lines[i])
#                            print (lines[i].find(s_w))
#                            if lines[i].find(s_w) >= 0 and s_w not in string["season"]:
#                                lines[i] = lines[i].replace(s_w,"")
                        text.append(lines[i])
                        se_flag = True
                        break
        count += 5
    se_flag = False
    if string["sleeve"] != "":
        for i in range(count,count+5):
            if "袖" in lines[i] and "サイズ" not in lines[i]:
                text.append(lines[i])
                se_flag = True
                break
            if "サイズ" not in lines[i] and "色" not in lines[i] and "カラー" not in lines[i] and "素材" not in lines[i]:
                text_s.append(lines[i])
        count += 5
    se_flag = False
    if len(string["color"]) > 0:
        for i in range(count,count+5):
            #modified 2019/10/3 カラー情報だけの生成文除外するのため
            if "色" in lines[i] or "カラー" in lines[i] or "素材" in lines[i] or "サイズ" in lines[i]:
                #text.append(lines[i])
                #break
                pass
            else:
                for c in string["color"]:
                    if c in lines[i]:
                        text.append(lines[i])
                        se_flag = True
        if not se_flag:
            if len(string["color"]) == 1:
                text.append("色は"+string["color"][0]+"となります。")
            else:
                mae_w =["カラーは","色は","カラーバリエーションは"]
                end_w =["色展開です。","をご用意いたしました。"]
                if random.randint(0,10)%3 != 0:
                    text.append(mae_w[random.randint(0,2)]+"、".join(string["color"])+"の"+str(len(string["color"]))+end_w[random.randint(0,1)])
                else:
                    text.append("「カラー」："+"、".join(string["color"])+"。")
        count += 5
    if string["size"] != "":
        #modified 2019/10/3サイズ情報混乱ので、生成じゃなくで、直接サイズ文出力に変更
        #for i in range(count,count+5):
        #    if "サイズ" in lines[i]:
        #        text.append(lines[i])
        #        break
        text.append("サイズ："+string["size"])
    #text_s = sorted(set(uniq_text(text_s,string["season"])),key=text_s.index)
#    print ("text:",text)
#    print ("text_s:",text_s)
    text = text+text_s
    text = sorted(set(uniq_text(text,string["season"])),key=text.index)
    description = ""
    for line in text:
        line = line.strip("\n")
        while line.find("<unk>") >= 0:
            line = line.replace("<unk>",",")
        description = description + "".join(line.split(" "))
        if description[-1] != "。":
            description = description + "。"
    while ",," in description:
        description = description.replace(",,","")
    while ",。" in description:
        description = description.replace(",。","")
    while "。," in description:
        description = description.replace("。,","。")
    while "ますます" in description:
        description = description.replace("ますます","")
    while "。ます。" in description:
        description = description.reaplace("。ます。","。")
    
    ff = codecs.open("filter.csv","r",'utf-8')
	
    filter_s = ff.readlines()
    for s in filter_s:
        s = s.strip("\n")
        while s in description:
            description = description.replace(s,"")
    return (description)
