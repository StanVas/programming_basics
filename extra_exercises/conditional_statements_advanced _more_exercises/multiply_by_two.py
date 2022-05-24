number = float(input())
while True:
    if number < 0:
        print('Negative number!')
        break
    else:
        print(f'Result: {number * 2:.2f}')
        number = float(input())
