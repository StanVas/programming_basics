nylon = int(input())
paint = int(input())
paint_thinner = int(input())
working_hours = int(input())
price_nylon = (nylon + 2) * 1.5
price_paint = (paint + (paint * 0.1)) * 14.5
price_paint_thinner = paint_thinner * 5
total_sum_materials = price_nylon + price_paint + price_paint_thinner + 0.4
price_workers = (total_sum_materials * 0.3) * working_hours
total_price = total_sum_materials + price_workers
print(total_price)
