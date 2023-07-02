Frutas =  ["maca","banana", "laranja", "abacaxi", "melancia"];

Frutas.append("uva");
print(Frutas);
Frutas.remove("uva");
print(Frutas);

fruta_selecionada = Frutas[1];
print(fruta_selecionada);


Cores = ("vermelho", "azul", "verde", "amarelo", "roxo");
print(Cores);
cor_selecionada = Cores[2];
print(cor_selecionada);

# tupla e imutavel, não aceita o metodo append.
# Cores.append("laranja");

aluno={"nome": "André",
        "idade": 51,
        "cidade": "Fortaleza"};

print(aluno);

idade_aluno = aluno["idade"];

print(idade_aluno);

aluno["genero"]="masculio";
print(aluno);

aluno.pop("cidade");
print(aluno);



      




