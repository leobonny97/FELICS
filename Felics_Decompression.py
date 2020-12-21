import AdjustedBinaryCode as abc

code = ''

with open("test.bnr", "rb") as f:
    while(1):
        carattere = f.read(1)
        if not carattere:
            print("File terminato")
            break
        else:
            num_bin = abc.dec_bin(ord(carattere), 8)
            print(ord(carattere))
            print(num_bin)
            code = code + str(num_bin)

f.close()