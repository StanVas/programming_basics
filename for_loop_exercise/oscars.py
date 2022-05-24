actor = input()
academy_points = float(input())
judges = int(input())
current_points = 0
total_points = 0
for judge in range(judges):
    name = input()
    points = float(input())
    current_points += (len(name) * points) / 2
    total_points = academy_points + current_points
    if total_points >= 1250.5:
        break
if total_points >= 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = abs(total_points - 1250.5)
    print(f'Sorry, {actor} you need {diff:.1f} more!')
