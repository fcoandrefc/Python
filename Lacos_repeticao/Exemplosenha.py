
contador = -1;
senhaBloqueada = False;
senha="entrar";
tentativas = 3;

while senha != '123456':
 
  contador += 1;
  if(contador == 3):
    senhaBloqueada = True;
    break;
  elif contador > 0 :
     print(f"falta {tentativas - contador} tentativas")

  senha = input("Digite a senha: ");

if(senhaBloqueada):
  print("Sua senha foi bloqueada!");    
else:
  print("Senha correta!");
