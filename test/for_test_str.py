name = 'Mario'
k = ''
current_value = 0

for i in range(len(name)):
    current_value = i
    for j in range(current_value, i + 1):
        k += name[j]
    print(k)
