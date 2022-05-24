needed_money = float(input())
owned_money = float(input())
spending_count = 0
days_count = 0
while owned_money < needed_money and spending_count < 5:
    command = input()
    money = float(input())
    days_count += 1
    if command == 'save':
        spending_count = 0
        owned_money += money
    elif command == 'spend':
        owned_money -= money
        spending_count += 1
        if owned_money < 0:
            owned_money = 0
if spending_count == 5:
    print("You can't save the money.")
    print(f'{days_count}')
if owned_money >= needed_money:
    print(f'You saved the money for {days_count} days.')
