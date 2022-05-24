budget = int(input())
season = input()
number_of_fisherman = int(input())
ship_price = 0
if season == 'Spring':
    ship_price = 3000
elif season == 'Summer' or season == 'Autumn':
    ship_price = 4200
elif season == 'Winter':
    ship_price = 2600
if number_of_fisherman <= 6:
    ship_price -= ship_price * 0.1
elif number_of_fisherman <= 11:
    ship_price -= ship_price * 0.15
elif number_of_fisherman >= 12:
    ship_price -= ship_price * 0.25
if number_of_fisherman % 2 == 0 and season != 'Autumn':
    ship_price -= ship_price * 0.05
diff = abs(budget - ship_price)

if budget >= ship_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
