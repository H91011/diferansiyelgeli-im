import numpy as np
from builtins import print

Np=5 # polulasyon büyüklüğü
Gmax=50 # generasyon sayısı
CR=0.75 # caprazlama oranı
F=0.65 # Ölçekleme Faktörü
D=2 # araştırma uzayının boyutu

x1=0
x2=0
kalite=np.zeros((5), dtype=np.float)


# Kalite degeri bulma fonksiyonu
def Fonkisyon(x1,x2):
    Fnk=100*(x1**2-x2)**2+(1-x1)**2
    return Fnk
# Başlangıç Populasyonunu üreten fonksiyon
def BaslangıcPop():
    x = np.random.randint(-4,4,(5,2,1))
    y = np.random.random((5,2,1))

    global Populasyon
    Populasyon= x+y
    return print(Populasyon)


# Kalite Degeri üretim Fonksiyonu
def KaliteUretim():
    for i in range(0,5):
        deger=Populasyon[i]
        kalite[i]= Fonkisyon(deger[0],deger[1])
    return

# Mutasyon ve seçim yapılan fonksiyon
def SecimMutasyon():
    randomSayi=np.random.random(1)
    yeniGenerasyon = np.zeros((2,1), dtype=np.float)
    rakip=0
    diger1=0;
    diger2=0;

    for i in range(0,4):

        while (i!=rakip): # Yarıştırılacak olanın seçimi
            rakip=np.random.randint(0,5,(1))

            while((diger1!=i) & (diger1!=rakip)):# Diger birinin seçimi
                diger1=np.random.randint(0,5,(1))
                while ((diger1!=i) & (diger1!=rakip) & (diger2!=diger1)):# Diger ikincisinin seçimi

                    diger2 = np.random.randint(0, 5, (1))

        mutasyonaugrayan=Populasyon[rakip]+F*(Populasyon[diger1]-Populasyon[diger2])

        if(randomSayi<CR):
            yeniGenerasyon[0]=mutasyonaugrayan[0][0]
        else:
            yeniGenerasyon[0]=Populasyon[i][0]
        if(randomSayi>CR):
            yeniGenerasyon[0][1] = mutasyonaugrayan[0][1]
        else:
            yeniGenerasyon[1] = Populasyon[i][1]

        yenigenerasyonKaliteDegeri=Fonkisyon(yeniGenerasyon[0],yeniGenerasyon[1])

        if(kalite[i]<yenigenerasyonKaliteDegeri):
            Populasyon[i]=yeniGenerasyon


    return print(Populasyon)


BaslangıcPop()
print("########")
KaliteUretim()
SecimMutasyon()
