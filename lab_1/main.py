import math


def max_triangle_square():
    sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
    sides = sorted(sides, reverse=True)
    smax = 0
    for i in range(len(sides)):
        a = sides[i]
        for j in range(i + 1, len(sides)):
            b = sides[j]
            for k in range(j + 1, len(sides)):
                c = sides[k]
                if a + b > c and a + c > b and b + c > a:
                    p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if s > smax:
                    smax = s
    print("Максимальная площадь треугольника", smax)


def main():
    print('Квадратное неравенство. Введите 3 числа через пробелы')
    a, b, c = map(int, input().split(' '))
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'x1: {x1}\nx2: {x2}')
    elif d == 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        print(f'x1: {x1}')
    else:
        print('Корней нет')


if __name__ == '__main__':
    max_triangle_square()
    main()
