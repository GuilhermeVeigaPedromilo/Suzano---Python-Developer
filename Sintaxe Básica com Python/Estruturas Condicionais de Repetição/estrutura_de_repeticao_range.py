# range(stop) -> range object
# range(start, stop[, step]) -> range object

lista = list(range(4))
print(lista)
# [0, 1, 2, 3]

# Utilizando range com for
for numero in range(0, 11):
    print(numero)

num_min = int(input("INSIRA O VALOR MÍNIMO: "));
num_max = int(input("INSIRA O VALOR MÁXIMO: "))

for list_num in range(num_min, num_max):
    print(list_num, end=" ")
