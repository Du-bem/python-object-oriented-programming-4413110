# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "ClassA"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = 'ClassB'


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)

c = C()
print(C.__mro__)
c.showprops()