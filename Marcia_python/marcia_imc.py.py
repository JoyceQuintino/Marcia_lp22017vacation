nome =(input('Informe seu nome: '))
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/(altura * altura)
print('\n=== Calculo do IMC ===\n')
print(nome + ' seu é IMC = %.2f'% imc)
if imc <= 18.5:
    print('Você está abaixo do peso')
elif  imc > 18.5 and imc <= 24.9:
    print('Você está com peso ideal')
elif imc > 24.9 and imc <= 29.9:
    print('Você está acima do peso')
elif imc > 29.9 and imc <= 34.9:
    print('Você está com obesidade grau I')
elif imc > 34.9 and imc <= 39.9:
    print('Você está com obesidade grau II (servera)')
else:
     print('Você está com obesidade grau III (mórbida)')

    
