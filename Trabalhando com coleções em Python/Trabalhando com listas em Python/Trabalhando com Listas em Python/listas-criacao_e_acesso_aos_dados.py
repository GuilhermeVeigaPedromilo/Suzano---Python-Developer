fruits = ["orange", "apple", "banana"]

letters = list("python")

numbers = list(range(20))

pares = [numbers for numbers in numbers if numbers % 2 == 0] # Filtro de dados
valores_alterados = [numero ** 2 for numero in numbers ] # Mdificando os valores

matriz = [
    [1, 0, 2],
    [3, 4, 5],
    [129, 30, 23]
]

print(f''' Fruits: {fruits}, 
      letters: {letters}, 
      Multiple numbers of 2: {pares},
      Update Numbers: {valores_alterados}
      "Matriz: " {matriz[2][2]}
''')