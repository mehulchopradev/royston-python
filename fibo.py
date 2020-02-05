'''
Take user input n as integer : n = 8
0 1 1 2 3 5 8 13
'''
n = int(input('Enter n: '))
a, b = 0, 1

print(a)
print(b)

for v in range(1, n - 2 + 1):
    c = a + b
    print(c)
    a, b = b, c