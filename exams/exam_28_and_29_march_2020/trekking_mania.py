groups_count = int(input())
top_musala = 0
top_monblan = 0
top_kilimadjaro = 0
top_k2 = 0
top_everest = 0
total_people = 0
for group in range(groups_count):
    people_count = int(input())
    total_people += people_count
    if people_count < 6:
        top_musala += people_count
    elif people_count < 13:
        top_monblan += people_count
    elif people_count < 26:
        top_kilimadjaro += people_count
    elif people_count < 41:
        top_k2 += people_count
    elif people_count >= 41:
        top_everest += people_count

percent_top_musala = (top_musala / total_people) * 100
percent_top_monblan = (top_monblan / total_people) * 100
percent_top_kilimandjaro = (top_kilimadjaro / total_people) * 100
percent_top_k2 = (top_k2 / total_people) * 100
percent_top_everest = (top_everest / total_people) * 100
print(f'{percent_top_musala:.2f}%')
print(f'{percent_top_monblan:.2f}%')
print(f'{percent_top_kilimandjaro:.2f}%')
print(f'{percent_top_k2:.2f}%')
print(f'{percent_top_everest:.2f}%')
