nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? ")) #converte o valor da variavel pra q seja só int

resto = 100 - idade

print (f"""Olá, {nome}. Você tem {idade} ano(s). 
Aproveite seus próximos {resto}, serão seus últimos.""")