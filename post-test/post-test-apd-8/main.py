from akun import register_user, login
from transaksi import create_transaksi, read_laporan, update_transaksi, delete_transaksi, hitung_total_aktif
from data import data
from clear import clear_screen

def main_menu():
    while True:
        print("Selamat datang! Pilih: 1. Registrasi  2. Login  3. Keluar")
        pilihan_awal = input("Masukkan pilihan: ")
        if pilihan_awal == '1':
            register_user()  
            role = login()  
        elif pilihan_awal == '2':
            role = login()
        elif pilihan_awal == '3':
            print("Terima kasih Telah Datang.")
            return
        else:
            print("Pilihan tidak valid.")
            continue
        
        while role:
            clear_screen()
            if role == 'admin':
                print("1. Buat Transaksi  2. Laporan  3. Update  4. Hapus  5. Logout")
            else:
                print("1. Buat Transaksi  2. Logout")  
            
            pilihan = input("Pilih: ")
            if pilihan == '1':
                waktu_mulai = input("Waktu mulai (YYYY-MM-DD): ")  
                try:
                    durasi = int(input("Durasi: "))  
                    nomor_pc = int(input("Nomor PC: "))
                    create_transaksi(waktu_mulai, durasi, nomor_pc)
                except ValueError:
                    print("Error: Input durasi dan nomor PC harus angka.")
            elif pilihan == '2' and role == 'admin':  
                tanggal = input("Tanggal: ")
                read_laporan(tanggal)
                transaksi_list = list(data['transaksi'].values())
                total_aktif = hitung_total_aktif(transaksi_list)
                print(f"Total transaksi aktif: {total_aktif}")
            elif pilihan == '2' and role != 'admin':  
                break  
            elif pilihan == '3' and role == 'admin':
                try:
                    update_transaksi(int(input("ID: ")), int(input("Durasi baru: ")))
                except ValueError:
                    print("Error: ID dan durasi harus angka.")
            elif pilihan == '4' and role == 'admin':
                try:
                    delete_transaksi(int(input("ID: ")))
                except ValueError:
                    print("Error: ID harus angka.")
            elif pilihan == '5' and role == 'admin':
                print("Anda telah logout.")
                role = None
            else:
                print("Pilihan tidak valid.")
            
            input("Tekan Enter")

if __name__ == "__main__":
    main_menu()