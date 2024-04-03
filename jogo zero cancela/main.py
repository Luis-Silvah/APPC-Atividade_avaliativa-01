# Trabalho grupo 1
# Gabriel, Luis, Pedro Tiezo, Henrique

import time;
print('''
==========================================================================
|    BBBBB   EEEEE   M   M         V   V   IIIII   N   N   DDDD    OOOO   |
|    B    B  E       MM MM         V   V     I     NN  N   D   D  O    O  |
|    BBBBB   EEEE    M M M          V V      I     N N N   D   D  O    O  |
|    B    B  E       M   M          V V      I     N  NN   D   D  O    O  |
|    BBBBB   EEEEE   M   M           V     IIIII   N   N   DDDD    OOOO   |
==========================================================================
      |                      JOGO ZERO CANCELA                     |
      ==============================================================               
''')
time.sleep(2)

print('''\n\t 
      --------------------------------------
    |                  Regras                 |
      --------------------------------------

    |1- Digite um numero para Somar           |
    |2- [0] Apaga o ultimo numero digitado    |
    |3- numeros negativos terminam o programa |
      ------------------------------------ 
''')
time.sleep(1.5)
num=float(input('\n\t Digite um numero para somar'))
soma=0
while num >= 0:
    num=float(input('\n\t Digite um numero para somar'))
    if num >= 0:
        soma += num
        cont0 = 0
    elif num == 0:
        soma -= num
        cont0 += 1
    else:
        print('''
            
        ''')
        time.sleep(1)
print('''
    _______________________________
    |                               |
    |       ORBIGADO POR JOGAR!     |
     _______________________________
''')