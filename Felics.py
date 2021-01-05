import cv2 as cv
import AdjustedBinaryCode as abc
from pixelPosition import left_center_right
from array import array as arr

bin_array_dim = arr("B")
bin_array = arr("B")

file = open("test.bnr", "wb")

path = "Immagini/2.jpg"

img = cv.imread(path)

''' 
ridimensionamento in percentuale
scale_percent = 220 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

dim = (width, height)
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
print(resized.shape)

cv.imshow("Original image", img)
cv.imshow("Resized image", resized)
cv.waitKey(0)
cv.destroyAllWindows()
'''

''' ridimensionamento statico
dim = (200, 200)
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
print(resized.shape)

cv.imshow("Original image", img)
cv.imshow("Resized image", resized)
cv.waitKey(0)
cv.destroyAllWindows()
'''

array = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #conversione in scala di grigi

x, y = array.shape
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



uno = array[0,0]
due = array[0,1]



primo = abc.dec_bin(uno, 8)
bin_array.append(int(str(primo), 2))
secondo = abc.dec_bin(due, 8)
bin_array.append(int(str(secondo), 2))


print("primo = "+str(uno)+" "+str(primo)+" secondo = "+str(due)+" "+str(secondo)+"\n\n"+str(array.shape)+"\n\nP  N1  N2  riga  colonna\n")

indice = 0
result = ''
contatore = 0

for riga in range(0,array.shape[0]):
    for colonna in range(0, array.shape[1]):
        if (indice > 1):
            P = array[riga, colonna]
            if (riga==0): #se siamo nella riga 0
                N1 = array[riga,colonna-1] #primo a sinistra
                N2 = array[riga,colonna-2] #secondo a sinistra
            if (colonna==0): #se siamo nella colonna 0
                N1 = array[riga - 1, colonna]     # sopra
                N2 = array[riga - 1, colonna+1]   # sopra a destra
            if (riga!=0 and colonna!=0):
                N1 = array[riga - 1, colonna]  # sopra
                N2 = array[riga, colonna - 1]  # sinistra
            print(str(P)+" "+str(N1)+" "+str(N2)+"   "+str(riga)+"   "+str(colonna))
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

