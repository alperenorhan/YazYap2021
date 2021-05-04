# Klavyeden 2 sayı girilecek. Daha sonra işlem numarası girilecek.Ggirilen işlem numarasına göre işlemi yapacak ve sonucu ekranda görüntüleyecek programı kodlayınız.

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

toplamaNo = 1
cikarmaNo = 2
carpmaNo = 3
bolmeNo = 4
sonuc = 0

print("Toplama İşlemi : 1, Çıkarma İşlemi : 2, Çarpma İşlemi : 3, Bölme İşlemi : 4")
islemNo = int(input("İşlem numarasını giriniz: "))

if islemNo == 1:
    sonuc = sayi1 + sayi2
    print("İşlem Sonucu :", sonuc)
elif islemNo == 2:
    sonuc = sayi1 - sayi2
    print("İşlem Sonucu :", sonuc)
elif islemNo == 3:
    sonuc = sayi1 * sayi2
    print("İşlem Sonucu :", sonuc)
elif islemNo == 4:
    sonuc = sayi1 / sayi2
    print("İşlem Sonucu :", sonuc)
else:
    print("Geçersiz işlem numarası girdiniz.")
