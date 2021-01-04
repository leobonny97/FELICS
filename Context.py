import GolombRice

arr_contesti = []
arr_contesti_dec = []



def searchContesti(high, low, p):
    delta = int(high - low)
    pos = -1
    for idx, e in enumerate(arr_contesti):
        if len(e) == 1:  # allora è un contesto
            if e[0] == delta:  # è il contesto che cercavamo
                pos = idx
                #print("Il contesto era già presente (posizione,contesto)")
                #print(idx, e)
                break

    if pos != -1:  # è stato trovato il contesto cercato
        array_di_valori1 = arr_contesti[pos + 1]   #aggioro i valori
        for k in range(4):
            if p < low:
                length = len(GolombRice.golomb_rice(low - p - 1, k))
                array_di_valori1[k] = array_di_valori1[k] + length
            elif p > high:
                length = len(GolombRice.golomb_rice(p - high - 1, k))
                array_di_valori1[k] = array_di_valori1[k] + length

        arr_contesti[pos + 1] = array_di_valori1  #aggiorno l'array di contesto
        #print("L'array del contesto già presente aggiornato con somma cumulativa è:")
        #print(array_di_valori1)
        min = array_di_valori1[0]
        k = 0
        for idx2, t in enumerate(array_di_valori1):
            if min > t:
                min = t
                k = idx2
        #print("Il k che ritorno è:")
        #print(k)
        return k
    else: #non c'è il contesto cercato, lo aggiungo e restituisco k=2
        #print("il contesto non è presente, lo aggiungo")
        addContestoeValori(high, low, p)
        k = 2
        return k

def addContestoeValori(high, low, p):
    arr_valori = []
    delta = int(high-low)
    for k in range(4):
        if p < low:
            arr_valori.append(len(GolombRice.golomb_rice(low - p - 1, k)))
        elif p > high:
            arr_valori.append(len(GolombRice.golomb_rice(p - high - 1, k)))
    arr_contesti.append([delta])
    arr_contesti.append(arr_valori)
    #print(self.arr_contesti)

def searchContesti_dec( high, low, code):
    delta = int(high - low)
    pos = -1
    aggiornare = False
    for idx, e in enumerate(arr_contesti_dec):
        if len(e) == 1:  # allora è un contesto
            if e[0] == delta:  # è il contesto che cercavamo
                pos = idx
                break

    if pos != -1:  # è stato trovato il contesto cercato
        array_di_valori1_dec = arr_contesti_dec[pos + 1]  # recupero i valori
        min = array_di_valori1_dec[0]
        k = 0
        for idx2, t in enumerate(array_di_valori1_dec):
            if min > t:
                min = t
                k = idx2  # ritorno la posizione del minimo, ovvero il k
        aggiornare = True
        return k, aggiornare
    else:  # non c'è il contesto cercato, lo aggiungo e restituisco k=2
        # print("il contesto non è presente, lo aggiungo")
        #addContestoeValori_dec(high, low, code)
        k = 2
        return k, aggiornare

def aggiornaContesto_dec(high, low, p):
    delta = int(high - low)
    pos = -1
    for idx, e in enumerate(arr_contesti_dec):
        if len(e) == 1:  # allora è un contesto
            if e[0] == delta:  # è il contesto che cercavamo
                pos = idx
                break

    if pos != -1:  # è stato trovato il contesto cercato
        array_di_valori1_dec = arr_contesti_dec[pos + 1]  # prendo i valori i valori
        for k in range(4):
            if p < low:
                length = len(GolombRice.golomb_rice(low - p - 1, k))
                array_di_valori1_dec[k] = array_di_valori1_dec[k] + length
            elif p > high:
                length = len(GolombRice.golomb_rice(p - high - 1, k))
                array_di_valori1_dec[k] = array_di_valori1_dec[k] + length

        arr_contesti_dec[pos + 1] = array_di_valori1_dec

def addContestoeValori_dec( high, low, p):
    arr_valori_dec = []
    delta = int(high-low)
    for k in range(4):
        if p < low:
            arr_valori_dec.append(len(GolombRice.golomb_rice(low - p - 1, k)))
        elif p > high:
            arr_valori_dec.append(len(GolombRice.golomb_rice(p - high - 1, k)))
    arr_contesti_dec.append([delta])
    arr_contesti_dec.append(arr_valori_dec)
    #print("array"+str(arr_valori_dec))
