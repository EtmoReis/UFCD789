#calculadora basica com condicional #

algartismo1 = float(input( "insira a primeira Parcela: "))
operacao = input("Escolha a operação (+, -, *, /): ")
algartismo2 = float(input( "insira a Segunda  Parcela: "))
   
if operacao == "+":
    resultado = algartismo1 + algartismo2
elif  operacao == "-":
    resultado = algartismo1 - algartismo2   
elif operacao == "*":
    resultado = algartismo1 * algartismo2   
elif operacao ==  "/" :
     if algartismo2 != 0 :
        resultado = algartismo1 / algartismo2
     else: 
         resultado= "Erro por divisao a 0 "
else:
          resultado="Operacao invalida "
          
          
print("O resultado é :",resultado)
        