country = input()
instrument = input()
score = 0
if country == 'Russia':
    if instrument == 'ribbon':
        score = 9.1 + 9.4
    elif instrument == 'hoop':
        score = 9.3 + 9.8
    elif instrument == 'rope':
        score = 9.6 + 9
elif country == 'Bulgaria':
    if instrument == 'ribbon':
        score = 9.6 + 9.4
    elif instrument == 'hoop':
        score = 9.55 + 9.75
    elif instrument == 'rope':
        score = 9.5 + 9.4
elif country == 'Italy':
    if instrument == 'ribbon':
        score = 9.2 + 9.5
    elif instrument == 'hoop':
        score = 9.45 + 9.35
    elif instrument == 'rope':
        score = 9.7 + 9.15
diff = 20 - score
percent = (diff/20) * 100

print(f'The team of {country} get {score:.3f} on {instrument}.')
print(f'{percent:.2f}%')
