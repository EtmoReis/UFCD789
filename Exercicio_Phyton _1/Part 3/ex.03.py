# Calculadora de media 

while True:
 try:


    valor1= int(input("Digite a Primeira parcela :  " ))
    valor2= int(input("Digite a Segunda parcela :  " ))
    valor3= int(input("Digite a Terceira parcela :  " ))
    valor4= int(input("Digite a Quarta  parcela :  " ))
    break # aqui  para se todos os valores forem desejaveis 
 except ValueError:# digitar letra ou decimal, mostra mensagem e repete.
      print("Erro!Digite apeneas numeros Inteiros ")

calc = (valor1 + valor2 + valor3 +valor4)// 4
print("O valor da Media é de :", calc)
 