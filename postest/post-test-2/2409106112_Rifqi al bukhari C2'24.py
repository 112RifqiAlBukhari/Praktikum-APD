# identitas
nama_1 = input("masukkan nama anda : ")
nim_2 = input("masukkan nim anda : ")
# mobil yang tersedia ada tesla,toyota,hyundai.
# harga semua mobil
harga_real = int(input("masukkan harga : "))
# harga diskon  setiap mobil
harga_diskon_tesla= 17/100
harga_diskon_toyota= 21/100
harga_diskon_hyundai= 23/100
# harga mobil setelah diskon
harga_mobil_tesla = harga_real-int(harga_diskon_tesla*harga_real)
harga_mobil_toyota = harga_real-int(harga_diskon_toyota*harga_real)
harga_mobil_hyundai = harga_real-int(harga_diskon_hyundai*harga_real)
# modulus
modulus1 = harga_real%7
print(f"mobil tesla seharga {harga_real} dan di beri diskon 17% menjadi {harga_mobil_tesla}")
print(f"mobil toyota {harga_real} dan di beri diskon 21% menjadi {harga_mobil_toyota}")
print(f"mobil hyundai seharga {harga_real} dan di beri diskon 23% {harga_mobil_hyundai}")
print(F"dan {harga_real} modulus 7 adalah {modulus1}")