floors = int(input())
apartments = int(input())

flat_number = 0
flat_name = ''
for floor in range(floors, 0, -1):
    for apartment in range(apartments):
        flat_number = floor * 10 + apartment

        if floor == floors:
            flat_name = f'L{flat_number} '
        elif floor % 2 != 0:
            flat_name = f'A{flat_number} '
        elif floor % 2 == 0:
            flat_name = f'O{flat_number} '

        print(flat_name, end='')

    print()
