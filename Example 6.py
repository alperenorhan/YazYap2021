# Yaşı girilen kişinin yaşı 18 veya 18'den büyük ise ehliyet alabilirsiniz yazdıran programı kodlayınız.

kullaniciYas = int(input("Yaş Giriniz: "))
if kullaniciYas <= 0:
    print("Geçersiz yaş girdiniz.")
elif kullaniciYas < 18:
    print("Ehliyet alamazsınız.")
else:
    print("Ehliyet alabilirsiniz.")
