from Parent import Parent


class Child(Parent):
    num2 = 300

    def getdata(self):
        return self.num2 + self.summation(100, 100)
obj = Child()
print(obj.getdata())
