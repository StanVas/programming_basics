yearly_tax = int(input())

trainers = yearly_tax * 0.6
sport_suit = trainers * 0.8
ball = sport_suit * 0.25
accessories = ball * 0.2
total = trainers + sport_suit + ball + accessories + yearly_tax
print(f'{total:.2f}')
