#setter method
class Student:
    def __init__(self):
        self.__marks = 0
    def set_marks(self,marks):
        self.__marks = marks

s = Student()

s.set_marks(90)
