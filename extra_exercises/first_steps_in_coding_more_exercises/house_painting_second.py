x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
windows = 2 * (1.5 * 1.5)

surface_of_two_triangles = 2 * (h * x / 2)
surface_of_squares = (2 * (x * x)) - door
surface_of_rectangles = (2 * (x * y)) - windows
surface_of_small_rectangles = 2 * (y * x)

green_surface = surface_of_squares + surface_of_rectangles
red_surface = surface_of_two_triangles + surface_of_small_rectangles

green_paint_consumption = green_surface / 3.4
red_paint_consumption = red_surface / 4.3
print(f'{green_paint_consumption:.2f}')
print(f'{red_paint_consumption:.2f}')
