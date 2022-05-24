turns = int(input())
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
final_score = 0
invalid_numbers = 0
for turn in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        final_score += number * 0.2
        from_0_to_9 += 1
    elif 10 <= number <= 19:
        final_score += number * 0.3
        from_10_to_19 += 1
    elif 20 <= number <= 29:
        final_score += number * 0.4
        from_20_to_29 += 1
    elif 30 <= number <= 39:
        final_score += 50
        from_30_to_39 += 1
    elif 40 <= number <= 50:
        final_score += 100
        from_40_to_50 += 1
    elif number > 50 or number < 0:
        final_score /= 2
        invalid_numbers += 1
print(f"{final_score:.2f}")
print(f"From 0 to 9: {(from_0_to_9 / turns) * 100:.2f}%")
print(f"From 10 to 19: {(from_10_to_19 / turns) * 100:.2f}%")
print(f"From 20 to 29: {(from_20_to_29 / turns) * 100:.2f}%")
print(f"From 30 to 39: {(from_30_to_39 / turns) * 100:.2f}%")
print(f"From 40 to 50: {(from_40_to_50 / turns) * 100:.2f}%")
print(f"Invalid numbers: {(invalid_numbers / turns) * 100:.2f}%")
