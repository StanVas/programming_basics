truck_capacity = float(input())
baggage_counter = 0
flag = False
statistic = 0
total_baggage = 0

while True:
    command = input()
    if command == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        flag = True
        break
    elif command != 'End':
        command = float(command)
        baggage_counter += 1
        statistic += 1

        if baggage_counter % 3 == 0:
            command += command * 0.1

        total_baggage += command
    if truck_capacity < total_baggage:
        flag = True
        statistic -= 1
        print("No more space!")
        break

if flag:
    print(f'Statistic: {statistic} suitcases loaded.')
