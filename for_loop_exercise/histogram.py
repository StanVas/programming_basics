numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for n in range(numbers):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num < 400:
        p2 += 1
    elif current_num < 600:
        p3 += 1
    elif current_num < 800:
        p4 += 1
    elif current_num >= 800:
        p5 += 1
p1_percent = (p1 / numbers) * 100
p2_percent = (p2 / numbers) * 100
p3_percent = (p3 / numbers) * 100
p4_percent = (p4 / numbers) * 100
p5_percent = (p5 / numbers) * 100
print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')
