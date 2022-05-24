from math import floor, ceil
square_meters = int(input())
grape_per_sqm = float(input())
needed_lt_wine = int(input())
workers = int(input())
total_grape = square_meters * grape_per_sqm
total_wine = (total_grape * 0.4) / 2.5
diff = abs(needed_lt_wine - total_wine)
workers_wine = floor(ceil(diff / workers))
if total_wine < needed_lt_wine:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(total_wine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(workers_wine)} liters per person.')
