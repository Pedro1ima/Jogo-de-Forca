import adivinhacao
import forca

print("***********************************************")
print("**************Escolha o seu jogo!**************")
print("***********************************************")

print("\n(1) Forca  (2) Adivinhação \n")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogar Forca")
    forca.jogar_forca()
    
elif(jogo == 2):
    print("Jogar Adivinhação")
    adivinhacao.jogar_adivinhacao()
    
    
