import random
import os


def tela(mensagem,mensagem2):
  
  os.system('cls') or None
  print("===================Bem-vindo ao jogo de adivinhação====================")
  print("=======================================================================")
  print(f"======={mensagem2}========")
  print("=======================================================================")
  print(f"Mensagem Sistema  :{mensagem}")
  
  
# Função : Menu Inicial -> Ecolha do nivel de dificuldade.
def menuinicial():

 dificudadeinicial= 0
 dificudadefinal = 0
 tentativas = 0
 # ---------------------------------------------------------------
 tela("|Digite o limite Inferior do intervalo de numeros  |","========================================================")
     
 while True:
 
  dificudadeint = input("=======> :")
  
  if dificudadeint.isdigit():
       dificudadeinicial = int(dificudadeint)
      
       if dificudadeinicial < 0:
       
        tela("|Digite numero interio positivo |"," ")
       else:
         break
       
  else:
       tela("|Digite numero inteiro|"," ")
       
  # ------------------------------------------------------------------------
  
 tela("|Digite o limite superior do intervalo de numeros  |","========================================================")
     
 while True:
 
  dificudadeint = input("=======> :")
  
  if dificudadeint.isdigit():
       dificudadefinal = int(dificudadeint)
         
       if dificudadefinal <= dificudadeinicial :
        tela("|Digite numero maior que o numero anterior |","========================================================")
       else:
         break
       
  else:
       tela("|Digite numero inteiro|","===================================================")
  # ----------------------------------------------------------------------------     

 tela("|Digite o numero de tentativas :|","===================================================")
     
 while True:
 
  tentativasint = input("=======> :")
  
  if tentativasint.isdigit():
       tentativas = int(tentativasint)
         
       if tentativas < 1  :
        tela("|Digite numero maior |","===================================================")
       else:
         break
       
  else:
       tela("|Digite numero inteiro|","===================================================")
  
 return dificudadeinicial, dificudadefinal, tentativas 

# Função para reinicializar o jogo.
def inicializar(men):
  
  tela("Digite -> | 1 - SAIR | 2 - JOGAR NOVAMENTE",men)
  
      
  while True:
      jogarint = input("=======> :")
      if jogarint.isdigit():
         jogar = int(jogarint)
      
         if jogar < 1 or jogar > 2:
           tela("Digite numero entre 1 e 3!","===================================================")
         elif jogar == 2:
          os.system('cls') or None
          adivinhacao()
      
         if jogar == 1:
          return "sair"
          break
      else:
         tela("Digite numero inteiro!","===================================================")
 
 
 # Função : Jogo
  
def adivinhacao():
   
     palpite = 0
     
     nivel = menuinicial()
     tentativas = nivel[2]
     
 
     numero_secreto = random.randint(nivel[0], nivel[1])
 
     
     tela(f"Voce tem {tentativas} tentativas, boa sorte!","===================================================")
     
     while True:
        palpiteint = input("Digite o seu palpite: ")
        
        respostainicializar = ""
  
        if palpiteint.isdigit():   
          palpite = int(palpiteint)
          tentativas -= 1
          tela(f"Você tem {tentativas} tentativas.", "===================================================") 
     
        
          if tentativas == 0:
            mensagemacabou = ("========| Você esgotou o numero tentativas |=======")
            respostainicializar = inicializar(mensagemacabou)
            if respostainicializar == "sair":
              break
         
         
        
          if palpite < numero_secreto:
             tela(f"Voce tem {tentativas} tentativas, Tente um número maior!","===================================================")
          elif palpite > numero_secreto:
            tela(f"Voce tem {tentativas} tentativas, Tente um número menor!","===================================================")
          else:          
            mensagemacabou = (f"=Parabéns! Você acertou o número em {nivel[2] - tentativas} tentativas!==")
            respostainicializar = inicializar(mensagemacabou)
            if respostainicializar == "sair":
             os.system('cls') or None
             print("Obrigado pela diversão! , Ate a proxima.")
            break
        else:
         tela("Digite um numero","")

adivinhacao()
