hora_inicial = int(input('Digite a hora inicial: '))
hora_final = int(input('Digite a hora final: '))
if hora_inicial == hora_final:
    duracao = 24
elif hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final
print(f'Duração total: {duracao}h')