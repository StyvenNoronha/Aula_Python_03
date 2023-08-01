from pathlib import Path
import csv

caminho  = Path(__file__).parent.parent / 'arquivo.csv'

with open(caminho, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:    
        print(linha)