numbers = int(input())
even_sum = 0
odd_sum = 0
for num in range(numbers):
    current_num = int(input())

    if num % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num
if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')
