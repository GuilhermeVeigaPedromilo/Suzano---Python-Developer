import datetime

d = datetime.datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

# Convertendo string para datetime
date_str = "20/07/2025 15:30"
data_convertida = datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M")
print(data_convertida)
print(type(data_convertida))