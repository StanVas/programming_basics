company_name = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_ticket_price = float(input())
customer_service = float(input())

adult_tickets_profit = (adult_ticket_price + customer_service) * adult_tickets
child_tickets_profit = ((adult_ticket_price * 0.3) + customer_service) * child_tickets

total_profit = (adult_tickets_profit + child_tickets_profit) * 0.2

print(f'The profit of your agency from {company_name} tickets is {total_profit:.2f} lv.')
