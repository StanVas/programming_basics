budget = float(input())
graphic_card_quantity = int(input())
processor_quantity = int(input())
ram_quantity = int(input())
graphic_card_price = 250
graphic_card_total_price = graphic_card_quantity * graphic_card_price
processor_price = graphic_card_total_price * 0.35
ram_price = graphic_card_total_price * 0.1
processor_total_price = processor_quantity * processor_price
ram_total_price = ram_quantity * ram_price
total_price = processor_total_price + ram_total_price + graphic_card_total_price
if graphic_card_quantity > processor_quantity:
    total_price -= total_price * 0.15
diff = abs(budget - total_price)
if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
