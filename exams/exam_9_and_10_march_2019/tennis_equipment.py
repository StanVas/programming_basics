from math import ceil, floor
tennis_rocket_price = int(input())
tennis_rockets = int(input())
pairs_of_trainers = int(input())

trainers_price = tennis_rocket_price / 6
total_trainers = trainers_price * pairs_of_trainers
total_tennis_rockets = tennis_rocket_price * tennis_rockets
other_equipment = (total_tennis_rockets + total_trainers) * 0.2

total_price = other_equipment + total_tennis_rockets + total_trainers

print(f'Price to be paid by Djokovic {int(total_price/8)}')
print(f'Price to be paid by sponsors {ceil((total_price-(total_price/8)))}')
