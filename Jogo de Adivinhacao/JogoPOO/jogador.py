class Jogador:
 
 
 
 
 def __init__(self,dicionario):
  
  self.dicionario = dicionario

 def gardarjogador(self,numero1,numero2):
     listajogador = {} 
          
     jogadornome = input()
     totalponto = (numero1 / numero2)
     listajogador[jogadornome] ={"Nome": jogadornome, "Pontos": totalponto}
     self.dicionario = listajogador
     #print(self.dicionario)
     #input("aqi")
     #self.nome = totaljogadores.append(jogadores.copy())
     
     
     