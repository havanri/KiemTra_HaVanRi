import random

shapes = ['Rect', 'Circle', 'Triangle']
with open('E:\\input.txt', 'w') as f:
    for i in range(100):
        shape_type = random.choice(shapes)
        f.write(f"#{shape_type}\n")
        if shape_type == 'Rect':
            chieu_dai = random.randint(1, 100)
            chieu_rong = random.randint(1, 100)
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            f.write(f"{chieu_dai} {chieu_rong}\n")
            f.write(f"{x} {y}\n")
        elif shape_type == 'Circle':
            ban_kinh = random.randint(1, 100)
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            f.write(f"{ban_kinh}\n")
            f.write(f"{x} {y}\n")
        else:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            c = random.randint(1, 100)
            while (a + b <= c) or (a + c <= b) or (b + c <= a):
                # Nếu ba cạnh không thỏa mãn điều kiện tam giác thì tạo lại đến khi thỏa mãn
                a = random.randint(1, 100)
                b = random.randint(1, 100)
                c = random.randint(1, 100)
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            f.write(f"{a} {b} {c}\n")
            f.write(f"{x} {y}\n")

