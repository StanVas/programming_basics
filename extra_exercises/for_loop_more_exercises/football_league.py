capacity = int(input())
all_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for fan in range(all_fans):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v +=1
    elif sector == 'G':
        sector_g += 1
percent_a = (sector_a / all_fans) * 100
percent_b = (sector_b / all_fans) * 100
percent_v = (sector_v / all_fans) * 100
percent_g = (sector_g / all_fans) * 100
percent_fans = (all_fans / capacity) * 100
print(f'{percent_a:.2f}%')
print(f'{percent_b:.2f}%')
print(f'{percent_v:.2f}%')
print(f'{percent_g:.2f}%')
print(f'{percent_fans:.2f}%')
