from math import pi
type_figure = input()
area = 0
if type_figure == 'square':
    a = float(input())
    area = a * a
elif type_figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif type_figure == 'circle':
    radius = float(input())
    area = pi * (radius ** 2)
elif type_figure == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b / 2
print(f'{area:.3f}')
