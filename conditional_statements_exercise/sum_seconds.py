time_first = int(input())
time_second = int(input())
time_third = int(input())
time_sum = time_first + time_second + time_third
time_min = time_sum // 60
time_sec = time_sum % 60
if time_sec <= 9:
    print(f'{time_min}:{time_sec:02d}')
else:
    print(f'{time_min}:{time_sec}')
