tournaments = int(input())
starting_points = int(input())
current_points = 0
win_rate = 0
for position in range(tournaments):
    tournament_stage = input()
    if tournament_stage == 'W':
        current_points += 2000
        win_rate += 1
    elif tournament_stage == 'F':
        current_points += 1200
    elif tournament_stage == 'SF':
        current_points += 720
final_points = starting_points + current_points
average_points = current_points / tournaments
win_rate_percent = (win_rate / tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {int(average_points)}')
print(f'{win_rate_percent:.2f}%')
