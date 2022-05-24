wanted_result = int(input())
current_result = 0
current_high = wanted_result - 30
total_jumps = 0
flag = False
while True:
    if current_high > wanted_result:
        print(f"Tihomir succeeded, he jumped "
              f"over {wanted_result}cm after {total_jumps} jumps.")
        break

    current_result = int(input())
    unsuccessful_jumps_count = 0

    if current_result > current_high:
        total_jumps += 1
        current_high += 5
    elif current_result <= current_high:
        total_jumps += 1
        unsuccessful_jumps_count += 1
        for _ in range(1, 3):
            again = int(input())
            if again <= current_high:
                unsuccessful_jumps_count += 1
                total_jumps += 1
                if unsuccessful_jumps_count == 3:
                    flag = True
                    print(f'Tihomir failed at {current_high}cm '
                          f'after {total_jumps} jumps.')
                    break

            elif again > current_high:
                total_jumps += 1
                unsuccessful_jumps_count = 0
                current_high += 5

    if flag:
        break
