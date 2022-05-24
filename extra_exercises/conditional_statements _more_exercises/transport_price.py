distance = int(input())
time_of_the_day = input()
taxi_price = 0
bus_price = 0
train_price = 0
transport = ''
total_price = 0
if time_of_the_day == "day":
    taxi_price = 0.79
    bus_price = 0.09
    train_price = 0.06
elif time_of_the_day == 'night':
    taxi_price = 0.90
    bus_price = 0.09
    train_price = 0.06
if distance < 20:
    # transport = "taxi"
    total_price = (distance * taxi_price) + 0.70
elif 20 <= distance < 100:
    # transport = 'bus'
    total_price = distance * bus_price
elif distance >= 100:
    # transport = 'train'
    total_price = distance * train_price
print(f'{total_price:.2f}')
