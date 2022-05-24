packages_pens = int(input())
packages_markers = int(input())
detergent_lt = int(input())
discount = int(input())
price_pens = packages_pens * 5.8
price_markers = packages_markers * 7.2
price_detergent = detergent_lt * 1.2
total = price_pens + price_markers + price_detergent
total_discount = total * discount/100
final_price = total - total_discount
print(f'{final_price:.2f}')
