n = int(input())
condition = False
current = 1
for row in range(1, n + 1):
    for col in range(1, row + 1):

        if current > n:
            condition = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if condition:
        break
    print()
