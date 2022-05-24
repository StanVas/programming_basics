days = int(input())
place_to_stay = input()
score = input()
price_per_night = 0
total_price = 0
if place_to_stay == 'room for one person':
    price_per_night = 18
    total_price = (days - 1) * price_per_night
elif place_to_stay == 'apartment':
    price_per_night = 25
elif place_to_stay == 'president apartment':
    price_per_night = 35
total_price = (days - 1) * price_per_night
if days < 10:
    if place_to_stay == 'apartment':
        total_price -= total_price * 0.3
    elif place_to_stay == 'president apartment':
        total_price -= total_price * 0.1
elif days <= 15:
    if place_to_stay == 'apartment':
        total_price -= total_price * 0.35
    elif place_to_stay == 'president apartment':
        total_price -= total_price * 0.15
elif days > 15:
    if place_to_stay == 'apartment':
        total_price -= total_price * 0.5
    elif place_to_stay == 'president apartment':
        total_price -= total_price * 0.2
if score == 'positive':
    total_price += total_price * 0.25
elif score == 'negative':
    total_price -= total_price * 0.1
print(f'{total_price:.2f}')
