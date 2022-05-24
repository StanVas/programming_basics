import sys
num = input()
max_num = -sys.maxsize

while num == 'Stop':
    break
    current_num = int(num)

    if current_num > max_num:
        max_num = current_num

        num = input()
    # else:
    #     break
    print(max_num)
