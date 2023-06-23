listanumeros = [1,2,3,4,5];
listastring = ["a","b","c","d"];
listamista = [1, "a", 3.14, True];

print(listanumeros);
print(listastring);
print(listamista);

frutas = ["maca", "banana", "morango"]

print(frutas[1]);

frutas[1] ="laranja";
print(len(frutas));

listanova=[1,["a", "b"]];

numeros= [1,2,3,4,5,6];
sublista = numeros[1:4];
print(sublista);

frutas = ["maca", "banana", "laranja"];
frutas.append("morango");
frutas.insert(1, "abacaxi");

frutaremovida = frutas.remove("laranja");
frutaremovida = frutas.pop(2);

print(frutas);
print(frutaremovida);

frutasshort = ["maca", "banana", "laranja", "pera", "uva","pitomba", "andre", "val","af", "aaa","bb", "chico", "flamengo"];

frutasshort.sort();

print(frutasshort);


