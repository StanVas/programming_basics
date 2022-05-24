season = input()
group = input()
number_of_students = int(input())
sleepovers = int((input()))
price = 0
sport = ''
if season == "Winter":
    if group == "boys":
        price = 9.6
        sport = 'Judo'
    elif group == "girls":
        price = 9.6
        sport = 'Gymnastics'
    elif group == 'mixed':
        price = 10
        sport = "Ski"
elif season == 'Spring':
    if group == "boys":
        price = 7.2
        sport = 'Tennis'
    elif group == "girls":
        price = 7.2
        sport = 'Athletics'
    elif group == 'mixed':
        price = 9.5
        sport = "Cycling"
elif season == 'Summer':
    if group == "boys":
        price = 15
        sport = 'Football'
    elif group == "girls":
        price = 15
        sport = 'Volleyball'
    elif group == 'mixed':
        price = 20
        sport = "Swimming"
total_price = (number_of_students * price) * sleepovers
if 10 <= number_of_students < 20:
    total_price -= total_price * 0.05
elif 20 <= number_of_students < 50:
    total_price -= total_price * 0.15
elif number_of_students >= 50:
    total_price -= total_price * 0.5
print(f'{sport} {total_price:.2f} lv.')
