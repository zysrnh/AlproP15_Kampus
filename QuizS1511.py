def luas(s):
    if s <= 0:
        return "Nilai tidak valid"
    else:
        return 0.5 * (s/4) * (s/4)

s = float(input("Masukkan nilai sisi segitiga sama kaki: "))
print(luas(s))