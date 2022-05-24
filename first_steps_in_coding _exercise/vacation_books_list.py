number_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())
total_time_for_reading = number_of_pages / pages_per_hour
hours_per_day = total_time_for_reading // days
print(hours_per_day)
