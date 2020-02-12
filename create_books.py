#Mehul
from com.abc.college.book import Book

b1 = Book('Programming in C', 900, 450)
# Internally
# 1. RAM space reserved - 6007
# 2. Book.__init__(6007, 'Programming in C', 900, 450)


b2 = Book('Programming in Python', 500, 490)
b3 = Book('Programming in Java', 1000, 560)

''' print(b1.title)
print(b2.title)
print(b3.price) '''

print(b1.get_details())
print(b3.get_details())
# Internally
# print(Book.get_details(b1))


print(b1.is_expensive())
# Internally
# print(Book.is_expensive(b1))

print(b2.is_expensive())
# Internally
# print(Book.is_expensive(b2))