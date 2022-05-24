# скумрия
mackerel = float(input())
# цаца
sprat = float(input())
bonito = float(input())
scad = float(input())
mussels = int(input())
# паламуд
bonito_cost = (mackerel + (mackerel * 0.6)) * bonito
#сафрид
scad_cost = (sprat + (sprat * 0.8)) * scad
#миди
mussels_cost = 7.5 * mussels
total_cost = bonito_cost + scad_cost + mussels_cost
print(f'{total_cost:.2f}')
