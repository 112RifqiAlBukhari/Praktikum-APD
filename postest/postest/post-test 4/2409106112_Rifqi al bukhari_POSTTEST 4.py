username = "rifqi"
password = 112
 # login
batas = 0
for i in range (3) :
    human = input("masukkan username : ")
    pw = input("masukkan pasword : ")
    batas +=1
    print(f"total mencoba {batas}")
    if human == "rifqi" and pw == "112":
        print("anda berhasil login")
        print("selamat datang dan pilih sesuai kemauan anda")
        #membeli mobil
        #diskon mobil
        diskon_tesla= 17/100
        diskon_toyota= 21/100
        diskon_hyundai= 23/100
        print("1. mobil tesla")
        print("2. mobil toyota")
        print("3. mobil hyundai")
        print("4. keluar")
        mobil =input("mobil apa yang anda pilih : ")
        harga_semua_mobil = int(input("masukkan harga :"))
        if mobil == "1" :
                tesla = int(harga_semua_mobil-(diskon_tesla*harga_semua_mobil))
                print(f"anda memilih mobil tesla dengan harga {tesla} karna sedang ada diskon 17%")
                print("selamat atas mobil baru anda dan senang melayani anda")
        elif mobil == "2" :
                toyota = int(harga_semua_mobil-(diskon_toyota*harga_semua_mobil))
                print(f"anda memilih mobil toyota dengan harga {toyota} karna sedang ada diskon 21%")
                print("selamat atas mobil baru anda dan senang melayani anda")
        elif mobil == "3":
                hyundai = int(harga_semua_mobil-(diskon_hyundai*harga_semua_mobil))
                print(f"anda memilih mobil toyota dengan harga {hyundai} karna sedang ada diskon 23%")
                print("selamat atas mobil baru anda dan senang melayani anda")
        elif mobil == "4":
                keluar = ("tidak jadi beli")
                print("terimakasih sudah berkunjung ke toko kami")
        break
    elif human or pw:
        print("username atau password kurang tepat")
else:
    print("terlalu banyak salah anda sudah melewati batas,program berhenti")
