search_curso = str(input("PROCURE UM CURSO:"))

curso_1 = str("Python")
curso_2 = str("JS")

exp = search_curso is curso_1
print(exp)

exp_2 = curso_2 is not search_curso
print(exp_2)