class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
        print("Student created")

    def __del__(self):
        Student.count -= 1
        print("Student destroyed")

    @classmethod
    def total_student(cls):
        print("Total objects:",cls.count)

s1 = Student("A")
s1 = Student("B")
s1 = Student("C")