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

def get_shape_from_file():
    shapes = []
    with open('E:\\input.txt', "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            shape_type = lines[i].strip()[1:]  # skip the '#'
            if shape_type == 'Circle':
                radius = int(lines[i + 1].strip())
                x, y = map(int, lines[i + 2].strip().split())
                shapes.append(Circle(radius, x, y, shape_type))
                i += 3
            elif shape_type == 'Triangle':
                a, b, c = map(int, lines[i + 1].strip().split())
                x, y = map(int, lines[i + 2].strip().split())
                shapes.append(Triangle(a, b, c, x, y, shape_type))
                i += 3
            elif shape_type == 'Rect':
                width, height = map(int, lines[i + 1].strip().split())
                x, y = map(int, lines[i + 2].strip().split())
                shapes.append(Rect(width, height, x, y, shape_type))
                i += 3
    return shapes
def exit_program():
    print("Chương trình đã kết thúc")
    exit()
while True:
    menu()
    choice = input("Vui lòng chọn một chức năng: ")
    if choice == "1":
        shapes = get_shape_from_file()
        print(shapes)
    elif choice == "2":
        shapes = get_shape_from_file()
        hinhCVMax = max(shapes, key=lambda x: x.chuVi())
        hinhDTMax = max(shapes, key=lambda x: x.dienTich())
        print(f'Hình có chu vi lơn nhất là {hinhCVMax.Name} có chu vi là {hinhCVMax.ChuVi}')
        print(f'Hình có diện tích lơn nhất là {hinhDTMax.Name} có diện tích là {hinhDTMax.ChuVi}')
    elif choice == "3":
        print("3")


    elif choice == "4":
        exit_program()
    else:
        print("Vui lòng chọn một lựa chọn hợp lệ.")