budget = float(input())
number_of_extras = int(input())
price_clothes_for_one_extra = float(input())
decor = budget * 0.1
if number_of_extras > 150:
    price_clothes_for_one_extra -= price_clothes_for_one_extra * 0.1
total_price_clothes = number_of_extras * price_clothes_for_one_extra
final_budget = total_price_clothes + decor
diff = abs(budget - final_budget)
if budget >= final_budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
