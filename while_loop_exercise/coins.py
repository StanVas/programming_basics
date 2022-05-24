current_sum = int(float(input()) * 100)
number_of_coins = 0

while current_sum > 0:
    if current_sum >= 200:
        current_sum -= 200
    elif current_sum >= 100:
        current_sum -= 100
    elif current_sum >= 50:
        current_sum -= 50
    elif current_sum >= 20:
        current_sum -= 20
    elif current_sum >= 10:
        current_sum -= 10
    elif current_sum >= 5:
        current_sum -= 5
    elif current_sum >= 2:
        current_sum -= 2
    elif current_sum >= 1:
        current_sum -= 1
    number_of_coins += 1

print(number_of_coins)
