cake_length = int(input())
cake_wight = int(input())
cake_size = cake_length * cake_wight
pieces_cake = 0

while cake_size > 0:
    command = input()
    if command == "STOP":
        print(f'{abs(cake_size)} pieces are left.')
        break
    elif cake_size > 0:
        cake_size -= int(command)
if cake_size < 0:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')
