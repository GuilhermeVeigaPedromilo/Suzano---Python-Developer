people_list = {
    "joao@uol.com": 
    {"nome": "João da Silva", 
     "idade": 30, 
     "cpf": "123.456.789-00"},
    "maria@uol.com": 
    {"nome": "Maria Souza", 
     "idade": 25, 
     "cpf": "987.654.321-11"},
    "carlos@hotmail.com": 
    {"nome": "Carlos Pereira", 
     "idade": 40, 
     "cpf": "111.222.333-44"}
}

new_dictionary = {}
new_dictionary.fromkeys(["nome", "telefone"])
select_an_user = people_list.get("joao@uol.com")
tuple_with_items = people_list.items()
keys = people_list.keys()
item = people_list.popitem()

print(f'''================= MÉTODOS PARA DICIONÁRIO =================
Dicionário: {people_list}

Criar um dicionário e apenas definir as chaves: {new_dictionary}

Acessando o dicionário: {select_an_user}

Retornando tuplas de um dicionário: {tuple_with_items}

Retorna as chaves do dicionário: {keys}

Retorna os items do dicionário: {item}
''')

set_default = people_list.get("maria@uol.com").setdefault("telefone", "(19)98138-9528")

print(f'''Adiciona uma chave se esta não existir no dicionário: {people_list}
''')

update = people_list.update({"carlos@hotmail.com": {"idade", 38}})
values = people_list.values()
verify_key = "guipedromilo@hotmail.com" in people_list

print(f'''Alter os valores de uma chave ou adiciona uma chave: {people_list}

Retorna todos os valores do dicionário: {values}

Verifica se uma chave existe ou está em um dicionário: {verify_key}
''')

del people_list["carlos@hotmail.com"]

print(f'''Deleta chaves ou valores no dicionário: {people_list}
''')
people_list.clear()

print(f"Limpando o dicionário: {people_list}")