x = float(input()) # height house
y = float(input()) # length
h = float(input()) # height triangle wall roof
side_wall = x * y
window = 1.5 * 1.5
side_walls_total = (2 * side_wall) - (2 * window)
back_wall = x * x
front_door = 1.2 * 2
front_wall = (x * x) - front_door
front_and_back_wall = back_wall + front_wall
green_paint = (front_and_back_wall + side_walls_total) / 3.4
roof_side = x * y
roof_front = x * h / 2
roof_total = (roof_side * 2) + (roof_front * 2)
red_paint = roof_total / 4.3
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
