visitors = int(input())
work_out = 0
buy_protein = 0
back = 0
chest = 0
legs = 0
work_out_abs = 0
protein_shake = 0
protein_bar = 0

for person in range(visitors):
    command = input()
    if command == 'Back' or command == 'Chest' or command == 'Legs' or command == 'Abs':
        work_out += 1
        if command == "Back":
            back += 1
        elif command == 'Chest':
            chest += 1
        elif command == 'Legs':
            legs += 1
        elif command == "Abs":
            work_out_abs += 1
    elif command == 'Protein shake' or command == 'Protein bar':
        buy_protein += 1
        if command == 'Protein shake':
            protein_shake +=1
        elif command == 'Protein bar':
            protein_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{work_out_abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f'{(work_out/visitors)*100:.2f}% - work out')
print(f'{(buy_protein/visitors)*100:.2f}% - protein')
