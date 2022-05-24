n = int(input())
a1 = 0
b1 = 0
c1 = 0
d1 = 0
flag = False
for a in range(1, 10):
    if flag:
        break
    for b in range(9, a - 1, -1):
        if flag:
            break
        for c in range(0, 10):
            if flag:
                break
            for d in range(9, c - 1, - 1):
                if flag:
                    break
                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    a1 = a
                    b1 = b
                    c1 = c
                    d1 = d
                    print(f'{a1}{b1}{c1}{d1}')
                    flag = True
                    break
                elif int((a * b * c * d) / (a + b + c + d)) == 3 and n % 3 == 0:
                    a1 = a
                    b1 = b
                    c1 = c
                    d1 = d
                    print(f'{d1}{c1}{b1}{a1}')
                    flag = True
                    break
                elif a == 9 and b == 9 and c == 0 and d == 0:
                    print('Nothing found')
                    break
