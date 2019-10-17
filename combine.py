import sys
of = open(sys.argv[1],"r")
wf = open(sys.argv[2],"w")
lines = of.readlines()
count = 0
w_text = ""
for line in lines:
    if count%2 == 0:
        w_text = line.strip("\n")
        w_text = w_text
    else:
        w_text = w_text+line
        wf.write(w_text)
        w_text = ""
    count += 1

