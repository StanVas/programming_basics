length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
volume_in_lt = volume / 1000
percent_total = percent / 100
total_lt = volume_in_lt - (volume_in_lt * percent_total)
print(total_lt)
