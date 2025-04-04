valstr=123123

qtdpt=0
numero=True
numflt=False

for i in valstr:
    if i ==".":
        print( i,"tem ponto")
        qtdpt +=1
        numflt=True
    elif i >-"1" and i <="9":
        print(i,"numero"
    else:
        print(i, "nao numero")
        nuemro = False
        break

if not numero or qtdpt > 1:
    print("numero invalido")
else:
    print("numero invalido")

if numflt:
    valor=float(valstr)
    print(valor,type(valor))
    print("nuemro float")
else:
    valor=int(valstr)
    print(valor, type(valor))
    print("numero inteiro")




######################################

frutas=["maca", "abacaxi", "morango", "banana"]
frutas[0]

for i in (0, 1, 2 ,3):
    print(frutas[i])

if frutas[-4]==frutas[0]:
    print(frutas[0])

# append adiciona
# remove retira
# len tamanho da lista