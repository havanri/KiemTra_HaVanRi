from Shape import Shape
class Circle(Shape):

    def __init__(self, bk, x, y, name):
        self.BK = bk
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()
        self.Name = name

    def chuVi(self):
        ChuVi = self.BK*2*3.14
        return ChuVi

    def dienTich(self):
        DienTich = pow(self.BK,2)*3.14
        return DienTich