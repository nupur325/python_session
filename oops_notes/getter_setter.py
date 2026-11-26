#getter method
class Student:
    def __init__(self):
        self.__marks = 0
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        self.__marks = marks

s = Student()
print("Before setter marks:",s.get_marks())
s.set_marks(95)
print("After setter marks:",s.get_marks())