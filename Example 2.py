# Kısa kenar uzunluğu ve uzun kenar uzunluğu kullanıcıdan alınan bir dikdörtgenin çevresini ve alanını hesaplayan programı kodlayınız.

kisaKenar = int(input("Kısa Kenar Uzunluğunu Giriniz: "))
uzunKenar = int(input("Uzun Kenar Uzunluğunu Giriniz: "))

print("----------------------------------")

cevre = 2 * (kisaKenar + uzunKenar)
alan = kisaKenar * uzunKenar

print("Dikdörtgenin Çevresi:", cevre)
print("Dikdörtgenin Alanı:", alan)
