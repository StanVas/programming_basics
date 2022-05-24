baggage_over_20_kg = float(input())
baggage_weight = float(input())
days_to_trip = int(input())
baggage_count = int(input())
baggage_price = 0
if baggage_weight < 10:
    baggage_price += baggage_over_20_kg * 0.2
elif 10 <= baggage_weight <= 20:
    baggage_price += baggage_over_20_kg * 0.5
elif baggage_weight > 20:
    baggage_price += baggage_over_20_kg
if days_to_trip > 30:
    baggage_price += baggage_price * 0.1
elif 7 <= days_to_trip <= 30:
    baggage_price += baggage_price * 0.15
elif days_to_trip < 7:
    baggage_price += baggage_price * 0.4
total_price = baggage_price * baggage_count
print(f'The total price of bags is: {total_price:.2f} lv.')
