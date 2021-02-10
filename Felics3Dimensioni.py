import cv2 as cv
import AdjustedBinaryCode as abc
from pixelPosition import left_center_right
from array import array as arr

bin_array_dim = arr("B")
bin_array = arr("B")

file = open("Test/FELICS/a colori/test20.bnr", "wb")

path = "Immagini/a colori/BMP/20.bmp"

array = cv.imread(path, 1)

x, y, z = array.shape
print(x)
print(y)

x_code = abc.dec_bin(x, 16)
bin_array_dim.append(int(x_code[:8][::+1], 2))
bin_array_dim.append(int(x_code[8:][::+1], 2))

y_code = abc.dec_bin(y, 16)
bin_array_dim.append(int(y_code[:8][::+1], 2))
bin_array_dim.append(int(y_code[8:][::+1], 2))

file.write(bytes(bin_array_dim))

print(x_code)
print(y_code)

print(bin_array_dim)



uno1, uno2, uno3 = array[0,0]
due1, due2, due3 = array[0,1]



primo1 = abc.dec_bin(uno1, 8)
bin_array.append(int(str(primo1), 2))
primo2 = abc.dec_bin(uno2, 8)
bin_array.append(int(str(primo2), 2))
primo3 = abc.dec_bin(uno3, 8)
bin_array.append(int(str(primo3), 2))
secondo1 = abc.dec_bin(due1, 8)
bin_array.append(int(str(secondo1), 2))
secondo2 = abc.dec_bin(due2, 8)
bin_array.append(int(str(secondo2), 2))
secondo3 = abc.dec_bin(due3, 8)
bin_array.append(int(str(secondo3), 2))


#print(str(array.shape)+"\n\nP  N1  N2  riga  colonna\n")

indice = 0
result = ''
contatore = 0

for riga in range(0,array.shape[0]):
    for colonna in range(0, array.shape[1]):
        if (indice > 1):
            for count_comp in range(0, 3):
                P = array[riga, colonna][count_comp]
                if (riga==0): #se siamo nella riga 0
                    N1 = array[riga,colonna-1][count_comp] #primo a sinistra
                    N2 = array[riga,colonna-2][count_comp] #secondo a sinistra
                if (colonna==0): #se siamo nella colonna 0
                    N1 = array[riga - 1, colonna][count_comp]     # sopra
                    N2 = array[riga - 1, colonna+1][count_comp]   # sopra a destra
                if (riga!=0 and colonna!=0):
                    N1 = array[riga - 1, colonna][count_comp]  # sopra
                    N2 = array[riga, colonna - 1][count_comp]  # sinistra
                #print(str(P)+" "+str(N1)+" "+str(N2)+"   "+str(riga)+"   "+str(colonna))
                #PARTE CENTRALE
                if N1 >= N2:        #se sono uguali chi è high è indifferente
                    high = N1
                    low = N2
                else:
                    high = N2
                    low = N1
                result += left_center_right(high, low, P)
                #print(result)
        else:
            indice = indice + 1
        while (len(result) > 8):
            bin_array.append(int(result[:8][::+1], 2))
            result = result[8:]

if len(result) > 0:
    while (len(result) == 8):
        result = result + '0'

bin_array.append(int(result[:8][::+1], 2))

file.write(bytes(bin_array))
file.close()
