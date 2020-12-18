import cv2 as cv

def decimale_binario(n):

    b = ""
    while n>0:
        if n%2==0:
            b="0"+b
        else:
            b="1"+b
        n=int(n/2)  #casting in intero

    while len(b)<8:
        b= "0"+b

    return b


path = "Immagini/2.jpg"

img = cv.imread(path)

''' ridimensionamento in percentuale
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

uno = array[0,0]
due = array[0,1]

primo = decimale_binario(uno)
secondo = decimale_binario(due)

print("primo = "+str(uno)+" "+str(primo)+" secondo = "+str(due)+" "+str(secondo)+"\n\n"+str(array.shape)+"\n\nP  N1  N2  riga  colonna\n")

indice = 0
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



            # INSERIRE QUI LA PARTE DI FRANCESCO



        else:
            indice = indice + 1

