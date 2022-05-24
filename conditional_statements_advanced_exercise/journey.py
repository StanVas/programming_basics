budget = float(input())
season = input()
place_to_stay = ''
price = 0
destination = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place_to_stay = 'Camp'
        price = budget * 0.3
    elif season == 'winter':
        place_to_stay = 'Hotel'
        price = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place_to_stay = 'Camp'
        price = budget * 0.4
    elif season == 'winter':
        place_to_stay = 'Hotel'
        price = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    place_to_stay = 'Hotel'
    price = budget * 0.9
print(f'Somewhere in {destination}')
print(f'{place_to_stay} - {price:.2f}')
