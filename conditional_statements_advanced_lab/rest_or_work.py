day_of_week = input()
# in за съвпадения в текста, което може да е само сричка или буква
if day_of_week in 'Monday Tuesday Wednesday Thursday Friday':
    print('Working day')
elif day_of_week in 'Saturday Sunday':
    print('Weekend')
else:
    print('Error')
