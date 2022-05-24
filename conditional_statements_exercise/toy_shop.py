price_vacation = float(input())
quantity_puzzles = int(input())
quantity_talking_dolls = int(input())
quantity_teddy_bear = int(input())
quantity_minions = int(input())
quantity_trucks = int(input())
total_quantity = quantity_puzzles + quantity_talking_dolls\
                 + quantity_teddy_bear + quantity_minions + quantity_trucks
total_price = (quantity_puzzles * 2.6) + (quantity_talking_dolls * 3)\
              + (quantity_teddy_bear * 4.1) + (quantity_minions * 8.2) + (quantity_trucks * 2)
if total_quantity >= 50:
    total_price -= total_price * 0.25
rent = total_price * 0.1
final_price = total_price - rent
diff = abs(final_price - price_vacation)
if final_price >= price_vacation:
    print(f"Yes! {diff:.2f} lv left.")
elif final_price < price_vacation:
    print(f"Not enough money! {diff:.2f} lv needed.")
