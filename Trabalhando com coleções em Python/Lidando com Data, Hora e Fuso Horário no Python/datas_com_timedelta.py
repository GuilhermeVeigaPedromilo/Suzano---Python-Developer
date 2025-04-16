import datetime
from datetime import timedelta

# Criando data e hora
d = datetime.datetime(2025, 7, 19, 13, 45)

# Adicionando uma semana
d = d + datetime.timedelta(weeks=1)

print(d)

forno_temperatura = int(input("Temperatura do fogão (Cº): "))
período_no_forno_curto = 15
período_no_forno_medio = 30
período_no_forno_medio_grande = 45
período_no_forno_grande = 60
data_atual = datetime.datetime.now()

if 200 <= forno_temperatura <= 240:
    data_horario_estimado = data_atual + timedelta(minutes=período_no_forno_curto)
    print(f"O forno desligará em {data_horario_estimado}")
elif 160 < forno_temperatura <= 200:
    data_horario_estimado = data_atual + timedelta(minutes=período_no_forno_medio)
    print(f"O forno desligará em {data_horario_estimado}")
elif 140 < forno_temperatura <= 160:
    data_horario_estimado = data_atual + timedelta(minutes=período_no_forno_medio_grande)
    print(f"O forno desligará em {data_horario_estimado}")
elif 100 < forno_temperatura <= 140:
    data_horario_estimado = data_atual + timedelta(minutes=período_no_forno_grande)
    print(f"O forno desligará em {data_horario_estimado}")
else:
    período = int(input("Informe o tempo em minutos: "))
    data_horario_estimado = data_atual + timedelta(minutes=período)
    print(f"O forno desligará em {data_horario_estimado}")