def tampilkan_zX():
    zX = []
    awal = -14
    for i in range(5):
        while True:
            nilai = int(input(f"Masukkan nilai zX ke-{i+1} (antara -14 sampai 14 dan harus {awal}): "))
            if -14 <= nilai <= 14 and nilai == awal:
                zX.append(nilai)
                awal += 3
                break
            else:
                print("Out Of Ranger")
    for nilai in zX:
        print(nilai)

tampilkan_zX()