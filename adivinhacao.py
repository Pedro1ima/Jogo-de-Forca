import random #para podermos usar a função random()

def jogar_adivinhacao():

    print("*****************************************************")
    print("*** Olá mundo! Bem-vindo ao jogo de Adivinhação!! ***")
    print("*****************************************************")


    # numero_secreto = random.random() * 100 # vai gerar um número aleatório (float - com muitas casas decimais)
    # numero_secreto = int(numero_secreto) # Também serve o comando --> round(numero_secreto) Para transformar o número em inteiro (int)
    # numero_secreto = round(random.random() * 100) # O problema é que vai gerar número de 0 até 100
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) fácil \n(2) Médio \n(3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
        
    elif(nivel == 2):
        total_de_tentativas = 15
        
    else:
        total_de_tentativas = 5

    print(numero_secreto)

    # while(rodada <= total_de_tentativas):
    # no final do código: rodada = rodada + 1
    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #tratar com valores em reais basta colocar dentro das {:.2F} exemplos: {:7.2F} // {:07.2F} // {:d} 
        chute_str = input("Adivinhe o número entre 1 e 100: ")
        chute = int(chute_str)
        

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue # Vai partir pra próxima interação, ou seja, vai começar o FOR novamente do início
            

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if(acertou):
            print("Você precisou de {} tentativa(s) para acertar!!".format(rodada)) 
            break # Usado para quebrar o loop/laço, já que o usuário acertou
            

        else:
            if(maior):
                print("Você errou, o seu palpite foi maior do que o número secreto")
            if(menor):
                print("Você errou, o seu palpite foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute) #O 'abs' serve pro valor não ficar negativo caso o chute seja um número maior que a resposta 
            pontos = pontos - pontos_perdidos
        
            
    print("O número secreto era: ", numero_secreto)
    print("Você fez um total de {} pontos!!".format(pontos))
    print("Fim do jogo!")

#Para rodar a Advinhação sem precisar ir pelo arquivo do "jogos.py"
if(__name__== "__main__"):
    jogar_adivinhacao()


