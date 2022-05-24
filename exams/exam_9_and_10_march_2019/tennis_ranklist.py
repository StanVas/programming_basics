tournaments = int(input())
starting_points = int(input())

average_points = 0
won_tournaments = 0

for n in range(tournaments):
    stage = input()
    if stage == 'W':
        average_points += 2000
        won_tournaments += 1
    elif stage == 'F':
        average_points += 1200
    elif stage == 'SF':
        average_points += 720
print(f'Final points: {starting_points + average_points}')
print(f'Average points: {int(average_points / tournaments)}')
print(f'{(won_tournaments/tournaments)*100:.2f}%')
