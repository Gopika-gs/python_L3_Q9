f = open('D:Dora/mashup/python/readme.txt','r')
line = f.read()
count = 0
n = line.split("\n")
for i in n:
    if i:
        count+=1
print(count)