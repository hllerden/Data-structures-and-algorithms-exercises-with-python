print("hello world")

ana_para= float(80_000)
gunluk_kar= float(.005)  #yüzde 1 olarak
gun=365*5

def kazanc(ana_para,gunluk_kar,gun):

    for i in range(1,gun+1):
        ana_para = ana_para + (ana_para *(gunluk_kar))
        print(" ",i,". gün kazancınız.",ana_para/20)

kazanc(ana_para,gunluk_kar,gun)