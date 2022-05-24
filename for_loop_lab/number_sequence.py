import sys
numbers = int(input())
biggest_num = -sys.maxsize
smallest_num = sys.maxsize
for n in range(numbers):
    current_num = int(input())
    if current_num > biggest_num:
        biggest_num = current_num
    if current_num < smallest_num:
        smallest_num = current_num
print(f'Max number: {biggest_num}')
print(f'Min number: {smallest_num}')
