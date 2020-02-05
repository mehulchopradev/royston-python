'''
Take the user input n as an integer.
Write logic to print whether that n is an even or odd number
'''

n = int(input('Enter n: '))

# branching (2 branches)
# if - else
'''
if <<relational arithmetic logical expression that evaluates to truthy/true or falsy/false>>:
    I1
    I2
else:
    I3
    I4
'''

''' if n % 2:
    print('It is odd')
else:
    print('It is even') '''

# Pre requisite
# both the branches must have 1 line of code
# if comprehensions
print('It is odd') if n % 2 else print('It is even')