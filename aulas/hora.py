from datetime import datetime

ano  = datetime.now().year
mes  = datetime.now().month
dia  = datetime.now().day
hora = datetime.now().hour
minuto = datetime.now().minute
segundo = datetime.now().second
hoje = datetime.now().strftime('%d/%m/%Y %H:%M:%S')


#print(f'Hoje é {dia}/{mes}/{ano} e são {hora}:{minuto}:{segundo} horas.')
while True:
    print(hoje)   

#print(f'Hoje é {dia}/{mes}/{ano} e são {hora} horas.')

