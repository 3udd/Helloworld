peso = float(input("Digite o peso: "))
alt = float(input("Digite a altura: "))

imc = peso / (alt**2)
print (f"Seu IMC é {imc}.")

if imc >= 25:
    print ("Você está com sobrepeso.")
elif imc >= 18.5:
    print ("Você tem o peso normal.")
else:
    print ("Você está abaixo do peso.")