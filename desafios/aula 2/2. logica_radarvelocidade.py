vel = float(input("Digite a velocidade de um carro: "))

if vel > 80:
    multa = (vel - 80) * 5
    print (f"Sua multa é de R$ {multa}.")