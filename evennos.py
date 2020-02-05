'''
    Take the user input n as an integer
    Print all the even nos till n (including n)
'''

n = int(input('Enter n: '))

# looping constructs
# while
'''
while <<truthy/true or falsy/false>>:
    I1
    I2
    I3
'''

''' i = 0
while i <= n:
    if not i % 2:
        print(i)
    i = i + 1 '''

# for loop (Preferred)
'''
for v in <<sequence of elements>>:
    I1
    I2
    I3
'''

# sequence of numbers (0-n)
# eg. n - 6 : [0,1,2,3,4,5,6]
''' for v in range(0, n + 1):
    if not v % 2:
        print(v) '''

for v in range(0, n + 1, 2):
    print(v)

