# identitas
nama = input("masukkan nama : ")
# harga mobil
harga_semua_mobil = int(input("masukkann harga : "))
# diskon mobil
diskon_tesla = 17/100
diskon_toyota= 21/100
diskon_hyundai= 23/100
# pilih mobil yang tersedia (tesla,toyota,hyundai)
mobil = input("masukkan nama mobil yang anda mau : ")
if mobil == "tesla" :
        tesla =  int(harga_semua_mobil-(diskon_tesla*harga_semua_mobil))
        print(f"{nama} membeli tesla seharga {tesla} karna sedang diskon 17%")
elif mobil == "toyota" :
         toyota = int(harga_semua_mobil-(diskon_toyota*harga_semua_mobil))  
         print(f"{nama} membeli toyota seharga {toyota} karna sedang diskon 21%")
elif mobil == "hyundai" :
         hyundai = int(harga_semua_mobil-(diskon_hyundai*harga_semua_mobil))
         print(f"{nama} membeli hyundai seharga {hyundai} karna sedang diskon 23%")
else:
    print(f"{nama} tidak jadi membeli mobil")           