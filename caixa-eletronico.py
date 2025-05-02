valor = int(input('Digite o valor: \n'))

notas_100 = valor // 100
valor = valor % 100

notas_50 = valor // 50
valor = valor % 50

notas_20 = valor // 20
valor = valor % 20

if notas_100 > 0:
    print(f'{notas_100} notas de R$100')
if notas_50 > 0:
    print(f'{notas_50} notas de R$50')
if notas_20 > 0:
    print(f'{notas_20} notas de R$20')