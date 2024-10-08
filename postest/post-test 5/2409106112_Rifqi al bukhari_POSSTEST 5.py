username_admin = "rifqi"
password_admin = "112"

akun = []
pilihan_sepatu = []
data_pesanan = []
order = []
harga_semua_sepatu = []


print("============================================")
while True:
    print("halo kawan! selamat datang pada toko sepatu kami")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("silahkan ke opsi selanjutnya")
    print("1.admin")
    print("2.Daftar akun")
    print("3.login")
    print("4.keluar")
    print("=====================================")
    pilih =input("silahkan pilih : ")
    print(" ")
    
    if pilih == "1":
        usernameadmin = input("masukkan username : ")
        passwordadmin = input("masukkan password : ")
        if usernameadmin == username_admin and passwordadmin == password_admin :
            while True:
                print("halloo bos apa yang kita lakukan hari ini?")
                print("1.atur harga sepatu")
                print("2.upload jenis sepatu")
                print("3.exit")
                pilih_admin = input(" mau yang mana? : ")
                    
                if pilih_admin == "1":
                      harga_semua_sepatu = int(input("masukkan harga : "))
                      print("===========================")
                      print(" ")
                
                elif pilih_admin == "2":
                    if not harga_semua_sepatu:
                        print("harga belum di tentukan")
                        print(" ")
                        
                    else:    
                        pilihan_sepatu = [f"1. Nike ={harga_semua_sepatu} ",f"Adidas = {harga_semua_sepatu}",
                                          f"converse {harga_semua_sepatu}",
                                      f"puma = {harga_semua_sepatu}"]
                        print(pilihan_sepatu)
                        print("===========================")
                        print(" ")
                    
                    
                elif pilih_admin == "3":
                    print("kembali ke beranda awal")
                    print("===========================")
                    print(" ")
                    break
                else:
                    print("input tidak valid silahkan pilih 1,2,dan 3.")
                    print(" ")
            
        else:
            print("username atau password kurang tepat,silahkan coba lagi")
            print(" ")
        
    
    elif pilih == "2":
        print("halo pelanggan baru! kami siap melayani anda dengan baik, silahkan buat akun dulu")
        username = input("masukkan username : ")
        akuna = False
        for akuns in akun:
            if akuns[0] == username:
                akuna = True
                break
        if akuna:
            print("username sudah terpakai silahkan ganti yang lain")
            print(" ")
        else:
            password = input("masukkan password : ")
            akun.append([username,password, ])
            print(f"akun anda berhasil di buat sekarang title anda adalah seorang pelanggan tebaik dengan ID {username}, silahkan lanjut ke opsi selanjutnya")
            print("================================")
            print(" ")
            
            
    elif pilih == "3":
        print(f"wahh pelanggan setia sudah  kembali silahkan login {username}")
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        for akuns in akun:
            if akuns[0] == username and akuns[1] == password:
                while True:
                    print("===================================")
                    print(f"selamata datang {username} silahkan mau pilih yang mana")
                    print("silahkan pilih opsi berikut")
                    print("1. tambah pembelian")
                    print("2. lihat keranjang pembelian")
                    print("3. edit pembelian")
                    print("4. hapus pesanan")
                    print("5. total harga")
                    print("6. exit")
                    
                    print("=============================")
                    
                    
                    memilih = input("silahkan di pilih : ")
                    print(" ")
                    
                    if memilih == "1":
                        if not pilihan_sepatu:
                            print("admin belom mengupload pilihan sepatu")
                            print(" ")
                            continue
                            
                        else:
                            print(pilihan_sepatu)
                            
                            
                        pilih_sepatu = input("silahkan di pilih : ")
                        if pilih_sepatu== "1":
                            print("wahhh selera anda bagus juga ya")
                            atas_nama = input("atas nama siapa : ")
                            alamat= input("alamat antar : ")
                            nike = harga_semua_sepatu
                            data_pesanan.append([atas_nama,alamat,harga_semua_sepatu])
                            print(f"harga dari sepatu nike adalah{harga_semua_sepatu}")
                            print(" ")
                            
                        elif pilih_sepatu == "2":
                            print("wahhh seleramu bagus sekali")
                            atas_nama = input("atas nama siapa : ")
                            alamat= input("alamat antar : ")
                            data_pesanan.append([atas_nama,alamat,harga_semua_sepatu])
                            adidas = harga_semua_sepatu
                            print(f"harga sepatu adidas adalah {adidas}")
                            print(" ")
                        
                        elif pilih_sepatu == "3":
                            print("wahhh seleramu bagus sekali")
                            atas_nama = input("atas nama siapa : ")
                            alamat= input("alamat antar : ")
                            data_pesanan.append([atas_nama,alamat,harga_semua_sepatu])
                            converse = harga_semua_sepatu
                            print(f"harga sepatu converse adalah {converse}")
                            print(" ")
                            
                        elif pilih_sepatu == "4":
                            print("wahhh seleramu bagus sekali")
                            atas_nama = input("atas nama siapa : ")
                            alamat= input("alamat antar : ")
                            data_pesanan.append([atas_nama,alamat,harga_semua_sepatu])
                            adidas = harga_semua_sepatu
                            print(f"harga sepatu adidas adalah {adidas}")
                            print(" ")
                        
                        
                        else:
                            print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.") 
                            print(" ") 
                            
                    elif memilih == "2":
                        for indeks, order in enumerate(data_pesanan): 
                            print(f"{indeks + 1}. atas nama: {order[0]} alamat : {order[1]} ")
                            print("==========================")
                            print(" ")
                            
                        if not data_pesanan:
                            print("belum ada barang yang anda pilih")
                            print("=====================================")
                            print(" ")
                            
                    elif memilih == "3":
                        if not data_pesanan:
                            print("Tidak ada pesanan yang bisa di edit.")
                            print(" ")
                        else:
                            edit = int(input("Catatan nomor berapa yang ingin kamu edit: ")) - 1
                            if 0 <= edit < len(data_pesanan):
                                ganti_baru = input("Masukkan nama baru : ")  
                                alamat_baru = input("alamat baru : ")
                                print("Apa kamu yakin ingin mengedit pesanan ?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "1":
                                    data_pesanan[edit] = [ganti_baru,alamat_baru] 
                                    print("pesanan yang kamu pilih sudah di edit ya!")
                                    print(" ")
                                elif memastikan_edit == "2":
                                    print("Aksi untuk mengedit pesanan dibatalkan")
                                    print(" ")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                                    print(" ")
                            else:
                                print("Tidak ada nomor pesanan yang kamu maksud, silahkan input ulang")
                                print(" ")
                                
                    elif memilih == "4":
                        if not data_pesanan:
                            print("Tidak ada pesanan yang bisa dihapus.")
                            print(" ")
                        else:
                            hapus = int(input("pesanan nomor berapa yang ingin dihapus: ")) - 1
                            if 0 <= hapus < len(data_pesanan):
                                print(f"Apa kamu yakin ingin menghapus pesaanan ? ")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "1":
                                    del data_pesanan[hapus]  
                                    print("pesanan yang kamu pilih sudah dihapus!")
                                    print(" ")
                                elif memastikan_hapus == "2":
                                    print("Aksi untuk menghapus dibatalkan")
                                    print(" ")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                                    print(" ")
                            else:
                                print("Tidak ada nomor pesanan yang kamu maksud, silahkan input ulang")
                                print(" ")
                                
                                
                                
                    elif memilih == "5":
                            total = 0
                            for indeks, order in enumerate(data_pesanan): 
                                total = total + order[2]
                            print(f"harga yang harus di bayar anda adalah sebanyak = {total}")
                            print(" ")
                           
                                
                            if not data_pesanan:
                                print(" belum ada barang yang anda pilih")
                                print(" ")
                    
                            
                    elif memilih == "6":
                        print("aplikasi di tutup ")
                        print(" ")
                        break
                        
                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.")
                        print(" ")         
                            
            else:
                print("username atau password kurang tepat, silahkan coba lagi")
                print(" ") 
            
    elif pilih == "4":
        print("Apakah kamu yakin ingin keluar dari aplikasi? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan!")
            print(" ")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'")
            print(" ")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")
        print(" ")
               
                                
                    
                    
                        
        
                        
                        
                        
    
                            
                            
                            
                            
                            
                            
        