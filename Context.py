import GolombRice
class Contesto:
    arr_contesti = []

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
                    print(idx, e)
                    break

        if pos != -1:  # è stato trovato il contesto cercato
            array_di_valori1 = self.arr_contesti[pos + 1]   #aggioro i valori
            array_di_valori2 = self.arr_contesti[pos + 1]   #aggiorno i valori
            array_di_valori_sum = [x+y for x, y in zip(array_di_valori1,array_di_valori2)]  #creo l'array sommato
            self.arr_contesti[pos + 1] = array_di_valori_sum #aggiorno l'array di contesto
            print(array_di_valori_sum)
            min = array_di_valori_sum[0]
            k = 0
            for idx2, t in enumerate(array_di_valori_sum):
                if min > t:
                    min = t
                    k = idx2
            return k
        else: #non c'è il contesto cercato, lo aggiungo e restituisco k=2
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


    def getArray(self):
        return self.arr_contesti