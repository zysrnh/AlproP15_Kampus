
def tampilkan_xT():
    xT = [[-2, 1, 0.5], [-2, 0, 1.5]]
    temp = xT[0][1]
    xT[0][1] = xT[1][2]
    xT[1][2] = temp
    print(xT)

tampilkan_xT()