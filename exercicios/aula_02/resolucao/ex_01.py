#!/usr/bin/bash

#1: capturar a informação de ano de nascimento

nascimento = int(input('Informe o ano de nascimento: '))

#2: Validar se o número digitado pertence a cada um dos intervalos:

#2.1: Baby Boomer
if nascimento <= 1964:
    print('Baby Boomer')
#2.2: Geração X
elif nascimento <= 1979:
    print('Geração X')
#2.3: Geração Y
elif nascimento <= 1994:
    print('Geração Y')
#2.4: Geração Z
else:
    print('Geração Z')
