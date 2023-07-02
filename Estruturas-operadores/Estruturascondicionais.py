

if int(input("Idade: ")) >= 18 :
   print("Parabens");
else:
   print("cai fora");
    
if 10 <=  int(input("Digite Numero: ")) <= 20:
   print("Dentro");
else:
   print("Fora");

lista1 = [1,2,3,4,5];
lista2 = [1,2,3];

if   len(lista1) > len(lista2):
     print("Maior");
    
elif len(lista2) > len(lista1): 
      print("Menor");
else:
     print("Igual");