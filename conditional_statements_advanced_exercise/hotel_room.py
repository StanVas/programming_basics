month = input()
sleepovers = int(input())
studio = 0
apartment = 0
if month == 'May' or month == 'October':
    studio = sleepovers * 50
    apartment = sleepovers * 65
    if 7 < sleepovers <= 14:
        studio -= studio * 0.05
    elif sleepovers > 14:
        studio -= studio * 0.3
        apartment -= apartment * 0.1
elif month == 'June' or month == 'September':
    studio = sleepovers * 75.2
    apartment = sleepovers * 68.7
    if sleepovers > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1
elif month == 'July' or month == 'August':
    studio = sleepovers * 76
    apartment = sleepovers * 77
    if sleepovers > 14:
        apartment -= apartment * 0.1

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')
