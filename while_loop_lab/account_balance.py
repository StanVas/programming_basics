total = 0

while True:
    current_sum = input()

    if current_sum == 'NoMoreMoney':
        break

    if float(current_sum) < 0:
        print('Invalid operation!')
        break

    total += float(current_sum)
    print(f'Increase: {float(current_sum):.2f}')

print(f'Total: {total:.2f}')
