from math import floor
needed_hours = int(input())
days = int(input())
workers = int(input())
training = days * 0.1
working_hours = floor((days - training) * 8)
overtime = workers * (2 * days)
total_hours = working_hours + overtime
diff = abs(needed_hours - total_hours)
if total_hours >= needed_hours:
    print(f'Yes!{diff} hours left.')
else:
    print(f'Not enough time!{diff} hours needed.')
