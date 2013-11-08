class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000: raise StopIteration
        return self.a
    def __iter__(self):
        return self
        
fibs = Fibs()
print list(fibs)
exit()
for f in fibs:
    print f
    if f > 1000:
        break