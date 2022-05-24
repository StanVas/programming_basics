budget = float(input())
type_of_ticket = input()
number_of_people = int(input())
vip_ticket = 499.99
normal_ticket = 249.99
total_price_tickets = 0
diff = 0
if number_of_people <= 4:
    budget -= budget * 0.75
    if type_of_ticket == 'VIP':
        total_price_tickets = number_of_people * vip_ticket
    elif type_of_ticket == 'Normal':
        total_price_tickets = number_of_people * normal_ticket
elif number_of_people <= 9:
    budget -= budget * 0.60
    if type_of_ticket == 'VIP':
        total_price_tickets = number_of_people * vip_ticket
    elif type_of_ticket == 'Normal':
        total_price_tickets = number_of_people * normal_ticket
elif number_of_people <= 24:
    budget -= budget * 0.50
    if type_of_ticket == 'VIP':
        total_price_tickets = number_of_people * vip_ticket
    elif type_of_ticket == 'Normal':
        total_price_tickets = number_of_people * normal_ticket
elif number_of_people <= 49:
    budget -= budget * 0.40
    if type_of_ticket == 'VIP':
        total_price_tickets = number_of_people * vip_ticket
    elif type_of_ticket == 'Normal':
        total_price_tickets = number_of_people * normal_ticket
else:
    budget -= budget * 0.25
    if type_of_ticket == 'VIP':
        total_price_tickets = number_of_people * vip_ticket
    elif type_of_ticket == 'Normal':
        total_price_tickets = number_of_people * normal_ticket
diff = abs(budget - total_price_tickets)
if budget >= total_price_tickets:
    print(f"Yes! You have {diff:.2f} leva left.")
elif total_price_tickets > budget:
    print(f"Not enough money! You need {diff:.2f} leva.")
