def hitung_aT():
    aT=input("Masukan Nila aT: ")
    if aT.isdigit():
        aT=int(aT)%20
        print("Hasil aT:", aT)
    else:
        print("Out of Range")
hitung_aT()