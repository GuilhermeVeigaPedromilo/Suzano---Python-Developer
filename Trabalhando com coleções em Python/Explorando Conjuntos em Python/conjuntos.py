DADOS_LISTA = set(list(range(10)))
OTHER_DADOS = [1, 3 ,6, 20, 11]
print(DADOS_LISTA)
print(OTHER_DADOS)

# Métodos da classe set

conjunto_a = {1, 2}
conjunto_b = [3, 4]
conjunto_c= {75, 20}

union = conjunto_a.union(conjunto_b)
intersection = union.intersection(conjunto_b)
difference = union.difference(intersection)
symetric_difference = intersection.symmetric_difference(difference)
isssubsetTrue = symetric_difference.issubset(union)
isssubsetFalse = symetric_difference.issubset(conjunto_c)
isdisjointTrue = symetric_difference.isdisjoint(conjunto_c)
isdisjointFalse = symetric_difference.isdisjoint(union)

print(f'''
========== MÉTODOS DA CLASSE SET ==========
União: {union},
Interseção: {intersection},
Diferença: {difference},
Diferença Siméetrica: {symetric_difference}
Verifica se os valores estão em um subconjunto, o qual 
está conrido em um elemento: {isssubsetTrue, isssubsetFalse },
Verifica se os conjuntos são elementos disjuntos:  {isdisjointTrue, isdisjointFalse}''')

union.add(7)
conjunto_a.discard(2)
is_in_union = 10 in union

print(f'''Adicionar: {union},
Descarta: {conjunto_a}
Verica se "n" está em um elemento: {is_in_union}
''')