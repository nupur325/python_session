#multiple variables
class Student:
    def __init__(self):
        self.__name = ""
        self.__rollno = 0
        self.__marks = 0

    #setter method
    def set_data(self,name,rollno,marks):
        self.__name = name
        self.__rollno  = rollno

        if 0<=marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    #getter method
    def get_data(self):
        print("Name:",self.__name)
        print("Roll No:",self.__rollno)
        print("Marks:",self.__marks)

#object creation
s1 = Student()

#accepting multiple values
name = input("Enter Name:")
roll = int(input("Enter roll no:"))
marks = int(input("Enter Marks:"))

s1.set_data(name,roll,marks)
print("\nStudent Details")
s1.get_data()