budget = float(input())
season = input()
destination = ''
place_to_stay = ''
price = 0
if budget <= 1000:
    place_to_stay = 'Camp'
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        destination = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    place_to_stay = 'Hut'
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        destination = 'Morocco'
        price = budget * 0.6
elif budget > 3000:
    place_to_stay = 'Hotel'
    if season == "Summer":
        destination = "Alaska"
    elif season == "Winter":
        destination = 'Morocco'
    price = budget * 0.9
print(f'{destination} - {place_to_stay} - {price:.2f}')
