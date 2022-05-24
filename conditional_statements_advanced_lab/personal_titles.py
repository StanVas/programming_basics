age = float(input())
gender = input()
title = ''
if gender == 'm' and age >= 16:
    title = 'Mr.'
elif gender == 'm' and age < 16:
    title = 'Master'
elif gender == 'f' and age >= 16:
    title = 'Ms.'
elif gender == 'f' and age < 16:
    title = 'Miss'
print(f'{title}')
