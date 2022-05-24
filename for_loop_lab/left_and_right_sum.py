numbers = int(input())
diff = 0
left_sum = 0
right_sum = 0
for num in range(numbers * 2):
    current_num = int(input())

    if num < numbers:
        left_sum += current_num
    else:
        right_sum += current_num

if left_sum == right_sum and numbers != 0:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
