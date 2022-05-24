type_of_fuel = input()
amount_of_fuel = float(input())
discount_card = input()
discount_gasoline = 0
discount_diesel = 0
discount_gas = 0
fuel_price = 0
if discount_card == 'Yes':
    discount_gasoline = amount_of_fuel * 0.18
    discount_diesel = amount_of_fuel * 0.12
    discount_gas = amount_of_fuel * 0.08
if type_of_fuel == 'Gasoline':
    fuel_price = (amount_of_fuel * 2.22) - discount_gasoline
elif type_of_fuel == "Diesel":
    fuel_price = (amount_of_fuel * 2.33) - discount_diesel
elif type_of_fuel == "Gas":
    fuel_price = (amount_of_fuel * 0.93) - discount_gas
if 20 <= amount_of_fuel <= 25:
    fuel_price -= fuel_price * 0.08
elif amount_of_fuel > 25:
    fuel_price -= fuel_price * 0.1
print(f"{fuel_price:.2f} lv.")
