# Module
# name -> series
'''
House all library functions related to generating mathematical series
'''

# every module in python has a built in variable: __name__

def get_fibo_series(n):
    # n = 8: '0 1 1 2 3 5 8 13'
    result = ''
    a, b = 0, 1
    result += str(a) + ' ' + str(b) + ' '

    for _ in range(1, n - 2 + 1):
        c = a + b
        result += str(c) + ' '

        a, b = b, c
    
    return result

def get_odd_series(n):
    # n = 5: '1 3 5'
    result = ''
    for v in range(1, n + 1, 2):
        result += str(v) + ' '
    return result

# print(__name__)
# when the module is run directly - __main__
# when the module is not run directly i.e. imported - com.abc.lib.series

if __name__ == '__main__':
    n = int(input('Enter n: '))
    print(get_fibo_series(n))
    print(get_odd_series(n))