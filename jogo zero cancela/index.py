print(
    "\n\t",
    33 * "=",
    "\n\t | \t BEM VINDO! \t\t |",
    "\n\t | \t JOGO ZERO CANCELA \t |",
    "\n\t",
    33 * "=",
)

num = float(input("\n\t Digite um número para somar: "))

soma = 0

contRodadasZero = 0

contDesconsiderados = 0
contConsiderados = 0

numAntecessor01 = 0
numAntecessor02 = 0
numAntecessor03 = 0

while num >= 0:
    if num == 0:
        contRodadasZero += 1

        # if contRodadasZero == 1:
        #     contDesconsiderados += 1
        #     contConsiderados -= 1

        # elif contRodadasZero == 2:
        #     soma -= numAntecessor01
        #     contDesconsiderados += 1
        #     contConsiderados -= 1

        # elif contRodadasZero == 3:
        #     soma -= numAntecessor01
        #     contDesconsiderados += 1
        #     contConsiderados -= 1

        if contRodadasZero > 3:
            print(f"Só é permitido até 3 zeros consecutivos!!!")
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
    97 * "=",
    "\n | \t SOMA TOTAL \t | \t Números considerados \t | \t Números desconsiderados \t |",
    f"\n | \t  {soma} \t\t | \t {contConsiderados} \t\t\t | \t {contDesconsiderados} \t\t\t\t |",
    "\n",
    97 * "=",
)

print("\n\t", 33 * "-", "\n\t | \t ORBIGADO POR JOGAR! \t |", "\n\t", 33 * "-")
