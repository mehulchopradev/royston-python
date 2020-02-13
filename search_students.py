from com.abc.college.student import Student

slist = [
    Student('mehul', 10, 'm', 90),
    Student('roy', 5, 'm', 99),
    Student('jane', 23, 'f', 95),
    Student('jill', 4, 'f', 85)
]

search = int(input('Enter roll to search: '))

for student in slist:
    if student.roll == search:
        print(student.get_details())
        break
else:
    # this block will execute when the corresponding for block has been exhausted
    # no break has been encountered in the corresponding for block
    print('Student not found')
