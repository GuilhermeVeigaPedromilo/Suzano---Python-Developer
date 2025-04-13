# VERIFICA SE O CURSO PROCURADO ESTÁ NA LISTA
search_curso = str(input("PROCURE UM CURSO:"))

cursos = ["Python", "JAVA", "JS", "React", "HTML e CSS", "Cloud"]

exp = search_curso in cursos 
print(exp)