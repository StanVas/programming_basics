import sys
numbers = int(input())
max_num = -sys.maxsize
total = 0
for n in range(numbers):
    current_num = int(input())
    total += current_num
    if current_num > max_num:
        max_num = current_num

if (total - max_num) == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = max_num - (total - max_num)
    print('No')
    print(f'Diff = {abs(diff)}')
