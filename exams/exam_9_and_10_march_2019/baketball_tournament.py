tournament = input()
total_games = 0
win = 0
lost = 0
while tournament != "End of tournaments":
    number_of_games = int(input())
    for game in range(1, number_of_games + 1):
        total_games += 1
        home_team = int(input())
        away_team = int(input())
        diff = abs(home_team - away_team)
        if home_team > away_team:
            win += 1
            print(f'Game {game} of tournament {tournament}: win with {diff} points.')
        else:
            lost += 1
            print(f'Game {game} of tournament {tournament}: lost with {diff} points.')
    tournament = input()

print(f'{(win/total_games)*100:.2f}% matches win')
print(f'{(lost/total_games)*100:.2f}% matches lost')
