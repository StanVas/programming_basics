goal = 10000
total_steps = 0
while goal > total_steps:
    command = input()
    if command == 'Going home':
        going_home_steps = int(input())
        total_steps += going_home_steps
        if total_steps >= goal:
            print('Goal reached! Good job!')
            print(f'{abs(total_steps - goal)} steps over the goal!')
        if total_steps < goal:
            print(f'{abs(total_steps - goal)} more steps to reach goal.')
        break
    else:
        total_steps += int(command)
        if total_steps >= goal:
            print('Goal reached! Good job!')
            print(f'{abs(total_steps - goal)} steps over the goal!')
            break
