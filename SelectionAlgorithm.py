import Context

#MAIN
high1 = 150
low1 = 120
p1 = 220

high2 = 160
low2 = 120
p2 = 220

high3 = 150
low3 = 120
p3 = 220

contesto = Context.Contesto(high1, low1, p1)
k = contesto.searchContesti(high1, low1, p1)

contesto2 = Context.Contesto(high2, low2, p2)
k2 = contesto2.searchContesti(high2, low2, p2)

contesto3 = Context.Contesto(high3, low3, p3)
k3 = contesto3.searchContesti(high3, low3, p3)

array = contesto.getArray()
print("L'array è: ")
print(array)

print("k , k2 e k3 rispettivamente: ")
if(k):

    print("la lunghezza codice più corta è data dal k: ")
    print(k)

if(k2):

    print("la lunghezza codice più corta è data dal k: ")
    print(k2)


if(k3):

    print(array)
    print("la lunghezza codice più corta è data dal k: ")
    print(k3)


#lato decodificatore, dato il contesto ritorna il k
paramtro_k_decodificatore = contesto.contestoDecodificatore(high1, low1, p1)  #richiamo e passo il contesto 1
if paramtro_k_decodificatore != -1:
    print("Il parametro k decodificato è:")
    print(paramtro_k_decodificatore)
else:
    print("non sono stato in grado di decodificare il k")