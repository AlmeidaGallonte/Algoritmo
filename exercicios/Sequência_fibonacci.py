a = 0
b = 1
c = 0
print(a, b, end=' ')
for _ in range(0,13):
    c = a + b
    print(c, end=' ')
    a = b
    b = c