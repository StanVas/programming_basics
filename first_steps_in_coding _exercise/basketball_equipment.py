tax_per_year = int(input())
trainers = tax_per_year * 0.6
suit = trainers * 0.8
ball = suit / 4
acc = ball / 5
total_price = tax_per_year + trainers + suit + ball + acc
print(total_price)
