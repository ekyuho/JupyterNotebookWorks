import re
with open("logall.txt") as f: lines = f.readlines()

a=[]
i = 1
for line in lines:
    if line.startswith("  SEC:"):
        #print(i, line.replace('\n',''))
        try:
            s = re.search(r" D(\d*,\d*), ", line).group(1)
        except AttributeError:
            s = ""
        print(i,',',s)
    if line.startswith("2019"):
        a.append((i, line.replace('\n','')))
    i += 1

for x in a:
    print(x)
