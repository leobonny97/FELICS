from GolombRice import golomb_rice, decompression_golomb_rice
import Context
from AdjustedBinaryCode import adjusted_binary_codeCod, adjusted_binary_codeDec


def left_center_right(h, l, p):
    result = ""
    if p < l:
        k = Context.searchContesti(h, l, p)
        result = result + '10' + golomb_rice(l-p-1, k)
    elif p > h:
        k = Context.searchContesti(h, l, p)
        result = result + '11' + golomb_rice(p-h-1, k)
    else:   #sei al centro
        result = result + '0' + adjusted_binary_codeCod(h, l, p)
    return result



def left_center_rightDec(h, l, code):
    if code[0] == '1':
        if code[1] == '0':
            print("sono in 10")
            #print(code)
            code = code[2:]
            k,aggiornare = Context.searchContesti_dec(h,l,code)
            #print("k = "+str(k))
            result,code = decompression_golomb_rice(code, k)
            result = l - result - 1 #p<l
            if aggiornare == True:
                Context.aggiornaContesto_dec(h, l, result) #result = p
            else: #devo aggiungere il contesto
                Context.addContestoeValori_dec(h, l, result) #result = p
        else:
            print("sono in 11")
            #print(code)
            code = code[2:]
            k,aggiornare = Context.searchContesti_dec(h, l, code)
            #print("k = " + str(k))
            result,code = decompression_golomb_rice(code, k)
            result = result + h + 1 #p>h
            if aggiornare == True:
                Context.aggiornaContesto_dec(h, l, result)  # result = p
            else:  # devo aggiungere il contesto
                Context.addContestoeValori_dec(h, l, result)  # result = p
    elif code[0] == '0':   #sei al centro
        print("sono in 0")
        #print(code)
        code = code[1:]
        result,code = adjusted_binary_codeDec(h, l, code)
    return result,code


'''
p = 180
l = 120
h = 150

p1 = 110
l1 = 120
h1 = 150

p2 = 140
l2 = 120
h2 = 150

risultato=""

risultato += left_center_right(h, l, p)
risultato += left_center_right(h1, l1, p1)
risultato += left_center_right(h2, l2, p2)
print("Il risultato e': ")
print(risultato)
'''
