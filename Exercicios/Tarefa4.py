# 1
x = 1
while x <=10:
    print(x)
    x += 1

#2
for n in range(1,11):
    print(n)

#3
x = 1
total = 0
while x <= 100:
    total += x
    x += 1
print(total)

#4
total = 0
for x in range(0,100):
    x += 1
    total += x
print(total)

#5
x= 0
while x <= 20:
  x +=1
  if x % 2 == 0:
    print(x)

#6
for x in range(1,21):
    x += 1
    if x % 2 == 0:
      print(x)

#7
nome = str(input("Digite palavra:"))
nomeinvert = ""
x = len(nome) -1
while x >= 0:
  nomeinvert +=(nome[x])
  x -= 1
print(nomeinvert)

#8
nome = str(input("Digite palavra:"))
nomeinvert = ""
for x in nome:
 nomeinvert = x + nomeinvert
if nome == nomeinvert:
  print("Palíndromo")
else: 
 print("Não é palíndromo")

#9
x = 0
while True:
  
  if (x ** 2) > 1000:
    print(f"Quadrado de {x} = {x**2}")
    break
  else:
    x += 1

# 10
lista = ["Flamengo", "Fortaleza", "Andre","Valdenia"]
for x in list(reversed(lista)):
  print(x)