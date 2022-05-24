months = int(input())
electricity = 0
water = 0
internet = 0
others = 0

for _ in range(months):
    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15
    others += (20 + 15 + electricity_bill) + ((20 + 15 + electricity_bill) * 0.2)
all_bills = (electricity + water + internet + others) / months

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {all_bills:.2f} lv')
