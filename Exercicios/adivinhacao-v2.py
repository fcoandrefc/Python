import random
import os


def tela(mensagem,mensagem2):
  
  os.system('cls') or None
  print("===================Bem-vindo ao jogo de adivinhação===============")
  print("==================================================================")
  print(f"======={mensagem2}========")
  print("==================================================================")
  print(f"Mensagem do Sistema  :{mensagem}")
  
  
# Função : Menu Inicial -> Ecolha do nivel de dificuldade.
def menuinicial():

 dificudadefalcil = 25
 dificudadeintermediaria = 50
 dificudadedificil = 100
 dificudade = 0
 
 tela("|Escolha o Nivel de dificuldade|","| 1 - INICIANTE| 2 - INTERMEDIARIO | 3 - AVANÇADO |")
       
 while True:
  
  
  dificudadeint = input("=======> :")
  
  if dificudadeint.isdigit():
       dificudade = int(dificudadeint)
         
       if dificudade < 1 or dificudade > 3:
        tela("|Digite numero entre 1 e 3|","| 1 - INICIANTE| 2 - INTERMEDIARIO | 3 - AVANÇADO |")
        
                 
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
       tela("|Digite numero inteiro|","| 1 - INICIANTE| 2 - INTERMEDIARIO | 3 - AVANÇADO |")
  
  


# Função para reinicializar o jogo.
def inicializar(men):
  
  tela("Digite -> | 1 - SAIR | 2 - JOGAR NOVAMENTE",men)
  
      
  while True:
      jogarint = input("=======> :")
      if jogarint.isdigit():
         jogar = int(jogarint)
      
         if jogar < 1 or jogar > 2:
           tela("Digite numero entre 1 e 3!","")
         elif jogar == 2:
          os.system('cls') or None
          adivinhacao()
      
         if jogar == 1:
          return "sair"
          break
      else:
         tela("Digite numero inteiro!","")
 
 
 # Função : Jogo
  
def adivinhacao():
   
     palpite = 0
     tentativas = 10
     nivel = menuinicial()
 
     numero_secreto = random.randint(1, nivel)
 
     if nivel == 25:
       mensagemnivel = "==========|Voce esta no nivel INICIANTE|===========" 
     elif nivel == 50:
       mensagemnivel = "==========|Voce esta no nivel INTERMEDIARIO|===========" 
     else:
        mensagemnivel = "==========|Voce esta no nivel AVANÇADO|===========" 
 
     tela(f"Voce tem {tentativas} tentativas, boa sorte!", mensagemnivel)
     while True:
        palpiteint = input("Digite o seu palpite: ")
        
        respostainicializar = ""
  
        if palpiteint.isdigit():   
          palpite = int(palpiteint)
          tentativas -= 1
          tela(f"Você tem {tentativas} tentativas.", mensagemnivel) 
     
        
          if tentativas == 0:
            mensagemacabou = ("========| Você esgotou o numero tentativas |=======")
            respostainicializar = inicializar(mensagemacabou)
            if respostainicializar == "sair":
              break
         
         
        
          if palpite < numero_secreto:
             tela(f"Voce tem {tentativas} tentativas, Tente um número maior!",mensagemnivel)
          elif palpite > numero_secreto:
            tela(f"Voce tem {tentativas} tentativas, Tente um número menor!",mensagemnivel)
          else:          
            mensagemacabou = (f"=Parabéns! Você acertou o número em {10 - tentativas} tentativas!==")
            respostainicializar = inicializar(mensagemacabou)
            if respostainicializar == "sair":
             os.system('cls') or None
             print("Obrigado pela diversão! , Ate a proxima.")
            break
        else:
         tela("Digite um numero",mensagemnivel)

adivinhacao()
