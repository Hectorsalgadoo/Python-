print("Hellow world")

#nome= input('Digite seu nome: ')
#print(f'ola, {nome}!')


nome='Hector'
idade= 23
#print('Meu nome è {} e tenho {} anos.'.format(nome, idade))
print(f'Meu nome è {nome} e tenho {idade} anos.')


preco=123.45618
print(f'Preço formatado {preco:.3f}')

nome='Python'
print(f'.{nome:<10}') #alinhado a esquera
print(f'.{nome:^10}') #centralizado
print(f'.{nome:>10}') #alinhado a direita

#1) numero inteiro com zro a esquerda (4 casas)
num_int = 10
print(f"{num_int:04d}") #0010

#2)Numero float com 3 casas decimais 
temp = 3.141
print(f'{temp:.2f}') #3,14
print(f'{temp:.4f}') #3,1410

#3) numeros formatados com tamanho 5
numeors =[10.5, 1.5, 333, 4500]
for num in numeros:
    print(f'{num:5,0f}'.replace(',','.'))

#4 numeors float formatados com duas casa
num1=3.14
num2=5.678
num3=8.9

print(f'{num1:5.2f}'.replace('.','.')) #3,14
print(f'{num2:5.2f}'.replace('.','.')) #5,68
print(f'{num3:5.2f}'.replace('.','.')) #8,90
