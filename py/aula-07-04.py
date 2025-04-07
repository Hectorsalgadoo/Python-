#Tupla
tx=(0,1,1,3,5)
tx.count(1)

tx.index(1)

print(tx.index)

cordenadas=(3,7)
x,y=cordenadas
print (x,y)

for i in tx:
    print(i)

#dic

dicionario_vazio = {}
# Dicionário com elementos
pessoa = {
 "nome": "João",
 "idade": 25,
 "cidade": "São Paulo"
}
pessoa["profissao"] = "Engenheiro"
print(pessoa)
print(pessoa["profissao"])

pessoa.keys()
for i in pessoa.keys():
    print(i,pessoa[i])

#pessoa.items()


for i in pessoa.keys():
    print(i,"-",i[0],"-",i[1])

contatos = {
 "Ana": "555-1234",
 "Pedro": "555-5678",
 "Maria": "555-8765"
}
contatos["Lucas"] = "555-4321"

telefone_ana = contatos.get("Ana")
print(telefone_ana)
telefone_lucas = contatos.get("Lucas")
print(telefone_lucas)
contatos.pop("Pedro")
print(contatos)

#set

frutas = {"maçã", "banana", "cereja"}
frutas.add("laranja")
frutas.remove("banana")
frutas.discard("banana")

fruta_removida = frutas.pop()

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2) # {1, 2, 3, 4, 5}
print(uniao)

intersecao = conjunto1.intersection(conjunto2)
diferenca = conjunto1.difference(conjunto2)
subconjunto = {1, 2}
resultado = subconjunto.issubset(conjunto1)

print(intersecao)
print(diferenca)
print(subconjunto)
print(resultado)

diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diff_simetrica)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# União
print(A | B) # {1, 2, 3, 4, 5, 6}
# Interseção
print(A & B) # {3, 4}
# Diferença
print(A - B) # {1, 2}
# Diferença Simétrica
print(A ^ B) # {1, 2, 5, 6}