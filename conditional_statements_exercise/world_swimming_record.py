from math import floor

current_record = float(input())
distance = float(input())
sec_to_swim_one_met = float(input())
water_resistance = floor(distance / 15) * 12.5
current_swim_time = (distance * sec_to_swim_one_met) + water_resistance
diff = abs(current_swim_time - current_record)
if current_swim_time < current_record:
    print(f"Yes, he succeeded! The new world record is {current_swim_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
