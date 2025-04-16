import datetime
#  Ou from datetime import date

data = datetime.date(2025, 4, 15,)
# Ou d = date(2025, 4, 15)

data_atual = datetime.date.today()

data_atual_e_hora = datetime.datetime.today()

print(data)
print(data_atual)
print(data_atual_e_hora)