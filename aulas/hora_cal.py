from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
fmt2 = '%d/%m/%Y'
data_Inicio = datetime.strptime('01/01/2021 00:00:00', fmt)
data_Fim = datetime.strptime('31/12/2021 23:59:59', fmt)
data_niver= datetime.strptime('02/12/1999', fmt2)
data_hoje = datetime.now()
delta = data_hoje - data_niver

print(delta.seconds)



#print(data_Fim - data_Inicio)
#print(data_Fim.timestamp() - data_Inicio.timestamp())

