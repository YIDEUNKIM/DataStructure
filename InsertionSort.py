a = [5, 4, 3, 2, 1]

print(a)
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp

print(a)