import csv
from random import randint

temp = [999,999,999,999,999]

# Função recursiva que verifica se número já existe na lista
def jaFoi(a,b,c):
	for k in range(0,b):
		if temp[k] == a:
			print("Old: ",temp)
			temp[b] = randint(0,c)
			print("K:",temp[k]," B:",temp[b])
			print("New: ",temp)
			print()
			jaFoi(temp[b],b,c)

# Função que escolhe refeições aleatórias
def selectFood():
	with open("data.csv") as data:
		reader = list(csv.reader(data))
	data.close()
	tamanho = len(reader)-1
	with open("MenuSemana.txt",'w') as escolhas:
		for i in range(0,5): # Escolhe 5 refeições
			temp[i] = randint(0,tamanho)
			jaFoi(temp[i],i,tamanho)
			
		print("Final: ",temp)
		for i in range(0,5):
			abc = reader[temp[i]]
			if i>0:
				escolhas.write("\n")
			for j in abc:
				escolhas.write(j)
				escolhas.write(" ")	
	escolhas.close()