idade = int(input("Informe uma idade maior que zero e menor que 120: "))
print(idade, "anos")
if idade >= 1 and idade <= 11:
	print("Criança")
elif idade > 11 and idade <= 19:
	print("Adolescente")
elif idade > 19 and idade <= 59:
	print("Adulto")
elif idade > 59 and idade < 120:
    print("Idoso")
else:
        print("Idade inválida")






