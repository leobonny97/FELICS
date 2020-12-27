import GolombRice
class Contesto:
    arr_contesti = []
    arr_contesti_dec = []

    def __init__(self, high, low, p):
        self.high = high
        self.low = low
        self.p = p

    def searchContesti(self, high, low, p):
        delta = int(high - low)
        pos = -1
        for idx, e in enumerate(self.arr_contesti):
            if len(e) == 1:  # allora è un contesto
                if e[0] == delta:  # è il contesto che cercavamo
                    pos = idx
                    #print("Il contesto era già presente (posizione,contesto)")
                    #print(idx, e)
                    break

        if pos != -1:  # è stato trovato il contesto cercato
            array_di_valori1 = self.arr_contesti[pos + 1]   #aggioro i valori
            for k in range(4):
                if p < low:
                    length = len(GolombRice.golomb_rice(low - p - 1, k))
                    array_di_valori1[k] = array_di_valori1[k] + length
                elif p > high:
                    length = len(GolombRice.golomb_rice(p - high - 1, k))
                    array_di_valori1[k] = array_di_valori1[k] + length

            self.arr_contesti[pos + 1] = array_di_valori1  #aggiorno l'array di contesto
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
            Contesto.addContestoeValori(self, high, low, p)
            k = 2
            return k

    def addContestoeValori(self, high, low, p):
        arr_valori = []
        delta = int(high-low)
        for k in range(4):
            if p < low:
                arr_valori.append(len(GolombRice.golomb_rice(low - p - 1, k)))
            elif p > high:
                arr_valori.append(len(GolombRice.golomb_rice(p - high - 1, k)))
        self.arr_contesti.append([delta])
        self.arr_contesti.append(arr_valori)
        #print(self.arr_contesti)


    def searchContestiDec(self, high, low, code):
        delta = int(high - low)
        pos = -1
        for idx, e in enumerate(self.arr_contesti_dec):
            if len(e) == 1:  # allora è un contesto
                if e[0] == delta:  # è il contesto che cercavamo
                    pos = idx
                    #print("Il contesto era già presente (posizione,contesto)")
                    #print(idx, e)
                    break

        if pos != -1:  # è stato trovato il contesto cercato
            array_di_valori1_dec = self.arr_contesti_dec[pos + 1]   #aggioro i valori
            for k in range(4):
                if code[0] == 1:
                    if code[1] == 0:
                        length = len(GolombRice.decompression_golomb_rice(low - code - 1, k))
                        array_di_valori1_dec[k] = array_di_valori1_dec[k] + length
                    else:
                        length = len(GolombRice.decompression_golomb_rice(code - high - 1, k))
                        array_di_valori1_dec[k] = array_di_valori1_dec[k] + length

            self.arr_contesti_dec[pos + 1] = array_di_valori1_dec  #aggiorno l'array di contesto
            #print("L'array del contesto già presente aggiornato con somma cumulativa è:")
            #print(array_di_valori1)
            min = array_di_valori1_dec[0]
            k = 0
            for idx2, t in enumerate(array_di_valori1_dec):
                if min > t:
                    min = t
                    k = idx2
            #print("Il k che ritorno è:")
            #print(k)
            return k
        else: #non c'è il contesto cercato, lo aggiungo e restituisco k=2
            #print("il contesto non è presente, lo aggiungo")
            Contesto.addContestoeValoriDec(self, high, low, code)
            k = 2
            return k

    def addContestoeValoriDec(self, high, low, code):
        arr_valori_dec = []
        delta = int(high - low)
        for k in range(4):
            if code[0] == 1:
                if code[1] == 0:
                    arr_valori_dec.append(len(GolombRice.decompression_golomb_rice(low - code - 1, k)))
                else:
                    arr_valori_dec.append(len(GolombRice.decompression_golomb_rice(code - high - 1, k)))
        self.arr_contesti_dec.append([delta])
        self.arr_contesti_dec.append(arr_valori_dec)
        # print(self.arr_contesti)
    '''
    def contestoDecodificatore(self, high, low, p):
        delta = int(high - low)
        pos = -1
        for idx, e in enumerate(self.arr_contesti):
            if len(e) == 1:  # allora è un contesto
                if e[0] == delta:  # è il contesto che cercavamo
                    pos = idx
                    break
        k=-1
        if pos != -1:  # è stato trovato il contesto cercato
            array_di_valori = self.arr_contesti[pos + 1]
            min = array_di_valori[0]

            for idx2, t in enumerate(array_di_valori):
                if min > t:
                    min = t
                    k = idx2
            return k
        else:  # non c'è il contesto cercato, non posso decodificare
            return k
    '''

    def getArray(self):
        return self.arr_contesti