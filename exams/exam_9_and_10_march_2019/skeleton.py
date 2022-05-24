minutes = int(input())
seconds = int(input())
distance = float(input())
sec_for_hundred_meters = int(input())
total_time = (minutes * 60) + seconds
delay = (distance/120) * 2.5
his_time = ((distance / 100) * sec_for_hundred_meters) - delay
diff = abs(his_time - total_time)
if his_time <= total_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f'His time is {his_time:.3f}.')
else:
    print(f'No, Marin failed! He was {diff:.3f} second slower.')
