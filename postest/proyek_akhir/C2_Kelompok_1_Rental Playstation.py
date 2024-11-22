from prettytable import PrettyTable # untuk membuat tabel

from colorama import init, Fore # untuk mewarnai terminal
init()

# username dan password admin
admin = "cepecial"
password = "24"
pesanan_ps = [] #untuk penyimpan pesanan ps pelanggan

# menu makanan dan menu makanan menggukanan nested dictionary
menu_makanan = {
    1:{  "Makanan" : 'indomie goreng/rebus', 'Harga' : 6000},
    2:{  "Makanan" : 'nasi', 'Harga' : 5000},
    3:{  "Makanan" : 'telur goreng/rebus', 'Harga' : 3000 },
    4:{  "Makanan" : 'gorengan', 'Harga' : 5000}
}

menu_minuman = {
      1:{"Minuman" : "es teh panas/dingin", "Harga" : 4000},
      2:{"Minuman" : "Nutrisari", "Harga" : 3000},
      3:{"Minuman" : "kopi panas", "Harga" : 3000},
      4:{"Minuman" : "kopi dingin", "Harga" : 5000},
      5:{"Minuman" : "extrajoss", "Harga" : 4000},
      6:{"Minuman" : "extrajoss + susu", "Harga" : 6000},
      7:{"Minuman" : "kukubima", "Harga" : 4000},
      8:{"Minuman" : "kukubima + susu", "Harga" : 6000},
      9:{"Minuman" : "pop ice", "Harga" : 4000}
}

# menu semua ruangan ps menggunakan dictionary dalam list dan termasuk dalam tipe list
lihat_menu_ps_no_smoking = [
    {"No": 1, "Ruangan": 1, "jenis": "ps 4", "Harga": 10000 },
    {"No": 2, "Ruangan": 2, "jenis": "ps 4", "Harga": 10000 },
    {"No": 3, "Ruangan": 3, "jenis": "ps 4", "Harga": 10000 },
    {"No": 4, "Ruangan": 4, "jenis": "ps 5", "Harga": 15000 },
    {"No": 5,"Ruangan": 5, "jenis": "ps 5", "Harga": 15000 }
]


lihat_menu_ps_smoking = [
    {"No": 1,"Ruangan": 11, "jenis": "ps 4", "Harga": 10000 },
    {"No": 2,"Ruangan": 12, "jenis": "ps 4", "Harga": 10000 },
    {"No": 3,"Ruangan": 13, "jenis": "ps 4", "Harga": 10000 },
    {"No": 4,"Ruangan": 14, "jenis": "ps 5", "Harga": 15000 },
    {"No": 5,"Ruangan": 15, "jenis": "ps 5", "Harga": 15000 }
]


lihat_menu_ps_vip = [
    {"No": 1,"Ruangan": 21, "jenis": "ps 5", "Harga": 20000 },
    {"No": 2,"Ruangan": 22, "jenis": "ps 5", "Harga": 20000 },
    {"No": 3,"Ruangan": 23, "jenis": "ps 5", "Harga": 20000 },
    {"No": 4,"Ruangan": 24, "jenis": "ps 5", "Harga": 20000 },
    {"No": 5,"Ruangan": 25, "jenis": "ps 5", "Harga": 20000 }
]


def lihat_menu_ps_no_smokingg():
    print(Fore.BLUE + "===Lihat menu ruangan no smoking===")
    table = PrettyTable(["No", "Ruangan", "Jenis", "Harga"])
    for info in lihat_menu_ps_no_smoking: 
        table.add_row([info["No"], info["Ruangan"], info["jenis"], info["Harga"], ])
    print(table)
    
    
def lihat_menu_ps_smokingg():
    print(Fore.BLUE +"===Lihat menu ruangan  smoking===")
    table = PrettyTable(["No", "Ruangan", "Jenis", "Harga" ])
    for info in lihat_menu_ps_smoking:
        table.add_row([info["No"], info["Ruangan"], info["jenis"], info["Harga"], ])
    print(table)
   
    
def lihat_menu_ps_vipp():
    print(Fore.BLUE + "===Lihat menu ruangan Vip===")
    table = PrettyTable(["No", "Ruangan", "Jenis", "Harga" ])
    for info in lihat_menu_ps_vip:
        table.add_row([info["No"], info["Ruangan"], info["jenis"], info["Harga"]])
    print(table)

    
def lihat_menu_makanan():
    print(Fore.GREEN + "===Lihat menu makanan===")
    table = PrettyTable([ "NO", "Makanan", "Harga"])
    for No, info in menu_makanan.items():
        if isinstance(info, dict):
            table.add_row([No, info["Makanan"], info["Harga"]])
    print(table)
        
def lihat_menu_minuman():
    print(Fore.GREEN + "===Lihat menu minuman===")
    table = PrettyTable([ "NO","Minuman", "Harga"])
    for No, info in menu_minuman.items():
        table.add_row([ No, info["Minuman"], info["Harga"], ])
    print(table)
        
def tambah_data_makanan():
    print(Fore.GREEN + "== Tambah Data Makanan ==")
    print("=" * 10)
    input_nama_makanan = input("Nama makanan\t: ")
    if input_nama_makanan.isalpha():
        try:
            input_Harga= int(input("Harga\t: "))
            next_key = max(menu_makanan.keys()) + 1
            menu_makanan[next_key] = {
                "Makanan": input_nama_makanan,
                "Harga": input_Harga
            }
            print("Data makanan berhasil ditambahkan!")
            return menu_makanan
        except ValueError:
            print("Inputan Tidak Valid")
    else:
        print("Inputan Tidak Valid")

def tambah_data_minuman():
    print(Fore.GREEN + "== Tambah Data Minuman ==")
    print("=" * 10)
    input_nama_minuman = input("Nama minuman\t: ")
    if input_nama_minuman.isalpha():
        try:
            input_Harga= int(input("Harga\t: "))
            next_key = max(menu_makanan.keys()) + 1
            menu_minuman[next_key]({
            "Minuman" : input_nama_minuman,
            "Harga" : input_Harga
            })    
            return menu_minuman
        except ValueError:
            print("Inputan Tidak Valid")
    else:
        print(" Inputan Tidak Valid")

def tambah_data_ps_no_smoking():
    print(Fore.GREEN + "== Tambah Data Ps No Smoking==")
    print("=" * 10)
    lihat_menu_ps_no_smokingg()
    try:
        input_nomor = int(input("No: "))
        input_nama_ruangan = int(input("No ruangan\t: "))
        input_jenis_ps = input("jenis\t: ")
        input_Harga= int(input("Harga\t: "))
        lihat_menu_ps_no_smoking.append({
        "No" : input_nomor,
        "Ruangan" : input_nama_ruangan,
        "jenis"  : input_jenis_ps,
        "Harga" : input_Harga
        })    
        return input_nomor,input_nama_ruangan,input_jenis_ps,input_Harga
    except ValueError:
        print("Inputan Tidak Valid")

def tambah_data_ps_smoking():
    print(Fore.GREEN + "== Tambah Data Ps Smoking==")
    print("=" * 10)
    try:
        input_nomor = int(input("No: ")) 
        input_nama_ruangan = int(input("No ruangan\t: "))
        input_jenis_ps = input("jenis\t: ")
        input_Harga= int(input("Harga\t: "))
        lihat_menu_ps_smoking.append({
        "No" : input_nomor,
        "Ruangan" : input_nama_ruangan,
        "jenis"  : input_jenis_ps,
        "Harga" : input_Harga
            })    
        return input_nomor,input_nama_ruangan,input_jenis_ps,input_Harga   
    except ValueError:
        print("Inputan Tidak Valid")

def tambah_data_ps_vip():
    print(Fore.GREEN + "== Tambah Data Ps Vip ==")
    print("=" * 10)
    try:
        input_nomor = int(input("No: ")) 
        input_nama_ruangan = int(input("No ruangan\t: "))
        input_Harga= int(input("Harga\t: "))
        input_jenis_ps = input("jenis Ps\t: ")
        lihat_menu_ps_vip.append({
         "No" : input_nomor,
        "Ruangan" : input_nama_ruangan,
        "jenis"  : input_jenis_ps,
        "Harga" : input_Harga
            })    
        return input_nomor,input_nama_ruangan,input_jenis_ps,input_Harga
    
    except ValueError:
        print("Inputan Tidak Valid")

def hapus_data_makanan():
    print(Fore.GREEN + "== Hapus Data Makanan ==")
    lihat_menu_makanan()
    print(" ")
    try:
        hapus = int(input("masukkan data ke berapa yang ingin dihapus: "))
        if hapus> len(menu_makanan) or hapus < 1:
            print("data tidak ditemukan")
        else:
            del_data = menu_makanan.pop(hapus)
            print(f"Menu Nomor {del_data['Makanan']} dengan Harga {del_data['Harga']} telah dihapus")
    except ValueError:
        print("Masukkan nomor ruangan yang valid.")
        
def clear_pesanan_cemilan():
    try:
        hapus = int(input("masukkan pesanan Ke Berapa Yang Sudah Selesai Di Antar, jika tidak ada silahkan tekan enter: "))
        if hapus> len(pesanan) or hapus < 1:
            print("data tidak ditemukan")
        else:
            del_data = pesanan.pop(hapus-1)
            print(f"{del_data['item']} dengan Harga {del_data['Harga']} telah di Selesaikan")
    except ValueError:
        print("Masukkan nomor ruangan yang valid.")
        

        
def hapus_data_minuman():
    print(Fore.BLUE + "== Hapus Data Minuman ==")
    lihat_menu_minuman()
    try:
        hapus = int(input("masukkan data ke berapa yang ingin dihapus: "))
        if hapus> len(menu_minuman) or hapus < 1:
            print("data tidak ditemukan")
        else:
            del_data = menu_minuman.pop(hapus)
            print(f"Menu Nomor {del_data['Minuman']} dengan Harga {del_data['Harga']} telah dihapus")
    except ValueError:
        print("Masukkan nomor ruangan yang valid.")

def hapus_data_ps_no_smoking():
    print(Fore.BLUE + "== Hapus Data Ps No Smoking ==")
    lihat_menu_ps_no_smokingg()
    try:
        hapus = int(input("masukkan Ruangan ke berapa yang ingin dihapus: "))
        if hapus> len(lihat_menu_ps_no_smoking) or hapus < 1:
            print("data tidak ditemukan")
        else:
            del_data = lihat_menu_ps_no_smoking.pop(hapus-1)
            print(f"{del_data['Ruangan']} dengan jenis {del_data['jenis']} dan dengan Harga {del_data['Harga']} telah dihapus")
    except ValueError:
        print("Masukkan nomor ruangan yang valid.")
        
def hapus_data_ps_smoking():
    print(Fore.BLUE + "== Hapus Data Ps Smoking ==")
    lihat_menu_ps_smokingg()
    try:
        hapus = int(input("masukkan Ruangan ke berapa yang ingin dihapus: "))
        if hapus> len(lihat_menu_ps_smoking) or hapus < 1:
            print("data tidak ditemukan")
        else:
            del_data = lihat_menu_ps_smoking.pop(hapus-1)
            print(f"{del_data['Ruangan']} dengan jenis {del_data['jenis']} dan dengan Harga {del_data['Harga']} telah dihapus")
    except ValueError:
        print("Masukkan nomor ruangan yang valid.")

def hapus_data_vip():
    print(Fore.BLUE + "== Hapus Data Ps Vip ==")
    lihat_menu_ps_vipp()
    try:
        hapus = int(input("masukkan Ruangan yang ingin dihapus: "))
        if hapus> len(lihat_menu_ps_vip) or hapus < 0:
            print("data tidak ditemukan")
        else:
            del_data = lihat_menu_ps_vip.pop(hapus-1)
            print(f"{del_data['Ruangan']} dengan jenis {del_data['jenis']} dan dengan Harga {del_data['Harga']} telah dihapus")
    except ValueError:
        print("Masukkan nomor ruangan yang valid.")

#fungsi pelanggan

pesanan = []  
def buat_pesanan_cemilan():
    total_pesanan = 0  

    while True:
        print(Fore.GREEN + "*" * 50)
        print(Fore.BLUE + "================= MENU CEMILAN ===================")
        print(Fore.GREEN + "*" * 50)
        print("MENU")
        print("[1] Makanan")
        print("[2] Minuman")
        print("[3] keluar")
        print("=" * 50)
        print(" ")

        kategori = input("Masukkan Kategori Cemilan Yang Ingin Dibeli : ")

        if kategori == '1':  
            lihat_menu_makanan()
            try:
                pilihan = input("Pilih makanan yang ingin dipesan atau tekan 'k' jika sudah selesai memilih: ")
                if pilihan == 'k':
                    continue
                
                try:
                    pilihan = int(pilihan)
                    if 0 <= pilihan <= len(menu_makanan):
                        item = menu_makanan[pilihan ]
                        jumlah = int(input(f"Berapa jumlah {item['Makanan']} yang dipesan? "))
                        pesanan.append({"item": item['Makanan'], "Harga": item['Harga'], "jumlah": jumlah})
                        total_pesanan += item['Harga'] * jumlah
                        print(f"{jumlah} {item['Makanan']} ditambahkan ke pesanan.")
                                                
                        print("\nPesanan Anda:")
                        for item in pesanan:
                            print(f"- {item['jumlah']} x {item['item']} (Rp {item['Harga']}/item) = Rp {item['Harga'] * item['jumlah']}")
                        print(f"\nTotal Harga: Rp {total_pesanan}")
                        lanjut = input("Apakah ingin memesan lagi? (iya/tidak): ")
                        if lanjut.lower() != 'iya':
                            break
                except ValueError:
                    print(" Inputan tidak valid")
                         
            except TypeError:
                print("Masukkan angka yang valid.")
      
        elif kategori == '2':  
            lihat_menu_minuman()
            try:
                pilihan = input("Pilih minuman yang ingin dibeli atau ketik 'k' jika sudah selesai memilih: ")
                if pilihan == 'k':
                    continue
                try:
                    pilihan = int(pilihan)
                    if 0 <= pilihan <= len(menu_minuman):
                            item = menu_minuman[pilihan ]
                            jumlah = int(input(f"Berapa jumlah {item['Minuman']} yang dipesan? "))
                            pesanan.append({"item": item['Minuman'], "Harga": item['Harga'], "jumlah": jumlah})
                            total_pesanan += item['Harga'] * jumlah
                            print(f"{jumlah} {item['Minuman']} ditambahkan ke pesanan.")
                                                
                            print("\nPesanan Anda:")
                            for item in pesanan:
                                print(f"- {item['jumlah']} x {item['item']} (Rp {item['Harga']}/item) = Rp {item['Harga'] * item['jumlah']}")
                            print(f"\nTotal Harga: Rp {total_pesanan}")
                            lanjut = input("Apakah ingin memesan lagi? (iya/tidak): ")
                            if lanjut.lower() != 'iya':
                                break

                except ValueError:
                    print("Masukkan angka yang valid.")
            except TypeError:
                print("Masukkan angka yang valid.")
                
            
        elif kategori == '3':
            print("\nPesanan Anda:")
            for item in pesanan:
                print(f"- {item['jumlah']} x {item['item']} (Rp {item['Harga']}/item) = Rp {item['Harga'] * item['jumlah']}")
            print(f"\nTotal Harga: Rp {total_pesanan}")
            break
        else:
            print("anda tidak jadi memesan.")




def lihat_pesanan_cemilan():
    if pesanan:
        print("\nPesanan Anda:")
        for item in pesanan:
            print(f"- {item['jumlah']} x {item['item']} (Rp {item['Harga']}/item) = Rp {item['Harga'] * item['jumlah']}")
    
def buat_pesanan_ps():
    total_pesanan = 0
    
    while True:
            print(Fore.GREEN + "*" * 50)
            print(Fore.BLUE + "=========== MENU RUANGAN PLAYSTATION =============")
            print(Fore.GREEN + "*" * 50)
            print("MENU")
            print("[1] Ruangan No Smoking")
            print("[2] Ruangan Smoking")
            print("[3] Ruangan Vip")
            print("[4] keluar")
            print("=" * 50)
            print(" ")
            kategori_ruangan = input("Pilih kategori ruangan : ")
            
            
            if kategori_ruangan == '1':
                lihat_menu_ps_no_smokingg()
                try:
                    pilihan = input("pilih Ruangan yang ingin dipesan atau tekan 'k' jika sudah selesai memilih: ")
                    if pilihan == 'k':
                            continue
                    try:
                        pilihan = int(pilihan)
                        if 1 <= pilihan <= len(lihat_menu_ps_no_smoking):
                            item = lihat_menu_ps_no_smoking[pilihan - 1]        
                            pesanan_ps.append({"Ruangan": item, "Harga": item['Harga'],})
                            total_pesanan += item['Harga'] 
                            print(f"{item['Ruangan']} ditambahkan ke pesanan.")
                            for item in pesanan_ps:
                                print(f"- {item['Ruangan']} = (Rp {item['Harga']}/item)")
                                print(f"\nTotal Harga: Rp {total_pesanan}")
                                
                            if pilihan> len(lihat_menu_ps_no_smoking) or pilihan < 1:
                                print("data tidak ditemukan")
                            else:
                                del_data = lihat_menu_ps_no_smoking.pop(pilihan-1)
                                print(f"{del_data['Ruangan']} dengan jenis {del_data['jenis']} dan dengan Harga {del_data['Harga']} telah dihapus")
                        else:
                            print("Nomor makanan tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")
                except TypeError:
                        print("Masukkan angka yang valid.")
                
            elif kategori_ruangan == '2':
                lihat_menu_ps_smokingg()
                
                pilihan = input("pilih Ruangan yang ingin dipesan atau tekan 'k' jika sudah selesai memilih: ")
                if pilihan in pesanan_ps:
                    print("Ruangan Sudah Di pesan")
                elif pilihan == 'k':
                        continue
                try:
                    pilihan = int(pilihan)
                    if 1 <= pilihan <= len(lihat_menu_ps_smoking):
                        item = lihat_menu_ps_smoking[pilihan - 1]
                        pesanan_ps.append({"Ruangan": item, "Harga": item['Harga'],})
                        total_pesanan += item['Harga'] 
                        print(" ")
                        print(f" Ruangan {item['Ruangan']} ditambahkan ke pesanan.")
                        print("\nPesanan Anda:")
                        for item in pesanan_ps:
                            print(f"- {item['Ruangan']} = (Rp {item['Harga']}/item)")
                            print(f"\nTotal Harga: Rp {total_pesanan}")
                        if pilihan> len(lihat_menu_ps_smoking) or pilihan < 1:
                            print("data tidak ditemukan")
                        else:
                            del_data = lihat_menu_ps_smoking.pop(pilihan-1)
                            print(f"{del_data['Ruangan']} dengan jenis {del_data['jenis']} dan dengan Harga {del_data['Harga']} telah dihapus")
                except ValueError:
                    print("Masukkan angka yang valid.")

                        
                
            elif kategori_ruangan == '3':
                lihat_menu_ps_vipp()
                try:
                    pilihan = input("pilih Ruangan yang ingin dipesan atau tekan 'k' jika sudah selesai memilih: ")
                    if pilihan == 'k':
                        continue
                    try:
                        pilihan = int(pilihan)
                        if 1 <= pilihan <= len(lihat_menu_ps_vip):
                            item = lihat_menu_ps_vip[pilihan - 1]
                            pesanan_ps.append({"Ruangan": item, "Harga": item['Harga'],})
                            total_pesanan += item['Harga'] 
                            print(f"{item['Ruangan']} ditambahkan ke pesanan.")
                            print("\nPesanan Anda:")
                            for item in pesanan_ps:
                                print(f"- {item['Ruangan']} = (Rp {item['Harga']}/item)")
                                print(f"\nTotal Harga: Rp {total_pesanan}")
                            if pilihan> len(lihat_menu_ps_vip) or pilihan < 1:
                                print("data tidak ditemukan")
                            else:
                                del_data = lihat_menu_ps_vip.pop(pilihan-1)
                                print(f"{del_data['Ruangan']} dengan jenis {del_data['jenis']} dan dengan Harga {del_data['Harga']} telah dihapus")
                    except ValueError:
                        print("Masukkan angka yang valid.")
                except TypeError:
                    print("Masukkan angka yang valid.")
            
            elif kategori_ruangan == "4":
                break
            
            else:
                print("inputan tidak valid")
                
def lihat_pesanan_ps():
    if pesanan_ps:
        print("\nPesanan Anda:")
        for item in pesanan_ps:
            print(f"- {item['Ruangan']} = (Rp {item['Harga']}) ")
            
# program inti
while True:
    print(Fore.BLUE + "*" * 50)
    print(Fore.GREEN + "=============== SELAMATT DATANGG =================")
    print(Fore.BLUE + "*" * 50)
    print("MENU")
    print("[1] Admin")
    print("[2] Pelanggan")
    print("[3] keluar")
    print("=" * 50)
    print(" ")
    
    
    memilih = input("silahkan di pilih : ")
    print(" ")
    
    if memilih == "1":
        # Cek apakah username dan password cocok dengan username dan password yang telah di tentukan
        username_admin = input(Fore.YELLOW + "Masukkan username anda : ")
        password_admin = input("Masukkan password anda : ")
        if username_admin == admin and password_admin == password :
            while True:
                # menu admin
                print(Fore.GREEN + "*" * 50)
                print(Fore.BLUE + "============ SELAMATT DATANGG GAMERSS ==============")
                print(Fore.GREEN + "*" * 50)
                print("MENU")
                print("[1] Lihat Menu Cemilan")
                print("[2] Lihat Menu Ps")
                print("[3] Tambah Menu")
                print("[4] Hapus Menu")
                print("[5] LIhat Pesanan (Cemilan)")
                print("[6] Lihat Pesanan (Ps)")
                print("[7] Kembali Ke halaman Sebelumnya")
                print("=" * 50)
                print(" ")
            
                 
                pilih = input("silahkan pilih tuan : ")
                print(" ")
                
                if pilih == "1":
                    lihat_menu_makanan()
                    print(" ")
                    lihat_menu_minuman()
                        
                elif pilih == "2":
                    lihat_menu_ps_no_smokingg()
                   
                    print(" ")
                    lihat_menu_ps_smokingg()
                    print(" ")
                    lihat_menu_ps_vipp()
                    print(" ")
                    
                elif pilih == "3":
    
                        while True:
                            print(Fore.GREEN + "*" * 50)
                            print(Fore.BLUE + "========== MENU YANG INGIN DI TAMBAH ============")
                            print(Fore.GREEN + "*" * 50)
                            print("MENU")
                            print("[1] Menu Makanan")
                            print("[2] Menu Minuman")
                            print("[3] Ruangan Ps")
                            print("[4] keluar")
                            print("=" * 50)
                            print(" ")
                            pilih_ganti = input("masukkan yang ingin menu mana yang anda ingin ganti :  ")
                            print(" ")
                        
                            if pilih_ganti == "1":
            
                                tambah_data_makanan()
                                
                            elif pilih_ganti == "2":
            
                                tambah_data_minuman()
                            
                            elif pilih_ganti == "3":
            
                                while True:
                                    print(Fore.GREEN +"*" * 50)
                                    print(Fore.BLUE + "======= MENU RUANGAN YANG INGIN DI TAMBAH ========")
                                    print(Fore.GREEN + "*" * 50)
                                    print("MENU")
                                    print("[1] Ruangan No Smoking")
                                    print("[2] Ruangan Smoking")
                                    print("[3] Ruangan Vip")
                                    print("[4] keluar")
                                    print("=" * 50)
                                    print(" ")
                                    pilih_gantii = input("pilih yang mana : ")
                                    if pilih_gantii == "1":
                    
                                        tambah_data_ps_no_smoking()
                                    
                                    elif pilih_gantii == "2":
                    
                                        tambah_data_ps_smoking()
                                        
                                    elif pilih_gantii == "3":
                    
                                        tambah_data_ps_vip()
                                    
                                    elif pilih_gantii == "4":
                                        print("kembali ke beranda")
                                        break
                                    
                                    else:
                                        print("inputan anda tidak valid,silahkan pilih 1,2,3,dan 4")
                                
                            elif pilih_ganti == "4":
                                print("kembali ke beranda")
                                break
                            
                            else:
                                print("inputan anda tidak valid,silahkan pilih 1,2,3,dan 4")
                                
                                
                elif pilih == "4":
    
                        while True:
                            print(Fore.GREEN + "*" * 50)
                            print(Fore.BLUE + "=========== MENU YANG INGIN DI HAPUS ============")
                            print(Fore.GREEN + "*" * 50)
                            print("MENU")
                            print("[1] Menu Makanan")
                            print("[2] Menu Minuman")
                            print("[3] Ruangan Ps")
                            print("[4] keluar")
                            print("=" * 50)
                            print(" ")
                            pilih_hapus = input("masukkan yang inginmenu mana yang anda ingin ganti :  ")
                            print(" ")

                            if pilih_hapus == "1":
            
                                hapus_data_makanan()
                                
                            elif pilih_hapus == "2":
            
                                hapus_data_minuman()
                                
                            elif pilih_hapus == "3":
                                while True:
                                    print(Fore.GREEN + "*" * 50)
                                    print(Fore.BLUE + "======= MENU RUANGAN YANG INGIN DI HAPUS =========")
                                    print(Fore.GREEN + "*" * 50)
                                    print("MENU")
                                    print("[1] Ruangan No Smoking")
                                    print("[2] Ruangan Smoking")
                                    print("[3] Ruangan Vip")
                                    print("[4] keluar")
                                    print("=" * 50)
                                    print(" ")
                                    pilih_hapuss= input("pilih yang mana : ")
                                    print(" ")
                                    
                                    if pilih_hapuss == "1":
                                        hapus_data_ps_no_smoking()
                                        
                                    elif pilih_hapuss == "2":
                                        hapus_data_ps_smoking()
                                        
                                    elif pilih_hapuss == "3":
                                        hapus_data_vip()
                                        
                                    elif pilih_hapuss == "4":
                                        print("Kembali ke menu sebelumnya")
                                        break
                                    else:
                                        print("inputan tidak valid")
                            
                                
                                
                            elif pilih_hapus == "4":
                                print("kembali ke menu sebelumnya")
                                print(" ")
                                break
                            else:
                                print("inputan tidak valid")
                            
                elif pilih == "5":
                        lihat_pesanan_cemilan()
                        print(" ")
                        clear_pesanan_cemilan()
                        print(" ")
                    
                elif pilih == "6":
                        lihat_pesanan_ps()
                        print(" ")
                        
                        
                elif pilih == "7":
                        print(" ")
                        print("Kembali Ke Beranda")
                        print(" ")
                        break

    elif memilih == "2":
            while True:
                # menu pelanggan
                print(Fore.GREEN + "*" * 50)
                print(Fore.BLUE + "============ SELAMATT DATANGG GAMERSS ==============")
                print(Fore.GREEN + "*" * 50)
                print("MENU")
                print("[1] Cemilan")
                print("[2] Ps")
                print("[3] keluar")
                print("=" * 50)
                print(" ")
                
                memilih = input("pilih : ")
                
                if memilih == "1":
                    buat_pesanan_cemilan()
                    print(" ")
                
                elif memilih == "2":
                    buat_pesanan_ps()
                    print(" ")
                    
                elif memilih == "3":
                    print(" ")
                    print("Kembali Beranda")
                    print(" ")
                    break
                
                else:
                    print("inputan tidak valid")
    elif memilih == "3":
        print(Fore.CYAN + "TERIMAKASIH DAN SEMANGAT")
        break
    else:
        print("inputan tidak valid")