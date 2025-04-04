
# Cp1-python Gutemberg rm562267 Hector rm565498

valorVenda = input("Venda..................:")
is_error = False

if valorVenda.isdigit():
    valorVenda=float(valorVenda)
else:
    is_error=True


if is_error == False:
    desconto = 0
    descCupon=0

    if valorVenda<=1000:
        desconto = valorVenda*0.05
        valorVenda -= desconto

    else:
        desconto = valorVenda*0.1
        valorVenda -= desconto


    possuiCupom=input("Tem cupom, [s]im [n]ao?..: ")
    possuiCupom=possuiCupom.lower()

    if possuiCupom == "s":
        descCupon = 50
        valorVenda -= descCupon

    elif possuiCupom == "n":
        descCupon = 0
        valorVenda += 0
    else:
        print("Resposta invalida")


    print("RELATORIO:")
    print(f"Venda............:{valorVenda:7,.2f}")
    print(f"Desconto.........:{desconto:7,.2f}")
    print(f"Cupom............:{descCupon:7,.2f}")
    print(f"Venda Final......:{valorVenda:7,.2f}")
else:
    print("Entrada invalida!")


    
    

