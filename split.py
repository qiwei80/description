of = open("./data/train.csv","r")
wf1 = open("./data/src.csv","w")
wf2 = open("./data/tgt.csv","w")
lines = of.readlines()
for line in lines:
    line = line.strip("\n")
    seg = line.split("@@@")
    if len(seg) == 2:
        wf1.write(seg[0]+"\n")
        wf2.write(seg[1]+"\n")
    else:
        print (line)
