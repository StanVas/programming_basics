tournament_days = int(input())
charity_money = 0
total_games_won = 0
total_games = 0

for day in range(tournament_days):
    while True:
        sport = input()
        won_games = 0
        total_games_today = 0
        money_today = 0

        if sport == 'Finish':
            if won_games > (total_games_today / 2):
                money_today += money_today * 0.1
            charity_money += money_today
            break
        else:
            result = input()
            total_games += 1
            total_games_today += 1
            if result == "win":
                money_today += 20
                total_games_won += 1
                won_games += 1
if total_games > (total_games / 2):
    charity_money += charity_money * 0.2
print(total_games_won)
print(total_games)
print(charity_money)
