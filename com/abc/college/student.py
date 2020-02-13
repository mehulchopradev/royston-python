# Roy
class Student:

    # Called at the time of object creation
    # Has code that creates attributes in an object
    # Constructor
    def __init__(self, name, roll, gender, marks):
        self.name = name
        self.roll = roll
        self.gender = gender
        self.marks = marks

    def get_details(self):
        # self - s1 (5003), s2 (4006)
        # self - current object address
        return 'Name: ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + \
            str(self.roll) + '\nMarks: ' + str(self.marks)

    def get_grade(self):
        marks = self.marks

        if marks > 100 or marks < 0:
            grade = 'I'
        elif marks >= 70:
            grade = 'A'
        elif marks >= 60:
            grade = 'B'
        elif marks >= 40:
            grade = 'C'
        else:
            grade = 'F'
        return grade

    def get_name_roll(self):
        return (self.name, self.roll)