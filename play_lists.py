nos = [6, 7, 4, 5, 6, 10, 1, 0, 4, 5]

# print all odd numbers from the nos list
for n in nos:
    if n % 2:
        print(n)

# get a new list of all odd numbers from the nos list (filtering)
''' odds = []
for n in nos:
    if n % 2:
        odds.append(n) '''

# for comprehensions
# Prerequisite - needing a new list
odds = [n for n in nos if n % 2]
print(odds)

# get a new list of all the even elements greater than 5 from the nos list (filtering)
evens = [n for n in nos if not n % 2 and n > 5]
print(evens)

# get a new list of marks added by 1 from the nos list (mapping)
''' new_nos = []
for n in nos:
    new_nos.append(n + 1) '''

new_nos = [n + 1 for n in nos]
print(new_nos)