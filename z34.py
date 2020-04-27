try:
    f = open("data.txt")
except:
    print("cannot open file")
k = 0
n = 0
s = 0
fl = 0
for line in f:
    for i in line.split():
        if k == 0:
            n = i
            k = 1
            fl=1
        else:
            if i==n and fl==1:
                k=k+1
            if i>n and fl==1:
                s=k
                fl=0
            if i<n:
                fl=1
                k=1
            n=i
if fl==1:
    s=k
print(s)
f.close()
