import math

def dec_bin(n,m):

    b = ""
    while n>0:
        if n%2==0:
            b="0"+b
        else:
            b="1"+b
        n=int(n/2)  #casting in intero

    while len(b)<m:
        b= "0"+b

    return b

def adjusted_binary_codeCod(H,L,P):

    delta = H - L
    if delta==0:            #se H,L,P sono tutti uguali
        k = math.log(2, 2)
    else:
        k = math.log(delta + 1, 2)
    potenza_di_due = k.is_integer()
    k = int(k)
    a = (2**(int(k)+1))-(delta + 1)
    b = 2*(delta + 1 - 2**int(k))

    if potenza_di_due == True:
        start = L
        for i in range (0,delta+1):
            #print(start)
            if P == start:
                #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
                return dec_bin(i, k)
            else:
                start = start + 1
    else:

        '''se stiamo al centro'''
        start = H - int(b/2)
        for i in range(1,a+1):
            n = 2**k - i
            #print(start)
            if P == start:
                #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
                return dec_bin(n,k)
            else:
                start = start - 1

        '''se stiamo sopra'''
        start = L
        for l in range(0,int(b/2)):
            #print(start)
            if P == start:
                #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
                return dec_bin(l,k+1)
            start = start + 1

        '''se stiamo sotto'''
        start = H
        for t in range(int(b/2), b):
            #print(start)
            if P == start:
                #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
                return dec_bin(t, k+1)
            start = start - 1

def adjusted_binary_codeDec(H,L,B):

    delta = H - L
    if delta==0:            #se H,L,P sono tutti uguali
        k = math.log(2, 2)
    else:
        k = math.log(delta + 1, 2)
    potenza_di_due = k.is_integer()
    k = int(k)
    a = (2**(int(k)+1))-(delta + 1)
    b = 2*(delta + 1 - 2**int(k))

    if potenza_di_due == True:
        sottostringaB = B[0:k]
        num = int(sottostringaB, base=2)
        #print(B)
        #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
        return num + L
    else:

        '''se stiamo al centro'''
        start = H - int(b/2)
        for i in range(1,a+1):
            n = 2**k - i
            d = dec_bin(n,k)
            sottostringaB = B[0:k]
            #print(d)
            if sottostringaB == d:
                #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
                return start
            else:
                start = start - 1

        '''se stiamo sopra'''
        start = L
        for l in range(0,int(b/2)):
            d = dec_bin(l,k+1)
            sottostringaB = B[0:k+1]
            #print(d)
            if sottostringaB == d:
                #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
                return start
            else:
                start = start + 1

        '''se stiamo sotto'''
        start = H
        for t in range(int(b/2), b):
            d = dec_bin(t, k+1)
            sottostringaB = B[0:k+1]
            #print(d)
            if sottostringaB == d:
                #print("delta = " + str(delta) + " a = " + str(a) + " b = " + str(b) + " k = " + str(k))
                return start
            else:
                start = start - 1

'''
H = 24
L = 15
P = 20
print("CODIFICA")
B = adjusted_binary_codeCod(H,L,P)
print(B)
print("\nDECODIFICA")
D = adjusted_binary_codeDec(H,L,B)
print(D)
'''

