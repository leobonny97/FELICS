import AdjustedBinaryCode as abc
import numpy as np
from pixelPosition import left_center_rightDec
import matplotlib.pyplot as plt

code = ''
x = 0
y = 0
result = ''

with open("test.bnr", "rb") as f:
    x1 = f.read(1)
    if not x1:
        print("File terminato")
    else:
        x2 = f.read(1)
        if not x2:
            print("File terminato")
        else:
            y1 = f.read(1)
            if not y1:
                print("File terminato")
            else:
                y2 = f.read(1)
                if not y2:
                    print("File terminato")
                else: #Arrivati a questo punto abbiamo letto la dimensione dell'immagine
                    num_bin1 = abc.dec_bin(ord(x1), 8)
                    num_bin2 = abc.dec_bin(ord(x2), 8)
                    x = num_bin1 + num_bin2
                    x = int(x, 2) #numero di righe
                    print("queste sono le righe: "+str(x))
                    num_bin1 = abc.dec_bin(ord(y1), 8)
                    num_bin2 = abc.dec_bin(ord(y2), 8)
                    y = num_bin1 + num_bin2
                    y = int(y, 2) #numero di colonne
                    print("queste sono le colonne: "+str(y))
                    primo = f.read(1)
                    if not primo:
                        print("File terminato")
                    else:
                        secondo = f.read(1)
                        if not secondo:
                            print("File terminato")
                        else: #arrivati a questo punto abbiamo letto il valore dei primi due pixel
                            array_immagine = np.zeros((x, y))
                            num_bin = abc.dec_bin(ord(primo), 8)
                            num_bin1 = num_bin
                            print(ord(primo))
                            print(num_bin)
                            array_immagine[0][0] = ord(primo)
                            num_bin = abc.dec_bin(ord(secondo), 8)
                            num_bin2 = num_bin
                            print(ord(secondo))
                            print(num_bin)
                            array_immagine[0][1] = ord(secondo)
                            while(1):
                                carattere = f.read(1)
                                if not carattere:
                                    print("File terminato")
                                    break
                                else:
                                    num_bin = abc.dec_bin(ord(carattere), 8)
                                    print(ord(carattere))
                                    print(num_bin)
                                    code = code + str(num_bin) #concatenazione delle varie letture
f.close()


indice = 0
print(x)
print(y)
for riga in range(0,x):
    for colonna in range(0,y):
        if (indice > 1):
            if (riga==0): #se siamo nella riga 0
                N1 = array_immagine[riga,colonna - 1] #primo a sinistra
                N2 = array_immagine[riga,colonna - 2] #secondo a sinistra
            if (colonna==0): #se siamo nella colonna 0
                N1 = array_immagine[riga - 1,colonna]       # sopra
                N2 = array_immagine[riga - 1,colonna + 1]   # sopra a destra
            if (riga!=0 and colonna!=0):
                N1 = array_immagine[riga - 1,colonna]   # sopra
                N2 = array_immagine[riga,colonna - 1]   # sinistra
            #print(str(P)+" "+str(N1)+" "+str(N2)+"   "+str(riga)+"   "+str(colonna))
            if N1 >= N2:        #se sono uguali chi è high è indifferente
                high = N1
                low = N2
                #print("H= " + str(high) + " L= " + str(low)+" IL CONTESTO E: "+str(high-low))
            else:
                high = N2
                low = N1
                #print("H= " + str(high) + " L= " + str(low)+" IL CONTESTO E: "+str(high-low))

            #print("high = "+str(high))
            #print("low = "+str(low))
            result,code = left_center_rightDec(high,low,code)
            array_immagine[riga,colonna] = result
            #print(result)
        else:
            indice = indice + 1

plt.imshow(array_immagine)
plt.savefig("Immagini\\prova.jpg")

