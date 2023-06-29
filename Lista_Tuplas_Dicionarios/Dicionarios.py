meuDicioanrio = {"nome"        :"Andre",
                 "sobrenome"   : "Felix",
                 "anos"        : 51
                 }
print(meuDicioanrio);

frutaDicioanrio = {
    "maca" : 3 ,
    "banana" : 4,
    "uva" : 5       
}

frutaDicioanrio["maca"] = 8;

print(frutaDicioanrio["maca"]);

animaisDicioanrio = {};

aluno = {
    "nome"    : "Andre",
    "idade"   : 51,
    "hobbies" : ['jogar', 'comer']
}
print(aluno)
print(aluno["hobbies"][1]);

print(aluno.get("nome"));
print(aluno.get("nomes", "erro"));

aluno.pop("idade");
print(aluno);

print(aluno.keys());
print(aluno.values());
print(aluno.items());
