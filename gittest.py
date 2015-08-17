n = 100
a = [i for i in range(2, n+1)]
for i in a:
    j = i*2
    while j <= n:
        if j in a:
            a.remove(j)
        j += i
print(a)

def func(a, b):
    return a*a+b*b

print(func(10, 39))
