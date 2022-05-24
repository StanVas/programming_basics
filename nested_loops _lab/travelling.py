command = input()

while command != 'End':
    destination = command
    needed_money = float(input())
    collected_money = 0
    while collected_money < needed_money:
        current_sum = float(input())
        collected_money += current_sum
    print(f'Going to {destination}!')
    command = input()
