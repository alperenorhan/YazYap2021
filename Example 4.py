# Ham fiyatı ve KDV oranı kullanıcıdan alınan bir ürünün KDV fiyatını ve satış fiyatını gösteren programı kodlayınız.

urunHamFiyat = int(input("Ürünün Ham Fiyatını Giriniz: "))
kdvOran = int(input("KDV Oranını Giriniz: "))

urunKDV = urunHamFiyat * kdvOran / 100
urunToplamFiyat = urunHamFiyat + urunKDV

print("Ürünün KDV'si: ", urunKDV)
print("Ürünün KDV Dahil Fiyatı: ", urunHamFiyat)
