num=float(input('\n\t Digite um numero para somar: '))

soma = 0

contRodadas = 0

contDesconsiderados = 0
contConsiderados = 0

subtrair = 0

num01 = 0
num02 = 0
num03 = 0

while num >= 0:
    if (num == 0): 
        print(f"Subtrair Número  {subtrair}")
        contDesconsiderados += 1
        if contDesconsiderados >= 3:
           print(f"Só é permitido até 3 zeros consecutivos!!!") 
        else:
            print(f"Subtrair Número {contDesconsiderados} {subtrair}")
        
    else: 
        subtrair = num
        soma = soma + num
        contConsiderados += 1
       
    contRodadas += 1

    print(f"contador de rodadas: {contRodadas}")

    if(contRodadas < 4):
        print(f"Rodada {num}")
    else: 
        contRodadas = 1

    num=float(input('\n\t Digite um numero para somar: '))

        
print(f"\n Números desconsideraos = {contDesconsiderados}")
print(f"\n Números considerados = {contConsiderados}")
print(f"\n Soma Total = {soma}")

