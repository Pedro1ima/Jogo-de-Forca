import random
    

def jogar_forca():
    
    imprime_mensagem_abertura()
    palavra_secreta = carregar_palavras_secretas()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas, "\n")
    
    enforcou = False
    acertou = False
    erros = 0
    
    # Enquanto não enforcou E não acertou
    while(not enforcou and not acertou):
        
        chute = pede_o_chute()
        
        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        
        else:
            erros += 1 # Seria a mesma coisa que erros = erros + 1
            print("Ops, você errou! Faltam {} tentativas.".format(7-erros))
            desenhaforca(erros)

            
        enforcou = erros == 7 # Quando o usuário atingir 6 erros, o loop parará já que ele terá enforcado.
        acertou = "_" not in letras_acertadas # Acertou vai ser TRUE, quando não tiver mais "_" dentro das letras_acertadas.
        print(letras_acertadas)
                           
    if(acertou):
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta) 


# FUNÇÕES:

def imprime_mensagem_abertura():
    print("***********************************************")
    print("*** Olá mundo! Bem-vindo ao jogo de Forca!! ***")
    print("***********************************************\n")
    
    
def carregar_palavras_secretas():
     # Dentro do arquivo "palavras.txt" foram criadas todas as palvras e apartir disso, criamos uma lista conterá os elementos de cada linha do arquivo.
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip() # Tirando o \n
        palavras.append(linha) # Cada linha está sendo adicionada dentro da lista como um elemento.
    arquivo.close()
        
    # Tornar a palavra aleatória.
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta # Serve para a função retornar o valor da palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta] # Crie um "_" dentro da lista, para cada letra na palavra_secreta.


def pede_o_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper() # Para os espaçamentos no input não afetarem a entrada do chute & as letras ficarem maiúsculas.
    return chute   

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0 # Para mostrar a posição de cada letra da palavra.
    for letra in palavra_secreta: # 'letra' vai destrinchar todas as letras da variável 'palavra_secreta'.
        if (chute == letra.upper()): # .upper() é para deixar todas as letras maiúsculas.
            letras_acertadas[index] = chute
        index = index + 1 # Seria a mesma coisa que index += 1
        
def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.     ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /       ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '._         ")
    print("        '-------'       ")

def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________          ")
    print("   /               \         ")
    print("  /                 \        ")
    print("//                   \/\     ")
    print("\|   XXXX     XXXX   | /     ")
    print(" |   XXXX     XXXX   |/      ")
    print(" |   XXX       XXX   |       ")
    print(" |                   |       ")
    print("  \_      XXX      __/       ")
    print("   |\     XXX     /|         ")
    print("   | |           | |         ")
    print("   | I I I I I I I |         ")
    print("   |  I I I I I I  |         ")
    print("   \_             _/         ")
    print("     \_         _/           ")
    print("       \_______/             ")
    
def desenhaforca(erros):
    print("  ______      ")
    print(" |/     |     ")

    if(erros == 1):
        print(" |     (_)    ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |     (_)    ")
        print(" |      |     ")
        print(" |            ")

    if(erros == 3):
        print(" |     (_)    ")
        print(" |     \|     ")
        print(" |            ")

    if(erros == 4):
        print(" |     (_)    ")
        print(" |     \|/    ")
        print(" |            ")

    if(erros == 5):
        print(" |     (_)   ")
        print(" |     \|/   ")
        print(" |      |    ")

    if(erros == 6):
        print(" |     (_)   ")
        print(" |     \|/   ")
        print(" |      |    ")
        print(" |     /     ")
    
    if(erros == 7):
        print(" |     (_)   ")
        print(" |     \|/   ")
        print(" |      |    ")
        print(" |     / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#Para rodar a forca sem precisar ir pelo arquivo do "jogos.py"
if(__name__ == "__main__"):
    jogar_forca()
