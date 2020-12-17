from GolombRice import golomb_rice
import Context
from AdjustedBinaryCode import adjusted_binary_codeCod


def left_center_right(h, l, p):
    result = ""
    if p < l:
        print("")
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

p = 180
l = 120
h = 150

risultato = left_center_right(h, l, p)
print("Il risultato e': ")
print(risultato)