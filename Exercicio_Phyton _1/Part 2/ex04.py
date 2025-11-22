## calculadora de massa Corporal IMC
nome =input("Digite vosso nome:")
idade = int(input("Digite vosso idade:"))
peso = float(input("Digite vosso peso: "))
altura = float (input("Digite vosso altura: "))


IMC = peso /  (altura **2)
 
if IMC < 17:
    print("Classificação: Muito abaixo do peso")
elif IMC < 18.5:
        print("Classificação: Abaixo do peso")
elif IMC < 25:
            print("Classificação: Peso normal")
elif IMC < 30:
                print("Classificação: Acima do peso")
elif IMC < 35:
                    print("Classificação: Obesidade I")
elif IMC < 40:
                        print("Classificação: Obesidade II (severa)")
else:
                        print("Classificação: Obesidade III (mórbida)")