num_pairs = int(input())
sum_numbers = 0
max_difference = 0
are_equal = False

for number in range(num_pairs):
    first_number = int(input())
    second_number = int(input())
    sum = first_number + second_number
    if number == 0:
        sum_numbers = sum
    if sum == sum_numbers:
        are_equal = True
    else:
        are_equal = False
        if number != 0:
            if sum > sum_numbers:
                difference = sum - sum_numbers
            else:
                difference = sum_numbers - sum
            if difference > max_difference:
                max_difference = difference
        sum_numbers = sum

if are_equal:
    print(f"Yes, value={sum_numbers}")
else:
    print(f"No, maxdiff={max_difference}")
