peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'O seu IMC é {imc:.1f}')
    print('Você está ABAIXO DO PESO normal')

elif imc >= 18.5 and imc < 25:
    print(f'O seu IMC é {imc:.1f}')
    print('PARABÉNS! Você está na faixa de PESO NORMAL.')

elif imc >= 25 and imc < 30:
    print(f'O seu IMC é {imc:.1f}')
    print('Você está ACIMA DO PESO normal.')

elif imc >= 30 and imc < 40:
    print(f'O seu IMC é {imc:.1f}')
    print('Você está em OBESIDADE.')

elif imc > 40:
    print(f'O seu IMC é {imc:.1f}')
    print('Você está em obesidade MORBIDA')