class Test:
    def __init__(self):
        self.a = 10
    def fun(self):
        self.b = 20

    def show(self):
        print(self.a)
        print(self.b)
        print(self.b)

t = Test()
t.fun()
t.c = 30
t.show()