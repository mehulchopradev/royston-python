i = 4 # scope (module)
k = 10 # scope (module)
m = 5 # scope (module)
n = 10 # scope (module)

def abc():
    j = 5 # scope (abc)

    print(j) #5
    print(i) #4

    k = 20 # scope (abc)
    print(k) # 20

    # m = m + 10 # this will not work. Cannot mix global with local variables in operations

    global n # after this statement, n will always refer the module level variable. In general avoid it
    n = n + 20

abc()
print(i) #4
# print(j) # will not work as scope of j is only the abc()
print(k) # 10
print(n) # 30

'''
Scope of any variable in python is either the module (global) scope
or the function (local) scope.
Unlike other languages where the scope of the variables is the block in which it is defined.
if-else, for, while, class
'''