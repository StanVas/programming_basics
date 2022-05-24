age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toys = 0
money_saved = 0
amount = 0

for num in range(1, age + 1):
    if num % 2 == 0:
        amount += 10
        money_saved += amount - 1
    else:
        toys += 1
money_from_toys = toys * toy_price
total_money = money_from_toys + money_saved
diff = abs(washing_machine_price - total_money)
if total_money >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
