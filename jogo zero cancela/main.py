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
time.sleep(2.5)

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


# Declarção de variaveis
soma = 0
contNumC = 0
contNumd = 0
num = 0
cont0 = 0

numAnt1 = 0
numAnt2 = 0
numAnt3 = 0
# Inicio do loop
while num >= 0:
    num=float(input('\n\t Digite um numero para somar: '))
    if num > 0:
        soma += num
        cont0 = 0
        contNumC += 1
        numAnt3 = numAnt2
        numAnt2 = numAnt1
        numAnt1 = num

    elif num == 0:
        cont0 += 1
        contNumd += 1
        if cont0 == 1:
            soma -= numAnt1
        elif cont0 == 2:
            soma -= numAnt2
        elif cont0 == 3:
            soma -= numAnt3
        elif cont0 > 3:
            print('\n\tNumero de deletes exedido')
    else:
        
        print(f'''
             ================================================= 
            | SOMA |  NUM CONSIDERADOS  | NUM DECONSIDERADOS  |
             =================================================
            |      |                    |                     |
            |  {soma} |          {contNumC}         |          {contNumd}          |
             =================================================                  
        ''')
        time.sleep(1)
    
# Agradecimentos
print('''\t
     ______________________________
    |                              |
    |      ORBIGADO POR JOGAR!     |
     ______________________________
''')