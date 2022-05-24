from math import ceil, floor
magnolias = int(input())
hyacinths = int(input())      # зюмбюли
roses = int(input())
cactus = int(input())
gift_price = float(input())
magnolias_price = magnolias * 3.25
hyacinths_price = hyacinths * 4
roses_price = roses * 3.5
cactus_price = cactus * 8
total = magnolias_price + hyacinths_price + roses_price + cactus_price
taxes = total * 0.05
total_price = total - taxes
diff = abs(total_price - gift_price)
if total_price >= gift_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')
