import math


def square(side):
    side_sq = math.ceil(side * side)
    return (side_sq)


side = float(input("Сторона квадрата равна: "))


print(f"Площадь квадрата равна: {side * side}")
