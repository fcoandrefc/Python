from tela import Tela
minhatela = Tela("","","")

class Menuinicial:
    
    
    
    import os
    
    def __init__(self,mensagem1,mensagem2):
        self.numero = self.testadados()
        self.mensagem1 = mensagem1
        self.mensagem2 = mensagem2
        
        
        
    
    def testadados(self):
        
      minhatela.telamensagens("==| Digite o limite Inferior do intervalo de numeros  |==","","")
 
             
      while True:
        
       numerodados =  input("=======> :")
 
       if numerodados.isdigit():
         dificudadeinicial = int(numerodados)
         
         if dificudadeinicial < 0:
             minhatela.telamensagens(self.mensagem1,"","")
         else:
             break
         
       else:
          minhatela.telamensagens("","","")
   
   # ----
 
      minhatela.telamensagens("==| Digite o limite superior do intervalo de numeros  |==","","")
 
      while True:
 
        dificudadeint = input("=======> :")
  
        if dificudadeint.isdigit():
           dificudadefinal = int(dificudadeint)
         
           if dificudadefinal <= dificudadeinicial :
             minhatela.telamensagens("|Digite numero maior que o numero anterior |","========================================================","")
           else:
             break
        else:
            minhatela.telamensagens("|Digite numero inteiro|","===================================================","")
   
   # -----    
   
      minhatela.telamensagens("===========| Digite o numero de tentativas |=============","","")

      while True:
 
       tentativasint = input("=======> :")
  
       if tentativasint.isdigit():
        tentativas = int(tentativasint)
         
        if tentativas < 1  :
           minhatela.telamensagens("|Digite numero maior |","===================================================","")
        else:
           break
       
       else:
         minhatela.telamensagens("|Digite numero inteiro|","===================================================","")
  
      return dificudadeinicial, dificudadefinal, tentativas 
       
          
          