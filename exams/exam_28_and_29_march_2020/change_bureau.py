bitcoins = int(input())
yuan = float(input())
commission = float(input())

yuan_to_bgn = (yuan * 0.15) * 1.76
bit_to_bgn = bitcoins * 1168
total_bgn = yuan_to_bgn + bit_to_bgn
total_euro = (total_bgn / 1.95)
total = total_euro - ((total_euro * commission) / 100)
print(f'{total:.2f}')
