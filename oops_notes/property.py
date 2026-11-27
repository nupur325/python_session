class Employee:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name = name 
        return

    def set_age(self,age):
        self.__age = age 
        return

    name = property(get_name,set_name,"name")
    age = property(get_age,set_age,"age")

el = Employee("Nupur",21)
print("Name",el.name,"age",el.age)

el.name = "Sur"
el.age = 22
print("Name",el.name,"age",el.age)