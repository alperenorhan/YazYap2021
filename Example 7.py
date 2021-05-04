# 100 üzerinden girilen notu, 5'lik sisteme çeviren programı kodlayınız.

kullaniciNot = int(input("Notunuzu Giriniz: "))

if 85 <= kullaniciNot < 100:
    print("5")
elif 70 <= kullaniciNot < 85:
    print("4")
elif 60 <= kullaniciNot < 70:
    print("3")
elif 45 <= kullaniciNot < 60:
    print("2")
elif 0 <= kullaniciNot < 45:
    print("1")
else:
    print("Geçersiz Not Girdiniz.")
