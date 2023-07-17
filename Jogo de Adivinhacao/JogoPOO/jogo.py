from tela import Tela
from inicializar import Inicializar
from jogador import Jogador
import random
import os


meujogador = Jogador("")




class Jogo:
    
 def __init__(self,nivel):
    self.nivel = nivel
    self.respostainicialzar = ""
    
 
    
     

 def jogoiniciar(self):
   
   meujogo = Inicializar("")
   
   minhatela = Tela("","","")
   palpite = 0
     
   tentativas = self.nivel[2]
   
 
   numero_secreto = random.randint(self.nivel[0], self.nivel[1])
 
     
   minhatela.telamensagens(f"=========== Voce tem {self.nivel[2]} tentativas, boa sorte! ===========","","")
     
   while True:
        palpiteint = input("Digite o seu palpite: ")
        
        
  
        if palpiteint.isdigit():   
          palpite = int(palpiteint)
          tentativas -= 1
          minhatela.telamensagens(f"=============== Você tem {tentativas} tentativas. ===============", "","'") 
     
        
          if tentativas == 0:
            mensagemacabou = ("========| Você esgotou o numero tentativas |=======")
            
            self.respostainicialzar = meujogo.inicializarjogo(mensagemacabou,"")
            break
            
         
         
        
          if palpite < numero_secreto:
             minhatela.telamensagens(f"================= Você tem {tentativas} tentativas. ================"," Tente um número maior!","")
          elif palpite > numero_secreto:
            minhatela.telamensagens(f"================= Você tem {tentativas} tentativas. =================","Tente um número menor!","")
          else:          
            mensagemacabou = (f"Parabéns! Você acertou o número [{numero_secreto}] em {self.nivel[2] - tentativas} tentativas!","")
            
            minhatela.telamensagens(mensagemacabou,"Digite seu nome:","")
            meujogador.gardarjogador(self.nivel[1],self.nivel[2])
            
            self.respostainicialzar = meujogo.inicializarjogo(mensagemacabou,meujogador.dicionario)
            break
            
            
        else:
         minhatela.telamensagens("Digite um numero","","")
         