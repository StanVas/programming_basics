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
        if type_color == 'touch up':
            profit += 20
        elif type_color == 'full color':
            profit += 30
diff = abs(day_target - profit)
if profit >= day_target:
    print("You have reached your target for the day!")
elif profit < day_target:
    print(f"Target not reached! You need {diff}lv. more.")

print(f'Earned money: {profit}lv.')
