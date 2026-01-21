def tampilkan_xT():
    xT = []
    awal = -12
    for i in range(5):
        while True:
            nilai = int(input(f"Masukkan nilai xT ke-{i+1} (antara -16 sampai 16 dan harus {awal}): "))
            if -16 < nilai <= 16 and nilai == awal:
                xT.append(nilai)
                awal += 4
                break
            else:
                print("Out Of Range")
    print(*xT)

tampilkan_xT()