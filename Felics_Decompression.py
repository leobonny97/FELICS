import AdjustedBinaryCode as abc
import numpy as np

code = ''
x = 0
y = 0


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
                    print(x)
                    num_bin1 = abc.dec_bin(ord(y1), 8)
                    num_bin2 = abc.dec_bin(ord(y2), 8)
                    y = num_bin1 + num_bin2
                    y = int(y, 2) #numero di colonne
                    print(y)
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
                            print(ord(primo))
                            print(num_bin)
                            array_immagine[0][0] = ord(primo)
                            num_bin = abc.dec_bin(ord(secondo), 8)
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
                                    #facciamo qualcosa

f.close()