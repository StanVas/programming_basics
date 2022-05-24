heritage = float(input())
rip = int(input())
years_old = 17
for year in range(1800, rip + 1):
    years_old += 1
    if year % 2 == 0:
        heritage -= 12000
    elif year % 2 !=0:
        heritage -= 12000 + (years_old * 50)
if heritage < 0:
    print(f'He will need {abs(heritage):.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {heritage:.2f} dollars left.')
