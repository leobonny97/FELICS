def decompression_golomb_rice(code, k):
    m = 2 ** k
    c = 0
    while code[c] =='1':
        c = c +1
    decode1 = c * m
    print('La prima parte del codice equivale a ' + str(decode1))

    decode2 = 0
    esponente = 0
    c2=len(code)-1
    while c2 > c:
        if code[c2] == '1':
            decode2 = decode2 + 2**esponente
        esponente = esponente + 1
        c2 = c2 - 1


    print('La seconda parte del codice equivale a ' + str(decode2))

    decode = decode1 + decode2
    print("Il valore decompressato equivale a " + str(decode))
    return decode

def golomb_rice(n, k):
    m = 2 ** k
    #print("Il valore m equivale a: ")
    #print(m)

    ris = int(n / m)
    #print("Il valore di n/m equivale a: ")
    #print(ris)

    code1 = ''

    while ris > 0:
        code1 = code1 + '1'
        ris = ris - 1
    code1 = code1 + '0'
    #print("Il valore in unario corrisponde a: ")
    #print(code1)

    mod = n % m
    #print("Il resto di n/m equivale a: ")
    #print(mod)

    code2 = ''
    while mod > 0:
        if mod % 2 == 0:
            code2 = '0' + code2
        else:
            code2 = '1' + code2
        mod = int(mod / 2)

    while len(code2) < k:
        code2 = '0' + code2


    #print("Il resto in binario corrisponde a: ")
    #print(code2)

    code1 = code1 + code2
    return code1