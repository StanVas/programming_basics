rolls_of_paper = int(input())
rolls_of_fabric = int(input())
glue_lt = float(input())
discount_percent = int(input())

money = (rolls_of_paper * 5.8) + (rolls_of_fabric * 7.2) + (glue_lt * 1.2)
discount = money * (discount_percent / 100)
total_money = money - discount
print(f'{total_money:.3f}')
