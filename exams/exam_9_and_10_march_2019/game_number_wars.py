player_one = input()
player_two = input()
player_one_score = 0
player_two_score = 0
flag = False

while True:
    command = input()
    if command == 'End of game':
        print(f'{player_one} has {player_one_score} points')
        print(f'{player_two} has {player_two_score} points')
        break
    command2 = input()

    if command != 'End of game':
        command2 = int(command2)
        command = int(command)
        if command > command2:
            player_one_score += command - command2
        elif command < command2:
            player_two_score += command2 - command
        elif command == command2:
            first = int(input())
            second = int(input())
            flag = True
            if first > second:
                print('Number wars!')
                print(f'{player_one} is winner with {player_one_score} points')
            elif second > first:
                print('Number wars!')
                print(f'{player_two} is winner with {player_two_score} points')
            if flag:
                break
