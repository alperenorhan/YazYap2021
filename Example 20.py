# Bir iletkenin kutupları arasındaki gerilim (V) iletkenden geçen amper türünde akım (I) iletken üzerinde var olan direncin (R) çarpımına eşittir. V=I*R formülüyle gösterilir. Formülden faydalanarak kullanıcı tarafından girilen akım ve direnç değerlerine göre iletkenin kutupları arasındaki gerilimi hesaplayan program kodlayınız.

akim = int(input("Akım değerini giriniz: "))
direnc = int(input("Direnç değerini giriniz: "))

V = akim*direnc

print("Gerilim Değeri", V)
