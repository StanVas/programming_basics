command = input()
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0
while command != "Finish":
    free_seats = int(input())
    tickets_sold = 0
    while tickets_sold <= free_seats:
        ticket = input()
        if free_seats == tickets_sold or ticket == 'End':
            print(f'{command} - {(tickets_sold / free_seats) * 100:.2f}% full.')
            tickets_sold = 0
            break
        else:
            tickets_sold += 1
            total_tickets += 1
        if ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'kid':
            kids_tickets += 1
        command = input()
if command == 'Finish':
    print(f'Total tickets: {total_tickets}')
    print(f'{(student_tickets / total_tickets) * 100:.2f}% student tickets.')
    print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
    print(f'{(kids_tickets / total_tickets) * 100:.2f}% kids tickets.')
