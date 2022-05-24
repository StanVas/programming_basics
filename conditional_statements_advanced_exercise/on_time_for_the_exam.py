hour_exam = int(input())
min_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())
sum_min_exam = (hour_exam * 60) + min_exam
sum_min_arrival = (hour_arrival * 60) + min_arrival
diff = abs(sum_min_exam - sum_min_arrival)
hour = 0
minutes = 0
if sum_min_arrival == sum_min_exam:
    print('On time')
elif sum_min_arrival < sum_min_exam and diff <= 30:
    print('On time')
    print(f'{diff} minutes before the start')
elif sum_min_arrival > sum_min_exam:
    print('Late')
    if diff <= 59:
        print(f'{diff} minutes after the start')
    elif diff > 59:
        hour = diff // 60
        minutes = diff % 60
        print(f'{hour}:{minutes:02d} hours after the start')
elif sum_min_exam > sum_min_arrival and diff > 30:
    print('Early')
    if diff <= 59:
        print(f'{diff} minutes before the start')
    elif diff > 59:
        hour = diff // 60
        minutes = diff % 60
        print(f'{hour}:{minutes:02d} hours before the start')
