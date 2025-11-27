


opcoes = {"S": "Solteiro", "C": "Casado", "V": "Viuvo "}

while True: 
 civil = input("Insira vosso Estado civil usando S,C ou V:").upper()
 if civil in opcoes:
    print("O Estado civil é:",opcoes[civil])# aqui chamo o dicionario criado com chaves e a variavel civil em colchetes e capturada para fazer a comparacao 
    
    break
 else:
   print("Informaçao invalida! Digite apenas  S, C e V.")

 