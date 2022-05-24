player = input()
points = 301
successful_shots = 0
unsuccessful_shots = 0
while True:
    command = input()
    if points == 0:
        print(f'{player} won the leg with {successful_shots} shots.')
        break
    if command == 'Retire':
        print(f'{player} retired after {unsuccessful_shots} unsuccessful shots.')
        break
    current_points = int(input())
    if points > current_points:
        points -= current_points
        successful_shots += 1
    elif points < current_points and points != 0:
        unsuccessful_shots += 1
