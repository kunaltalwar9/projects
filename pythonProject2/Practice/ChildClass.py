from PerfectNumber import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 3,5)

    def getcomdata(self):
        return self.num2 + self.num + self.add()


obj = ChildImpl()
print(obj.getcomdata())
