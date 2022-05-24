free_days = int(input())

working_days = 365 - free_days
working_days_time = working_days * 63
free_days_time = free_days * 127
total_time = working_days_time + free_days_time
diff = abs(30000 - total_time)
hours = diff // 60
minutes = diff % 60
if total_time <= 30000:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
