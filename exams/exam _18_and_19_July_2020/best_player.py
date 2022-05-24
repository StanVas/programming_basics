best_player = ''
max_goals = 0

while True:
    player = input()
    if player == 'END':
        break
    else:
        goals = int(input())
        if goals > max_goals:
            best_player = player
            max_goals = goals
        if goals >= 10:
            break


print(f'{best_player} is the best player!')
if max_goals >= 3:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f"He has scored {max_goals} goals.")
