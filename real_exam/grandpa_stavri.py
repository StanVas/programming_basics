rakia_days = int(input())
total_amount = 0
average_degrees = 0
for rakia in range(rakia_days):
    amount_of_rakia = float(input())
    rakia_degrees = float(input())
    total_amount += amount_of_rakia
    average_degrees += amount_of_rakia * rakia_degrees

average_degrees = average_degrees / total_amount
print(f'Liter: {total_amount:.2f}')
print(f'Degrees: {average_degrees:.2f}')
if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees <= 42:
    print("Super!")
elif average_degrees > 42:
    print("Dilution with distilled water!")
