f = open("data.txt")
k = 0
n = 0
s = 0
for line in f:
    for i in line.split():
        if k == 0:
            n = i
            k = k + 1
        else:
            if i < n:
                k = 1
            if i == n:
                k = k + 1
            n = i
print(k)
f.close()
