# -*- coding: utf-8 -*-
#import json
#jsonstring = "{\"category1\": \"レディース\", \"category2\": \"トップス\", \"category3\": \"Tシャツ\", \"material\": [\"ナイロン 34%\", \"綿 66%\"], \"season\": [\"春\", \"夏\"], \"name1\": \"\", \"name2\": \"\", \"sleeve\": \"半袖\", \"feature\": \"\", \"color\": [\"ライトブルー\", \"白\"], \"size\": \"L M S\"}"
#string = json.loads(jsonstring)
#print (string)
import codecs
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
            if "サイズ" not in lines[i] and "色" not in lines[i]:
                text_s.append(lines[i])
        if not se_flag and len(string["material"]) > 0:
            if len(string["material"]) == 1:
                text.append("素材は"+" ".join(string["material"])+"です。")
            else:
                text.append("素材は"+",".join(string["material"])+"です。")
        count += 5
    se_flag = False
    if len(string["season"]) > 0:
        for i in range(count,count+5):
            s_flag = 1
            for s in string["season"]:
                if s not in lines[i]:
                    s_flag = s_flag * 0
            if s_flag == 1:
                text.append(lines[i])
                se_flag = True
                break
        if not se_flag:
            for i in range(count,count+5):
                s_flag = 1
                for s in string["season"]:
                    if s in lines[i]:
                        text.append(lines[i])
                        se_flag = True
                        break
        count += 5
    se_flag = False
    if string["sleeve"] != "":
        for i in range(count,count+5):
            if "袖" in lines[i]:
                text.append(lines[i])
                se_flag = True
                break
            if "サイズ" not in lines[i] and "色" not in lines[i] and "素材" not in lines[i]:
                text_s.append(lines[i])
        count += 5
    if len(string["color"]) > 0:
        for i in range(count,count+5):
            if "色" in lines[i] or "カラー" in lines[i]:
                text.append(lines[i])
                break
        count += 5
    if string["size"] != "":
        for i in range(count,count+5):
            if "サイズ" in lines[i]:
                text.append(lines[i])
                break
    text_s = sorted(set(text_s),key=text_s.index)
    text = text+text_s
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
    return (description)
