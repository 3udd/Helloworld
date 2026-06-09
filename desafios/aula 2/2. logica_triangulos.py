l1 = int(input("Digite o valor do primeiro lado: "))
l2 = int(input("Digite o valor do segundo lado: "))
l3 = int(input("Digite o valor do terceiro lado: "))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print ("Temos um triângulo.")
else:
    print ("Não temos um triângulo.")