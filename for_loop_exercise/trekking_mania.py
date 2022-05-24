groups = int(input())
mussala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_people = 0
for people in range(groups):
    number_of_people = int(input())
    total_people += number_of_people
    if number_of_people <= 5:
        mussala += number_of_people
    elif number_of_people <= 12:
        monblan += number_of_people
    elif number_of_people <= 25:
        kilimandjaro += number_of_people
    elif number_of_people <= 40:
        k2 += number_of_people
    elif number_of_people > 40:
        everest += number_of_people
percent_mussala = (mussala / total_people) * 100
percent_monblan = (monblan / total_people) * 100
percent_kilimandjaro = (kilimandjaro / total_people) * 100
percent_k2 = (k2 / total_people) * 100
percent_everest = (everest / total_people) * 100
print(f'{percent_mussala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimandjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
