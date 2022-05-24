type_flowers = input()
flower_amount = int(input())
budget = int(input())
cost = 0
if type_flowers == "Roses":
    cost = flower_amount * 5
    if flower_amount > 80:
        cost -= cost * 0.1
elif type_flowers == "Dahlias":
    cost = flower_amount * 3.8
    if flower_amount > 90:
        cost -= cost * 0.15
elif type_flowers == "Tulips":
    cost = flower_amount * 2.8
    if flower_amount > 80:
        cost -= cost * 0.15
elif type_flowers == "Narcissus":
    cost = flower_amount * 3
    if flower_amount < 120:
        cost += cost * 0.15
elif type_flowers == "Gladiolus":
    cost = flower_amount * 2.5
    if flower_amount < 80:
        cost += cost * 0.2
diff = abs(budget - cost)
if budget >= cost:
    print(f'Hey, you have a great garden with {flower_amount} {type_flowers} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
