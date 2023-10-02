n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2:
    if n1 > n3:
        print(f'O maior número é {n1}')
    else:
        print(f'O maior número é {n3}')
elif n2 > n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')
    