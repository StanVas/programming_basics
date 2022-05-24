food = int(input())
total_food = food * 1000
consumed_food = 0
flag = False

while True:
    command = input()

    if command == "Adopted":
        flag = True
        break
    elif command != 'Adopted':
        command = int(command)

    consumed_food += command

diff = abs(total_food - consumed_food)

if flag:
    if consumed_food > total_food:
        print(f'Food is not enough. You need {diff} grams more.')
    elif consumed_food <= total_food:
        print(f'Food is enough! Leftovers: {diff} grams.')
