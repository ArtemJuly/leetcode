class BaseFigure:
    n_dots = None

    def __init__(self) -> None:
        self.validate

    def area():
        raise NotImplementedError
    
    def validate():
        raise NotImplementedError
    

class Rectangle(BaseFigure):
    n_dots = 4
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

        self.validate()

    
    def area(self):
        return self.a * self.b
    
    def validate(self):
        return self.a, self.b
    

class Triangle(BaseFigure):
    n_dots = 3
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

        self.validate()

    

    def area(self):
        p = (self.a + self.b + self.c) * 0.5
        s = (p * (p - self.a) * (p - self.b) * (p -self.c)) ** 0.5
        return s
    
    def validate(self):
        if (self.a >= self.b + self.c) | (self.b >= self.a + self.c) | (self.c >= self.a + self.b):
            raise ValueError("triangle inequality does not hold")
        



tr_2 = Triangle(4,5,5)
square_2 = tr_2.area()
tr_2.validate()
print(square_2)

rec2 = Rectangle(2, 5)
srec = rec2.area()
rec2.validate()
print(srec)

print(tr_2.c)\