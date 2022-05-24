days = int(input())
total_food = float(input())
total_food_dog = 0
total_food_cat = 0
total_eaten_food = 0
total_eaten_biscuits = 0
for day in range(1, days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())
    total_food_dog += food_eaten_by_dog
    total_food_cat += food_eaten_by_cat
    total_eaten_food += (food_eaten_by_dog + food_eaten_by_cat)
    if day % 3 == 0:
        total_eaten_biscuits += (food_eaten_by_cat + food_eaten_by_dog) * 0.10
total_eaten_food_percent = (total_eaten_food / total_food) * 100
total_food_dog_percent = (total_food_dog / total_eaten_food) * 100
total_food_cat_percent = (total_food_cat / total_eaten_food) * 100

print(f"Total eaten biscuits: {round(total_eaten_biscuits)}gr.")
print(f"{total_eaten_food_percent:.2f}% of the food has been eaten.")
print(f"{total_food_dog_percent:.2f}% eaten from the dog.")
print(f"{total_food_cat_percent:.2f}% eaten from the cat.")
