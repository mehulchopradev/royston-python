# Module
# name -> menu

'''
1. Fibo series
2. Odd series
3. Even or Odd
4. Exit
Enter choice: 1
Enter n: 8
0 1 1 2 3 5 8 13
1. Fibo series
2. Odd series
3. Even or Odd
4. Exit
Enter choice: 2
Enter n: 5
1 3 5
1. Fibo series
2. Odd series
3. Even or Odd
4. Exit
Enter choice: 3
Enter n: 6
Even
1. Fibo series
2. Odd series
3. Even or Odd
4. Exit
Enter choice: 4
'''

# import the module
''' import series
import math '''

# import the functions directly from the module
from series import get_fibo_series, get_odd_series
from math import even_odd

while True:
    print('1. Fibo series\n2. Odd series\n3. Even or Odd\n4. Exit')
    choice = int(input('Enter choice: '))
    if choice == 1 or choice == 2 or choice == 3:
        n = int(input('Enter n: '))
    
    if choice == 1:
        # compute fibo series
        # pass # makes the python environment ignore empty blocks and not raise an error for it
        # print(series.get_fibo_series(n))
        print(get_fibo_series(n))
    elif choice == 2:
        # print(series.get_odd_series(n))
        print(get_odd_series(n))
    elif choice == 3:
        # print(math.even_odd(n))
        print(even_odd(n))
    else:
        break # breaks from the inner most loop explicitly