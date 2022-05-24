vacation_price = float(input())
saved_money = float(input())
spending_count = 0
days_count = 0
while True:
    command = input()
    money = float(input())
    if command == 'spend':
        spending_count += 1
        days_count += 1
        if spending_count == 5:
            print("You can't save the money.")
            print(f'{days_count}')
            break
        if saved_money < money:
            saved_money = 0
        else:
            saved_money -= money
    elif command == 'save':
        days_count += 1
        saved_money += money
    if vacation_price <= saved_money:
        print(f'You saved the money for {days_count} days.')
        break
