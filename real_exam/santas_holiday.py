days = int(input()) - 1
type_of_room = input()
score = input()
price = 0
discount = 0
total_price = 0
if type_of_room == 'room for one person':
    total_price = days * 18

elif type_of_room == 'apartment':
    price = days * 25
    if days < 10:
        discount = price * 0.3
        total_price = price - discount
    elif 10 <= days <= 15:
        discount = price * 0.35
        total_price = price - discount
    elif days > 15:
        discount = price * 0.5
        total_price = price - discount

elif type_of_room == 'president apartment':
    price = days * 35
    if days < 10:
        discount = price * 0.1
        total_price = price - discount
    elif 10 <= days <= 15:
        discount = price * 0.15
        total_price = price - discount
    elif days > 15:
        discount = price * 0.2
        total_price = price - discount

if score == 'positive':
    total_price += total_price * 0.25
elif score == 'negative':
    total_price -= total_price * 0.1

print(f'{total_price:.2f}')
