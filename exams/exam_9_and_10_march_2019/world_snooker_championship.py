stage = input()
type_of_ticket = input()
number_of_tickets = int(input())
picture_with_trophy = input()
price = 0
picture_price = 0
if type_of_ticket == 'Standard':
    if stage == 'Quarter final':
        price = 55.5 * number_of_tickets
    elif stage == 'Semi final':
        price = 75.88 * number_of_tickets
    elif stage == 'Final':
        price = 110.10 * number_of_tickets
elif type_of_ticket == 'Premium':
    if stage == 'Quarter final':
        price = 105.20 * number_of_tickets
    elif stage == 'Semi final':
        price = 125.22 * number_of_tickets
    elif stage == 'Final':
        price = 160.66 * number_of_tickets
elif type_of_ticket == 'VIP':
    if stage == 'Quarter final':
        price = 118.90 * number_of_tickets
    elif stage == 'Semi final':
        price = 300.40 * number_of_tickets
    elif stage == 'Final':
        price = 400 * number_of_tickets
if picture_with_trophy == 'Y':
    picture_price = number_of_tickets * 40
if price < 2500:
    price += picture_price
elif 2500 <= price <= 4000:
    price -= price * 0.1
    price += picture_price
elif price > 4000:
    price -= price * 0.25
    # if picture_with_trophy == 'Y':
    #     price -= price * 0.25
    #     picture_with_trophy = 0
    # elif picture_with_trophy == "N":
    #     price -= price * 0.25
print(f'{price:.2f}')
