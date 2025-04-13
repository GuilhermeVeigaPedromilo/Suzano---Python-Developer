curso_1 = "pYthon"
curso_2 = "          Python   "
curso_3 = "Python"

#  MAIÚSCULA, minúscula e Título
print(curso_1.upper()) # PYTHON
print(curso_1.lower()) # python
print(curso_1.title()) # Python

# Eliminando espaços em branco de uma str
print(curso_2.strip()) # "Python"
print(curso_2.rstrip()) # "          Python"
print(curso_2.lstrip()) # "Python    "

# Junções e Centralização
print(curso_3.center(10, "#")) # "##Python##"
print(".".join(curso_3)) # "P.y.t.h.o.n"