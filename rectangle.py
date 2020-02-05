def perimeter_rectangle(length, breadth):
    '''
    this function takes in length and breadth
    and returns the perimeter
    '''
    return 2 * (length + breadth)

def area_rectangle(length, breadth):
    return length * breadth

# float(), bool(), str(), int()
l = int(input('Enter length: '))
b = int(input('Enter breadth: '))

p = perimeter_rectangle(l, b)
a = area_rectangle(l, b)

print(p) # built in function print()
print(a)