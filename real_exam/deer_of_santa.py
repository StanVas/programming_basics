from math import ceil
days_away = int(input())
left_food = int(input())
food_per_day_for_first_deer = float(input())
food_per_day_for_second_deer = float(input())
food_per_day_for_third_deer = float(input())
first = food_per_day_for_first_deer * days_away
second = food_per_day_for_second_deer * days_away
third = food_per_day_for_third_deer * days_away
total = first + second + third
diff = abs(total - left_food)
if left_food >= total:
    print(f'{int(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
