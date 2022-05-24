w = float(input())
h = float(input())
var = 3 <= h <= w <= 100
w_cm = w * 100
h_cm = h * 100
rows = w_cm / 120
desks = (h_cm -100) / 70
number_of_desks = (int(desks))
number_of_rows = (int(rows))
total_number_of_desks = number_of_desks * number_of_rows - 3
print(total_number_of_desks)
