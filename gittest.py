n = 100
a = [i for i in range(2, n+1)]
for i in a:
    j = i<<1
    while j <= n:
        if j in a: a.remove(j)
        j += i
print(a)
