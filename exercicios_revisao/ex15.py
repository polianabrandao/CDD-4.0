n1 = int(input('Digite o primero número: '))
n2 = int(input('Digite o segundo número: '))
while n1 == n2:
    n2 = int(input('Digite o segundo número diferente do primeiro: '))

if n1 < n2:
    print(n1, n2)
else:
    print(n2, n1)