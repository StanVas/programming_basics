load_count = int(input())
total_price = 0
bus = 0
truck = 0
train = 0
total_weight = 0
for load in range(load_count):
    weight = int(input())
    total_weight += weight
    if weight < 4:
        total_price += weight * 200
        bus += weight
    elif weight < 12:
        total_price += weight * 175
        truck += weight
    elif weight >= 12:
        total_price += weight * 120
        train += weight
print(f'{total_price / total_weight:.2f}')
print(f'{(bus / total_weight) * 100:.2f}%')
print(f'{(truck / total_weight) * 100:.2f}%')
print(f'{(train / total_weight) * 100:.2f}%')
