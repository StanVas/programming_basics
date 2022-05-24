fruit = input()
set_pcs = input()
ordered_sets = int(input())
price = 0
if fruit == 'Watermelon':
    if set_pcs == 'small':
        price = ordered_sets * 56 * 2
    elif set_pcs == 'big':
        price = ordered_sets * 28.70 * 5
elif fruit == 'Mango':
    if set_pcs == 'small':
        price = ordered_sets * 36.66 * 2
    elif set_pcs == 'big':
        price = ordered_sets * 19.60 * 5
elif fruit == 'Pineapple':
    if set_pcs == 'small':
        price = ordered_sets * 42.10 * 2
    elif set_pcs == 'big':
        price = ordered_sets * 24.80 * 5
elif fruit == 'Raspberry':
    if set_pcs == 'small':
        price = ordered_sets * 20 * 2
    elif set_pcs == 'big':
        price = ordered_sets * 15.20 * 5
if price > 1000:
    price /= 2
elif 400 < price <= 1000:
    price -= price * 0.15
print(f'{price:.2f} lv.')
