import pandas
from Triangle import  Triangle
from Circle import  Circle
from Rect import  Rect
def menu():
    print("MENU")
    print("1. Đọc dữ liệu hình từ input.txt")
    print("2. Liệt kê hình có chu vi lớn nhất và hình có diện tích lớn nhất")
    print("3. Kiểm tra số lượng hình chồng lên nhau nhiều nhất")
    print("4. Thoát chương trình")


def exit_program():
    print("Chương trình đã kết thúc")
    exit()
while True:
    menu()
    choice = input("Vui lòng chọn một chức năng: ")
    if choice == "1":
        shapes = []
        with open('E:\\input.txt', "r") as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                shape_type = lines[i].strip()[1:]  # skip the '#'
                if shape_type == 'Circle':
                    name = lines[i].strip()
                    print(name)
                    radius = int(lines[i + 2].strip())
                    x, y = map(int, lines[i + 3].strip().split())
                    shapes.append(Circle(radius, x, y, name))
                    i += 4
                elif shape_type == 'Triangle':
                    name = lines[i + 1].strip()
                    a, b, c = map(int, lines[i + 2].strip().split())
                    x, y = map(int, lines[i + 3].strip().split())
                    shapes.append(Triangle(a, b, c, x, y, name))
                    i += 4
                elif shape_type == 'Rect':
                    name = lines[i + 1].strip()
                    width, height = map(int, lines[i + 2].strip().split())
                    x, y = map(int, lines[i + 3].strip().split())
                    shapes.append(Triangle(width, height, x, y, name))
                    i += 4
        print(shapes)
    elif choice == "2":
        with open('E:\\input.txt', "r") as file_shape:  # open file in a with statement
            counter = 0
            Shape = []
            chuVi = 0
            dienTich = 0
            cvHinhTron = Circle(0,0,0)
            dtHinhTron = Circle(0,0,0)
            cvhinhTamGiac = Triangle(0,0,0,0,0)
            dthinhTamGiac = Triangle(0,0,0,0,0)
            cvhinhChuNhat = Rect(0,0,0,0)
            dthinhChuNhat = Rect(0,0,0,0)
            for line in file_shape:  # iterate line by line
                counter = counter + 1
                Shape.append(line)
                if (counter % 3 == 0):
                    res = []
                    for sub in Shape:
                        res.append(sub.replace("\n", ""))
                    paramsCanh = [int(e) for e in res[1].split()]
                    paramsToado = [int(e) for e in res[2].split()]
                    if res[0] == "#Triangle":
                          # split line and convert string elements into int
                        triangle = Triangle(paramsCanh[0], paramsCanh[1], paramsCanh[2], paramsToado[0], paramsToado[1])
                        if(triangle.ChuVi > chuVi):
                            chuVi = triangle.ChuVi
                            cvhinhTamGiac = triangle
                        if (triangle.DienTich > dienTich):
                            dienTich = triangle.DienTich
                            dthinhTamGiac = triangle
                    elif res[0] == "#Circle":
                        circle = Circle(paramsCanh[0], paramsToado[0], paramsToado[1])
                        if (circle.DienTich > chuVi):
                            chuVi = circle.DienTich
                            cvHinhTron = circle
                        if (circle.DienTich > dienTich):
                            dienTich = circle.DienTich
                            dtHinhTron = circle
                    else:
                        rect = Rect(paramsCanh[0], paramsCanh[1], paramsToado[0], paramsToado[1])
                        if (rect.ChuVi > chuVi):
                            chuVi = rect.ChuVi
                            cvhinhChuNhat = rect
                        if (rect.DienTich > dienTich):
                            dienTich = rect.DienTich
                            dthinhChuNhat = rect
                    Shape.clear()
            print('Chu vi lon nhat', cvHinhTron.chuVi())
            arrayCv = []
            arrayCv.append(cvHinhTron)
            arrayCv.append(cvhinhTamGiac)
            arrayCv.append(cvhinhChuNhat)
            sorted(arrayCv, key=lambda x: x.ChuVi, reverse=True)

            arrayDt = []
            arrayDt.append(dtHinhTron)
            arrayDt.append(dthinhTamGiac)
            arrayDt.append(dthinhChuNhat)
            sorted(arrayDt, key=lambda x: x.DienTich, reverse=False)
            print('Chu vi lon nhat', arrayCv[0].ChuVi)
            print('Dien tich lon nhat', arrayCv[0].DienTich)
    elif choice == "3":
        print("3")


    elif choice == "4":
        exit_program()
    else:
        print("Vui lòng chọn một lựa chọn hợp lệ.")