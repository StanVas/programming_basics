bought_chrysanthemums = int(input())        # хризантеми
bought_roses = int(input())
bought_tulips = int(input())          # лалета
season = input()
holiday_or_not = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
discount = 0
total_flowers = bought_chrysanthemums + bought_roses + bought_tulips
if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
total_price = (chrysanthemums_price * bought_chrysanthemums) + (roses_price * bought_roses)\
              + (tulips_price * bought_tulips)
if holiday_or_not == 'Y':
    total_price += total_price * 0.15
if season == "Spring" and bought_tulips > 7:
    total_price -= total_price * 0.05
if season == "Winter" and bought_roses >= 10:
    total_price -= total_price * 0.1
if total_flowers > 20:
    total_price -= total_price * 0.2
print(f'{(total_price + 2):.2f}')
