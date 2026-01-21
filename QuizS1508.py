def tampilkan_qR():
    qR=[12,-0.5,-2,1.75,0.5,-13]
    print(qR)
    temp=qR[0]
    qR[0]=qR[4]
    qR[4]=qR[2]
    qR[2]=temp
    print(qR)
tampilkan_qR()