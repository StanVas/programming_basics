from math import ceil, floor
vacation_days = int(input())
total_food = int(input())
food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input())
total_dog_food = food_per_day_dog * vacation_days
total_cat_food = food_per_day_cat * vacation_days
total_turtle_food = (food_per_day_turtle * vacation_days) / 1000
total = total_dog_food + total_cat_food + total_turtle_food
diff = abs(total_food - total)
if total_food >= total:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
