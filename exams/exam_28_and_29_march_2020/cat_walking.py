minutes_walking_per_day = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

burned_calories = (minutes_walking_per_day * walks_per_day) * 5
if (calories_per_day / 2) <= burned_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')
