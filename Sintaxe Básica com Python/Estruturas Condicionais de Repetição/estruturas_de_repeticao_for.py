procure_usuario = input("INSIRA UM NOME OU ID: ")
listas = [(1, "Guilherme"), (2, "Veiga"), (3, "Gabi")]

encontrado = False

for id, nome in listas:
    if procure_usuario == str(id) or procure_usuario.lower() == nome.lower():
        print(f"Usuário encontrado: ID={id}, Nome={nome}")
        encontrado = True
        break

if not encontrado:
    print("ESTE USUÁRIO NÃO EXISTE")