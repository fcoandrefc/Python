n1 = int(input("Digite Primento numero inteiro: "));
n2 = int(input("Digite Segundo numero inteiro: "));

print(n1 + n2);
print(n1 - n2);
print(n1 * n2);
print(n1 / n2);

temperatura = int(input("Digite a Temperatura graus Celsius: "));
if temperatura > 100:
  print("A agua está fervendo!");
  
  
n3 = int(input("Digite numero inteiro: "));
if (n3 % 2 == 0):
  print("Numero Par")
else:
  print("Numero Impar");

senha = input("Digite senha: ");
if senha == "123456":
  print("Senha Correta")
else:
  print("Senha Errada");
  
  

idade = int(input("Digite sua Idade: "));
if 18 <= idade <=30:
  print("Esta entre 18 e 30")
else:
  print("Nao esta em 18 e 30");
  
n4 = int(input("Digite 1 numero inteiro: "));
n5 = int(input("Digite 2 numero inteiro: "));
n6 = int(input("Digite 3 numero inteiro: "));

if n4 >= 0 or n5 >= 0 or n6 >= 0:
    print ("Tem numero positivo")
else:
    print("Não tem numero positivo");
    
letra = input("Digite uma letra:");  
Listavogais =["a","e","i","o","u"];
if letra in Listavogais:
   print("Letra e um vogal!")
else:
    print("Letra não e uma vogal") ;
    
n7 = int(input("Digite numero inteiro: "));
if n7 > 0:
  print("Numero Positivo")
elif n7<0:
  print("Numero negativo")
else:
   print("Numero zero");

n8 = int(input("Digite 1 numero inteiro: "));
n9 = int(input("Digite 2 numero inteiro: "));
n10 = int(input("Digite 3 numero inteiro: "));

if n9 < n8 or n10 < n8:
  print("Numero fora da order crescente")
else:
   print("Numero na ordem crescente");


n11 = int(input("Digite numero inteiro: "));

if (n11 % 3 == 0) and (n11 % 5 == 0) :
  print("Numero mutiplo de 3 e 5")
else:
  print("Numero nao é mutiplo de 3 e 5");





    

  