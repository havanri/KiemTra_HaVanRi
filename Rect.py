from Shape import Shape
class Rect(Shape):

    def __init__(self, rong, dai, x, y, name):
        self.Rong = rong
        self.Dai = dai
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()
        self.Name = name

    def chuVi(self):
        ChuVi = (self.Rong + self.Dai) * 2
        return ChuVi

    def dienTich(self):
        DienTich = self.Rong * self.Dai
        return DienTich
