sal = float(input("Digite seu salário: "))

if sal > 1500:
    sal_novo = sal + (sal/100*10)
    print (f"Seu novo salário é R$ {sal_novo}")
else:
    sal_novo = sal + (sal/100*15)
    print (f"Seu novo salário é R$ {sal_novo}")