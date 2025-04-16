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

E_MAIL = input(str("Insira o e-mail do usuário: "))

print(f''' My name is {people_list[E_MAIL]["nome"]}, I'm {people_list[E_MAIL]["idade"]} years old
and my cpf is {people_list[E_MAIL]["cpf"]}''')