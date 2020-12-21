from GolombRice import golomb_rice
import Context
from AdjustedBinaryCode import adjusted_binary_codeCod


def left_center_right(h, l, p):
    result = ""
    if p < l:
        contesto = Context.Contesto(h, l, p)
        k = contesto.searchContesti(h, l, p)
        result = result + '10' + golomb_rice(l-p-1, k)
    elif p > h:
        contesto = Context.Contesto(h, l, p)
        k = contesto.searchContesti(h, l, p)
        result = result + '11' + golomb_rice(p-h-1, k)
    else:   #sei al centro
        result = result + '0' + adjusted_binary_codeCod(h, l, p)
    return result
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
