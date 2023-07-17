from tela import Tela

import os



class Inicializar:
    
    def __init__(self,mensagem):
     self.mensagem = mensagem

    def inicializarjogo(self,mensageminicializar,mensagempontos):
     self.mensageminicializar = mensageminicializar
     self.mensagempontos = mensagempontos
     
     
      
        
     minhatela = Tela("","","")
     minhatela.telamensagens(self.mensageminicializar,"Digite -> | 1 - SAIR | 2 - JOGAR NOVAMENTE",self.mensagempontos)
        
     while True:
        jogarint = input("=======> :")
        if jogarint.isdigit():
            jogar = int(jogarint)
      
            if jogar < 1 or jogar > 2:
              minhatela.telamensagens("Digite numero entre 1 e 3!","===================================================","")
            elif jogar == 2:
               os.system('cls') or None
               return  "continuar"
               break
      
            if jogar == 1:
              return "sair"
              break
        else:
          minhatela.telamensagens("Digite numero inteiro!","===================================================","")
        