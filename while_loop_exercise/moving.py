wight = int(input())
length = int(input())
height = int(input())
command = input()
free_space = wight * length * height
while free_space > 0:
    if command == 'Done':
        print(f'{free_space} Cubic meters left.')
        break
    else:
        free_space -= int(command)
        if free_space < 0:
            print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
            break
    command = input()
