ladoa = int(input('Digite o valor do Lado A:\n'))
while ladoa < 1:
    print('Digite um valor maior que 0.')
    ladoa = int(input('Digite o valor do Lado A:\n'))

ladob = int(input('Digite o valor do Lado B:\n'))
while ladob < 1:
    print('Digite um valor maior que 0.')
    ladob = int(input('Digite o valor do Lado B:\n'))

ladoc = int(input('Digite o Valor do Lado C:\n'))
while ladoc < 1:
    print('Digite um valor maior que 0.')
    ladoc = int(input('Digite o Valor do Lado C:\n'))

v1 = (ladoa + ladob)
v2 = (ladoa + ladoc)
v3 = (ladob + ladoc)

if ladoa < v3:
    resultado = True
elif ladob < v2:
    resultado = True
elif ladoc < v1:
    resultado = True
else:
    resultado = False

if resultado == True:
    print('É um triangulo')
else:
    print('Não é um triangulo')
