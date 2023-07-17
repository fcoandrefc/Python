import os
from jogador import Jogador

listjogador = Jogador("")


class Tela:

        
    def __init__(self,mensage1,mensagem2,mensagem3):
        self.mensage1 = mensage1
        self.mensage2 = mensagem2
        self.mensage3 = mensagem3
        
        
        
    def telainicial(self):
        
           
        os.system('cls') or None
        print("===================Bem-vindo ao jogo de adivinhação====================")  
        print("=======================================================================") 
        print("===================Jogadores e Pontuação===============================") 
        print(f"{self.mensage3}") 
        print("=======================================================================") 
        print(f"======={self.mensage1}=======")
        print("=======================================================================")
        print(f"Mensagem Sistema  :{self.mensage2}")
        
        
        
        return 
    
    def telamensagens(self,mensagemjogo1,mensagemjogo2,mensagemjogo3):
        
        self.mensage1 = mensagemjogo1
        self.mensage2 = mensagemjogo2
        self.mensage3 = mensagemjogo3
        Tela.telainicial(self)
        return  