animal = input()
class_animal = ''
if animal == 'dog':
    class_animal = 'mammal'
elif animal == 'crocodile' or animal == 'snake' or animal == 'tortoise':
    class_animal = 'reptile'
else:
    class_animal = 'unknown'
print(class_animal)
