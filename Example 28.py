# a-b arası tek sayıların toplamını ve ortalamasını bulan programı kodlayınız.

a = int(input("a sayısını giriniz: "))
b = int(input("b sayısını giriniz: "))

toplam = 0
sayiMiktari = abs(a-b)-1

for i in range(a+1, b):
    toplam += i

ortalama = toplam / sayiMiktari

print("Aradaki sayıların toplamı:", toplam)
print("Aradaki sayıların ortalaması:", ortalama)
