day_target = int(input())
profit = 0

while profit < day_target:
    if profit >= day_target:
        break
    service = input()
    if service == 'closed':
        break
    if service == 'haircut':
        type_haircut = input()
        if type_haircut == 'mens':
            profit += 15
        elif type_haircut == 'ladies':
            profit += 20
        elif type_haircut == 'kids':
            profit += 10
    elif service == 'color':
        type_color = input()
        if type_color == 'touch':
            profit += 20
        elif type_color == 'full':
            profit += 30
        type_color2 = input()
        if type_color2 == 'up':
            pass
        elif type_color2 == 'color':
            pass

diff = abs(day_target - profit)
if profit >= day_target:
    print("You have reached your target for the day!")
elif profit < day_target:
    print(f"Target not reached! You need {diff}lv. more.")

print(f'Earned money: {profit}lv.')
