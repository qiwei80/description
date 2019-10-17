import random

of1 = open("./data/src.csv","r")
of2 = open("./data/tgt.csv","r")
lines1 = of1.readlines()
lines2 = of2.readlines()

num = []
print (len(lines1))
for i in range(len(lines1)):
    num.append(i)
random.seed(34)
for i in range(100):
    random.shuffle(num)
wf1 = open("./data/src_r.csv","w")
wf2 = open("./data/tgt_r.csv","w")
for i in num:
    wf1.write(lines1[i])
    wf2.write(lines2[i])
print (num)
