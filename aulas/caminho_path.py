from pathlib import Path
caminho = Path()

print(caminho) 
print(caminho.absolute())    

caminho = Path(__file__)
print(caminho)
print(caminho.parent)
print(caminho.parent.parent)