# Old Style %
nome = "Guilherme"
idade = 17
profissão = "Software Engineer"
calc = 3 / 2.71343

print("Old Style: Hi, my name is %s. I'm %d years old, I work as a %s and I like to play violin!" % (nome, idade, profissão))

# Método format
print("Format_1: Hi, my name is {}. I'm {} years old, I work as a {} and I like to play violin!".format(nome, idade, profissão))
print("Format_2: Hi, my name is {0}. I'm {2} years old, I work as a {1} and I like to play violin!".format(nome, profissão, idade))
print("Format_3: Hi, my name is {nome}. I'm {idade} years old, I work as a {profissão} and I like to play violin!".format(nome=nome, idade=idade, profissão=profissão))
# Definido com um dicionário print("Format_4: Hi, my name is {nome}. I'm {idade} years old, I work as a {profissão} and I like to play violin!".format(**pessoa))

# f-string
print(f"f-string: Hi, my name is {nome}. I'm {idade} years old, I work as a {profissão} and I like to play violin!")
print(f"Valor do cálculo: {calc:.2f}") # Apenas duas casas após a vírgula