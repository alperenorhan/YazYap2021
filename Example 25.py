# Klavyeden girilen N sayısına göre 1 den N ye kadar olan tek sayıların toplamı ve çarpımını, çift sayıların ise karelerinin toplamını bulan programı kodlayınız.

nSayisi = int(input("N sayısını giriniz: "))

toplam = 0
carpim = 1
kareToplam = 0

for i in range(0, nSayisi+1):
    toplam += i

for i in range(1, nSayisi+1):
    carpim *= i

for i in range(0, nSayisi+1):
    kareToplam += (i*i)

print("N'e kadar olan sayıların toplamı :", toplam)
print("N'e kadar olan sayıların çarpımı :", carpim)
print("N'e kadar olan sayıların karelerinin toplamı :", kareToplam)
