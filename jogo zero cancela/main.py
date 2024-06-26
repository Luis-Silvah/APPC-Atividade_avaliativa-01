# Trabalho grupo 1
# Gabriel, Luis, Pedro Tiezo, Henrique

import time;

print('''
\t==========================================================================
\t|    BBBBB   EEEEE   M   M         V   V   IIIII   N   N   DDDD    OOOO   |
\t|    B    B  E       MM MM         V   V     I     NN  N   D   D  O    O  |
\t|    BBBBB   EEEE    M M M          V V      I     N N N   D   D  O    O  |
\t|    B    B  E       M   M          V V      I     N  NN   D   D  O    O  |
\t|    BBBBB   EEEEE   M   M           V     IIIII   N   N   DDDD    OOOO   |
\t==========================================================================
\t      |                      JOGO ZERO CANCELA                     |
\t      ==============================================================               
''')
time.sleep(2.5)

print('''\n\t 
      --------------------------------------
    |                  Regras                 |
      --------------------------------------

    |1- Digite um numero para Somar           |
    |2- [0] Apaga o ultimo numero digitado    |
    |3- numeros negativos terminam o programa |
      ------------------------------------- 
''')
time.sleep(1.5)

num = float(input("\n\t Digite um número para somar: "))

# Declaração de variaveis
soma = 0

contRodadasZero = 0

contDesconsiderados = 0
contConsiderados = 0

numAntecessor01 = 0
numAntecessor02 = 0
numAntecessor03 = 0

# Inicio do Loop
while num >= 0:
    if num == 0:
        contRodadasZero += 1

        # if contRodadasZero == 1:
        #     soma -= numAntecessor01
        #     contDesconsiderados += 1
        #     contConsiderados -= 1

        # elif contRodadasZero == 2:
        #     soma -= numAntecessor02
        #     contDesconsiderados += 1
        #     contConsiderados -= 1

        # elif contRodadasZero == 3:
        #     soma -= numAntecessor03
        #     contDesconsiderados += 1
        #     contConsiderados -= 1

        if contRodadasZero > 3:
            print(f"Só é permitido até 3 zeros consecutivos!!!")
        elif numAntecessor01 == 0:
            print("Não há números para apagar")
        else:
            soma -= numAntecessor01
            contConsiderados -= 1
            contDesconsiderados += 1

        numAntecessor01 = numAntecessor02
        numAntecessor02 = numAntecessor03
        numAntecessor03 = 0

    else:
        soma += num
        contConsiderados += 1
        contRodadasZero = 0
        
        numAntecessor03 = numAntecessor02
        numAntecessor02 = numAntecessor01
        numAntecessor01 = num

    num = float(input("\n\t Digite um número para somar: "))

print(
    "\n",
    80 * "=",
    "\n | SOMA TOTAL \t | Números considerados \t | Números desconsiderados \t |",
    f"\n | \t  {soma} \t | \t\t {contConsiderados} \t\t | \t\t  {contDesconsiderados} \t\t |",
    "\n",
    80 * "="
)

print("\n\t", 33 * "-", "\n\t | \t ORBIGADO POR JOGAR! \t |", "\n\t", 33 * "-")
