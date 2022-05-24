joinery_count = int(input())
type_of_joinery = input()
delivery = input()
price = 0

if type_of_joinery == '90X130':
    price = 110
    if 30 < joinery_count < 60:
        price -= price * 0.05
    elif joinery_count > 60:
        price -= price * 0.08
elif type_of_joinery == '100X150':
    price = 140
    if 40 < joinery_count < 80:
        price -= price * 0.06
    elif joinery_count > 80:
        price -= price * 0.1
elif type_of_joinery == '130X180':
    price = 190
    if 20 < joinery_count < 50:
        price -= price * 0.07
    elif joinery_count > 50:
        price -= price * 0.12
elif type_of_joinery == '200X300':
    price = 250
    if 25 < joinery_count < 50:
        price -= price * 0.09
    elif joinery_count > 50:
        price -= price * 0.14

price = price * joinery_count

if delivery == 'With delivery':
    price += 60
if joinery_count > 99:
    price -= price * 0.04
if joinery_count < 10:
    print("Invalid order")
else:
    print(f'{price:.2f} BGN')
