# Mehul
from com.abc.college.student import Student

# s1 = Student() # 5003 (RAM)
# Internally
# 1. RAM 5003 memory is reserved
# 2. Student.__init__(5003)

s1 = Student('mehul chopra', 10, 'm', 45)
# Internally
# 1. RAM 5003 memory is reserved
# 2. Student.__init__(5003, 'mehul chopra', 10, 'm', 45)


''' s1.name = 'mehul chopra'
s1.roll = 10
s1.gender = 'm'
s1.marks = 45 '''

''' t = s1.get_name_roll()
name = t[0]
roll = t[-1] '''

name, roll = s1.get_name_roll() # tuple unpacking. Works with a list too
print(name)
print(roll)
# Student.get_name_roll(s1)


s2 = Student('jane', 11, 'f', 67) # 4006 (RAM)
''' s2.name = 'jane'
s2.roll = 11
s2.gender = 'f'
s2.marks = 67 '''

s3 = Student('roy', 15, 'm', 89) # 5005 (RAM)
''' s3.student_name = 'roy'
s3.r = 15
s3.gen = 'm'
s3.marks = 89 '''

print(s3.get_details())
# print(Student.get_details(s3))

print(s1.get_details())

# Internally
# print(Student.get_details(s1))


print(s2.get_details())

print(s1.get_grade())
# Internally
# print(Student.get_grade(s1))

print(s2.get_grade())
# Internally
# print(Student.get_grade(s2))

# Internally
# print(Student.get_details(s2))


# print(s1)
# print(s2)

''' print(s2.name)
print(s2.gender)

print(s1.name)
print(s1.gender) '''