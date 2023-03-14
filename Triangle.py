import math

from Shape import Shape
class Triangle(Shape):

    def __init__(self, a, b, c, x, y, name):
        self.A = a
        self.B = b
        self.C = c
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()
        self.Name = name

    def chuVi(self):
        ChuVi = self.A + self.B + self.C
        return ChuVi

    def dienTich(self):
        p = self.ChuVi/2
        DienTich =math.sqrt(p*(p-self.A)*(p-self.B)*(p-self.C))
        return DienTich