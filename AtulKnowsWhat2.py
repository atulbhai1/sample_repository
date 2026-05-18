import math

#My stupid IDE auto-imported things without me knowing or it telling me(maybe I ignored it, idk?) and I had to delete them.-> explains previous submission
#My body code is the same; I hand-typed it.
class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img
    def addComplex(self, other):
        return Complex(self.real + other.real, self.img + other.img)
    def subtractComplex(self, other):
        return Complex(self.real - other.real, self.img - other.img)
    def multiplyComplex(self, other):
        new_real = self.real * other.real - other.img * self.img
        new_img = self.real*other.img + other.real*self.img
        return Complex(new_real, new_img)
    def divideComplex(self, other):
        numerator = self.multiplyComplex(other.conjugate())
        denominator = other.multiplyComplex(other.conjugate())
        #now denominator is all real, can do simpler math w/ that real part of it, maybe from another method we made, hmm....
        return numerator.divide_float(denominator.real)
    def divideFloat(self, value):
        return Complex(self.real/value, self.img/value)
    def divide_float(self, value):
        return self.divideFloat(value)
    def add_float(self, value):
        return self.addFloat(value)
    def subtract_float(self, value):
        return self.subtractFloat(value)
    def multiply_float(self, value):
        return self.multiplyFloat(value)
    def addFloat(self, value):
        return Complex(self.real + value, self.img)
    def subtractFloat(self, value):
        return Complex(self.real - value, self.img)
    def multiplyFloat(self, value):
        return Complex(self.real*value, self.img*value)
    def abs(self):
        return math.sqrt(self.real**2 + self.img**2)
    def pow(self, n:int):
        if n == 0:
            return Complex(1, 0)
        elif n > 0:
            temp = Complex(self.real, self.img)
            for i in range(1, n):
                temp = temp.multiplyComplex(self)
            return temp
        elif n < 0:
            temp = Complex(self.real, self.img)
            for i in range(1, n):
                temp = temp.multiplyComplex(self)
            temp = Complex(1, 0).divideComplex(temp)
            return temp
    def conjugate(self):
        return Complex(self.real, self.img*-1)
    def getReal(self):
        return self.real
    def getImag(self):
        return self.img
    def __str__(self):
        return f"{self.real:.2f} + {self.img:.2f}i"
    def __eq__(self, other):
        if type(other) == float or type(other) == int:
            if self.img == 0 and self.real == other:
                return True
            else:
                return False
        elif type(other) == Complex:
            if self.real == other.real and self.img == other.img:
                return True
            else:
                return False
        else:
            return False
