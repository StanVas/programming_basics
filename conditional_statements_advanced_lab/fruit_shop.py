fruit = input()
day = input()
quantity = float(input())
price = 0
fruit_is_valid = True
fruit_price = 0
day_is_valid = True
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday'\
        or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        fruit_price = 2.5
    elif fruit == 'apple':
        fruit_price = 1.2
    elif fruit == 'orange':
        fruit_price = 0.85
    elif fruit == 'grapefruit':
        fruit_price = 1.45
    elif fruit == 'kiwi':
        fruit_price = 2.7
    elif fruit == 'pineapple':
        fruit_price = 5.5
    elif fruit == 'grapes':
        fruit_price = 3.85
    else:
        fruit_is_valid = False
elif day == "Saturday" or day == "Sunday":
    if fruit == 'banana':
        fruit_price = 2.7
    elif fruit == 'apple':
        fruit_price = 1.25
    elif fruit == 'orange':
        fruit_price = 0.9
    elif fruit == 'grapefruit':
        fruit_price = 1.60
    elif fruit == 'kiwi':
        fruit_price = 3
    elif fruit == 'pineapple':
        fruit_price = 5.6
    elif fruit == 'grapes':
        fruit_price = 4.2
    else:
        fruit_is_valid = False
else:
    day_is_valid = False
if not fruit_is_valid or not day_is_valid:
    print('error')
else:
    price = fruit_price * quantity
    print(f'{price:.2f}')
