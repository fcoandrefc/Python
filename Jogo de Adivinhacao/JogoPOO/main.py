from tela import Tela
from menuinicial import Menuinicial
from jogo import Jogo
import os

intervalos = 0
resposta = ""

while True:
    
  minhatela = Tela(" "," ","")
  minhatela.telainicial()
  meumenu = Menuinicial(" "," ")
  meujogo = Jogo(meumenu.numero)
  meujogo.jogoiniciar()
  if meujogo.respostainicialzar == "sair":
    os.system('cls') or None
    print("Obrigado pela diversão! , Ate a proxima.")
    break
  
  


