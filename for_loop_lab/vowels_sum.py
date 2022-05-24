text = input()
points = 0
for letter in text:
    if letter == 'a':
        points += 1
    if letter == 'e':
        points += 2
    if letter == 'i':
        points += 3
    if letter == 'o':
        points += 4
    if letter == 'u':
        points += 5
print(points)
