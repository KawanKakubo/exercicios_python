nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculo é:', (nome.upper()))
print(f'Seu nome em minúsculo é:', (nome.lower()))
print(f'Seu nome possui:', len(nome)-nome.count(' '), 'letras.')
print(f'Seu primeiro nome possui:', (nome.find(' ')), 'letras.')
