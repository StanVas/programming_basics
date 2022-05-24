hour = int(input())
minutes = int(input())
sum_min = (hour * 60) + minutes + 15
hour_result = sum_min // 60
minutes_result = sum_min % 60
if hour_result > 23:
    hour_result = 0
print(f'{hour_result}:{minutes_result:02d}')
