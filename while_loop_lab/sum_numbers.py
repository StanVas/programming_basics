first_num = int(input())
total_sum = 0

while True:
    current_num = int(input())
    total_sum += current_num

    if total_sum >= first_num:
        print(total_sum)
        break
