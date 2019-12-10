from math import hypot

class Vector:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __repr__(self):
        return "Vector(%r,%r)" %(self.a,self.b)

    def __abs__(self):
        return hypot(self.a,self.b)
    

    def __mul__(self,scalar):
        return Vector(self.a*scalar,self.b*scalar)


    def __add__(self,v2):
        return Vector(self.a+v2.a,self.b+v2.b)

    def __bool__(self):
        return bool(self.a or self.b)

Vector(1,2)*3 #this is fine

#Try 3*Vector(1,2)  这是不行的
#__repr__和__str__
#利用这种方法，每次运算的创建一个新的例子，不会改变原先的东东

#bool 一般情况下，若class x中未定义__bool__或者__len__，bool(x)会返回一个True
#若定义了__len__,未定义__bool__，则返回值会由长度决定。
#p12页鸟的位置没看懂

