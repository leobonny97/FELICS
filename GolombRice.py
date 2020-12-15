def decompression_golomb_rice(nbin, k):
    m = 2 ** k
    c = 0
    while nbin[c] =='1':
        c = c +1
    decode1 = c * m
    print('La prima parte del codice equivale a ' + str(decode1))

    decode2 = 0
    esponente = 0
    c2=len(nbin)-1
    while c2 > c:
        if nbin[c2] == '1':
            decode2 = decode2 + 2**esponente
        esponente = esponente + 1
        c2 = c2 - 1


    print('La seconda parte del codice equivale a ' + str(decode2))

    decode = decode1 + decode2
    print("Il valore decompressato equivale a " + str(decode))
    return decode

def golomb_rice(n, k):
    m = 2 ** k
    print("Il valore m equivale a: ")
    print(m)

    ris = int(n / m)
    print("Il valore di n/m equivale a: ")
    print(ris)

    code1 = ''

    while ris > 0:
        code1 = code1 + '1'
        ris = ris - 1
    code1 = code1 + '0'
    print("Il valore in unario corrisponde a: ")
    print(code1)

    mod = n % m
    print("Il resto di n/m equivale a: ")
    print(mod)

    code2 = ''
    while mod > 0:
        if mod % 2 == 0:
            code2 = '0' + code2
        else:
            code2 = '1' + code2
        mod = int(mod / 2)

    while len(code2) < k:
        code2 = '0' + code2


    print("Il resto in binario corrisponde a: ")
    print(code2)

    code1 = code1 + code2
    return code1


p = 180
l = 120
h = 150
k = 4
code = '1'
if p < l:
    code = code + '0' + golomb_rice(l-p-1, k)
elif p > h:
    code = code + '1' + golomb_rice(p-h-1, k)

print("La codifica completa equivale a: ")
print(code)


if code[0] == '1':
    decode = decompression_golomb_rice(code[2:],k)
    if code[1] == '0':
        decode = l - (decode + 1)
        print("Il valore originale del pixel corrisponde a " + str(decode))
    elif code[0] == '1':
        decode = h + (decode + 1)
        print("Il valore originale del pixel corrisponde a " + str(decode))