import random
#a = random.randrange(1, 10,1)
#b = random.randint(1, 10)
#c= random.uniform(1, 10)
#d = random.random()
nomes = ['Ana', 'João', 'Maria', 'José']
#random.shuffle(nomes)
#random.choice(nomes)
a = random.sample(nomes, k=2)
b = random.choices(nomes, k=3)
c = random.choice(nomes)
print(c)


#print(a)
#for i in range(b):
#    print(i)
#print(d)