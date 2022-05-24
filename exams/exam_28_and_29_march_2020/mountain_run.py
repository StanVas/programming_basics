record_sec = float(input())
distance_in_meters = float(input())
climbing_speed_sec = float(input())

total_sec = climbing_speed_sec * distance_in_meters
delay = int(distance_in_meters / 50)
total_delay = delay * 30
total = total_sec + total_delay
diff = abs(total - record_sec)
if total < record_sec:
    print(f'Yes! The new record is {total:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')
