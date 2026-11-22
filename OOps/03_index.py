class CSStudent:
    stream = 'cse'   # Class Variable
    roomNo = 108

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

a = CSStudent('Amit',1)
b = CSStudent('Nat',2)

a.stream = 'ece'

print(a.stream)
print(b.stream)


print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roomNo)