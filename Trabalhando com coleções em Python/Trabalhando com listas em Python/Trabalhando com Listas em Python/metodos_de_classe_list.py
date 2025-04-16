#  [].append // [].clear // [].copy // [].count // 
# [].extend // [].index // [].pop // [].remove // 
# [].reverse // [].sort // len() // [].sorted //

lista_de_compras = [
    "Pão", "Carne", "Feijão"
]

lista_de_compras_2 = []

lista_de_compras_3 = [
    "Pão", "Pão", "Rosca Doce", "Brusqueta"
]

lista_de_compras_4 = [
    "Manteiga", "Doce de leite", "Berinjela"
]

listas = []

copy_lista = lista_de_compras.copy()
lista_de_compras.clear()
lista_de_compras.append("Ovos")
lista_de_compras.append("Banana")
lista_de_compras.append(["Trigo", "Brinde", "Pão"])
lista_de_compras_2.append([copy_lista, "Uvas"])

position_ovo = lista_de_compras.index("Ovos")

count_pao = lista_de_compras_3.count("Pão")

listas.extend([
    lista_de_compras, lista_de_compras_2, 
    lista_de_compras_3, lista_de_compras_4
])

select_part_list = listas.pop(2)

lista_de_compras_3.remove("Pão")

lista_de_compras_3.reverse()

lista_de_compras_4.sort() # Dentro do sort, pode utilizar outros parâmetros para tratar

qtd_listas = len(listas)

list_numbers = list(range(5))

print(f''' === MÉTDOS DE CLASSE PARA LISTAS ===

      Lista de compras 1: {lista_de_compras}, 
      Lista de compras 2: {lista_de_compras_2},
      Removendo um dos Pães da terceira lista: {lista_de_compras_3},
      Terceira lista invertida: {lista_de_compras_3},
      Ordenando alfabeticamente a terceira lista: {lista_de_compras_4}
      Posição dos Ovos na lista 1: {position_ovo},
      Quantas vezes aparece Pão na lista 3 ? {count_pao},
      Lista total: {listas},
      Quantidade de listas: {qtd_listas}
      Selecionando terceira parte das listas: {select_part_list},
      Lista de números com sorted: {sorted(list_numbers)}
''')