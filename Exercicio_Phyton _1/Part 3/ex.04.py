# Programa para repetir mensagem 100 vzs 
while True:
 


    Msg= input("Digite HELLO WORLD :  " ).upper()
   
    if Msg == "HELLO WORLD":
        for i in range (1,101):
          if i == 100:
             print(Msg +"  consegui")
          else:
                print(Msg)
        break 
    else:
       print ("Mensagem nao desejavel" )
