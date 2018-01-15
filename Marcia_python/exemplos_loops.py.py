print('===== Numeros pares entre zero e cinquenta =====')
n = 0
while n <= 50:
    print(n, end =' ' )
    n+= 2

print('\n\n===== Tabuada de multiplicação de um número =====')
num = int(input('Informe o número da tabuada: '))
for seq in range(0, 11):
    print('%2d x %2d = %3d' % (seq, num, seq * num ))
    

    

