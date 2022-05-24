number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())
price_chicken_menus = number_of_chicken_menus * 10.35
price_fish_menus = number_of_fish_menus * 12.4
price_vegetarian_menus = number_of_vegetarian_menus * 8.15
desert = (price_vegetarian_menus + price_chicken_menus + price_fish_menus) * 0.2
total_price = price_vegetarian_menus + price_fish_menus + price_chicken_menus + desert + 2.5
print(f'{total_price:.2f}')
