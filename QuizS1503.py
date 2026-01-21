aT = [
    [-1,0,-0.5,-3],
    [-3,5,-1,5,-1],
]
zP = [
    [1,7,-4,1.5],
    [0,0,-1,1.5],
]

zL = []
for i in range(len(aT)):
    baris = []
    for j in range(len(aT[0])):
        hasil=aT[i][j] + zP[i][j]
        baris.append(hasil)
    zL.append(baris)
print("Hasil Matriks zL:")
for baris in zL:
    print(baris)