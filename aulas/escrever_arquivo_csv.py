from pathlib import Path
import csv
caminho  = Path(__file__).parent.parent / 'arquivo01.csv'

lista = [
{'Name': 'Brandon Hess', 'Age': '72', 'City': 'Lauraberg'},
{'Name': 'Matthew Warner', 'Age': '43', 'City': 'Englishfort'},
{'Name': 'Justin Jackson', 'Age': '92', 'City': 'Dustinmouth'},
{'Name': 'Michele Rodriguez', 'Age': '38', 'City': 'New Tamara'},
{'Name': 'Geoffrey Nelson', 'Age': '67', 'City': 'Jesushaven'},
{'Name': 'Ashley White', 'Age': '82', 'City': 'West Johnfort'},
]

with open(caminho, 'w') as arquivo:
    nome_colunas = ['Name', 'Age', 'City']
    escritor = csv.writer(arquivo)
    escritor.writerow(nome_colunas)
    for i in lista:
        escritor.writerow(i.values())


