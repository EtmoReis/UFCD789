

# aqui vou criar  em forma de lista os meses 
lista = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
while  True: #criei um ciclo infinito ate o ultilizador inserir o valor desejado 
  mes = int(input("Digite o numero do mês desejado:  "))

  if 1 <= mes <= 12:
     print("O mês é:", lista[mes - 1])# aqui o (-1) faz com que o ultilizador ao digitar 1 ele ande uma posicao atras sendo assim 1= a 0 (janeiro)
     break
  elif mes <= 0 :
     print ("O mês deve ser um valor entre 1 e 12 ")

  else: 
     print("Numero Invalido !Digite entrte 1 e 12")