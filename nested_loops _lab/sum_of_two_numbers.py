start_num = int(input())
end_num = int(input())
magical_num = int(input())
combination_counter = 0
condition = False
for num1 in range(start_num, end_num + 1):
    for num2 in range(start_num, end_num + 1):
        combination_counter += 1
        if num1 + num2 == magical_num:
            print(f"Combination N:{combination_counter} ({num1} + {num2} = {magical_num})")
            condition = True

    if condition:
        break

if not condition:
    print(f"{combination_counter} combinations - neither equals {magical_num}")
