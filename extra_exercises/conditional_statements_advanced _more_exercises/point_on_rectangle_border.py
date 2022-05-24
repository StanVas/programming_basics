x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x1 < x < x2 and y1 < y < y2:
    print('Inside / Outside')
elif x1 <= x <= x2 or y1 <= y <= y2:
    print('Border')
