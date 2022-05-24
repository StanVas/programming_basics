fuel_type = input()
amount_of_fuel = int(input())
fuel = ''
if fuel_type == 'Diesel':
    fuel = 'diesel'
elif fuel_type == 'Gasoline':
    fuel = 'gasoline'
elif fuel_type == 'Gas':
    fuel = 'gas'
else:
    print('Invalid fuel!')
if amount_of_fuel >= 25 and fuel_type == 'Diesel':
    print(f'You have enough {fuel}.')
elif amount_of_fuel >= 25 and fuel_type == 'Gasoline':
    print(f'You have enough {fuel}.')
elif amount_of_fuel >= 25 and fuel_type == 'Gas':
    print(f'You have enough {fuel}.')
elif amount_of_fuel < 25 and fuel_type == 'Diesel':
    print(f'Fill your tank with {fuel}!')
elif amount_of_fuel < 25 and fuel_type == 'Gasoline':
    print(f'Fill your tank with {fuel}!')
elif amount_of_fuel < 25 and fuel_type == 'Gas':
    print(f'Fill your tank with {fuel}!')
