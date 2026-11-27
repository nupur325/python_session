class Parent:
    def parentMethod(self):
        print("Caliing parent mwthod")

class Child:
    def childmethod(parentMethod):
        print("Calling child method")

c= Child()
c.parentMethod()
c.childmethod()
