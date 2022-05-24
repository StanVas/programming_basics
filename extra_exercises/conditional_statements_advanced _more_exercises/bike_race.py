juniors = int(input())
seniors = int(input())
track = input()
juniors_and_seniors_sum = juniors + seniors
total_money = 0
juniors_tax = 0
seniors_tax = 0
if track == 'trail':
    juniors_tax = 5.5
    seniors_tax = 7
elif track == 'cross-country':
    juniors_tax = 8
    seniors_tax = 9.5
    if juniors_and_seniors_sum >= 50:
        juniors_tax -= juniors_tax * 0.25
        seniors_tax -= seniors_tax * 0.25
elif track == 'downhill':
    juniors_tax = 12.25
    seniors_tax = 13.75
elif track == 'road':
    juniors_tax = 20
    seniors_tax = 21.5
total_money = (juniors_tax * juniors) + (seniors_tax * seniors)
expenses = total_money * 0.05
final_money = total_money - expenses
print(f'{final_money:.2f}')
