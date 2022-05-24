price_per_kg_vegetables = float(input())
price_pre_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_frits = int(input())
euro = 1.94
total_price_vegetables = price_per_kg_vegetables * total_kg_vegetables
total_price_fruits = price_pre_kg_fruits * total_kg_frits
total_price_euro = (total_price_vegetables + total_price_fruits) / euro
print(f'{total_price_euro:.2f}')
