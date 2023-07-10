import random
import os


def tela(mensagem):
  
  os.system('cls') or None
  print("===================Bem-vindo ao jogo de adivinhação===============")
  print("==================================================================")
  print("=======| 1 - INICIANTE| 2 - INTERMEDIARIO | 3 - AVANÇADO |========")
  print("==================================================================")
  print(f"Mensagem do Sistema:>>>>>>>{mensagem}")
  
   

# Função : Menu Inicial -> Ecolha do nivel de dificuldade.
def menuinicial():

 dificudadefalcil = 25
 dificudadeintermediaria = 50
 dificudadedificil = 100
 dificudade = 0
 
 tela("")
       
 while True:
  
  
  dificudadeint = input("=======> :")
  
  if dificudadeint.isdigit():
       dificudade = int(dificudadeint)
         
       if dificudade < 1 or dificudade > 3:
        tela("Digite numero entre 1 e 3!")
        
                 
       elif dificudade == 1:
        os.system('cls') or None
        return dificudadefalcil
        break
       elif dificudade == 2:
        os.system('cls') or None
        return dificudadeintermediaria
        break      
       else:
        os.system('cls') or None
        return dificudadedificil
        break 
         
  else:
       tela("Digite numero inteiro!")
  
  


# Função para reinicializar o jogo.
def inicializar():
  
 
      
  while True:
      jogar = int(input("Digite -> | 1 - SAIR | 2 - JOGAR NOVAMENTE"))
      
      if jogar < 1 or jogar > 2:
         os.system('cls') or None
         print("Opção invalida!!!")
         
      elif jogar == 2:
         os.system('cls') or None
         adivinhacao()
      
      if jogar == 1:
        return "sair"
        break
 
 # Função : Jogo
  
def adivinhacao():
   
 palpite = 0
 tentativas = 10
 
 numero_secreto = random.randint(1, menuinicial())
 
 
 tela(f"Voce tem {tentativas} tentativas, boa sorte!")

 
  

 while True:
     palpite = int(input("Digite o seu palpite: "))
     tentativas -= 1
     
     tela(f"Você tem {tentativas} tentativas.") 
     
        
     if tentativas == 0:
         tela(f"Você esgotou o numero tentativas {tentativas} .")
         if inicializar() == "sair":
           break
         
         
        
     if palpite < numero_secreto:
            tela(f"Voce tem {tentativas} tentativas, Tente um número maior!")
     elif palpite > numero_secreto:
            tela(f"Voce tem {tentativas} tentativas, Tente um número menor!")
     else:
            tela(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            if inicializar() == "sair":
             break

adivinhacao()
