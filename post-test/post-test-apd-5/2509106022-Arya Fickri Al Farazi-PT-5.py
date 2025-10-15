import os  
from datetime import datetime 

data = [  
    [],
    []   
]

if not any(user[0] == 'admin' for user in data[0]):
    data[0].append(['admin', '123', 'admin'])  # Username: admin, Password: 123, Role: admin

def register_user():
    username = input("Masukkan username baru: ")
    if any(user[0] == username for user in data[0]): 
        print("Username sudah digunakan.")
        return None
    password = input("Masukkan password: ")
    data[0].append([username, password, 'user'])  
    print(f"Pengguna {username} berhasil terdaftar sebagai user.")
    return username  

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    for user in data[0]:
        if user[0] == username and user[1] == password:
            print(f"Login berhasil sebagai {user[2]}.")
            return user[2]  
    print("Login gagal. Username atau password salah.")
    return None

def get_next_id():
    return len(data[1]) + 1  

def create_transaksi(waktu_mulai, durasi, harga_per_jam, nomor_pc):
    
    try:
        date_part = waktu_mulai.split(' ')[0]  
        datetime.strptime(date_part, '%Y-%m-%d')  
    except ValueError:
        print("Error: Waktu mulai harus dalam format YYYY-MM-DD (contoh: 2023-10-01, atau dengan waktu seperti 2023-10-01 14:30).")
        return
    
    if not isinstance(durasi, int) or durasi < 0:
        print("Error: Durasi harus angka positif.")
        return
    if not isinstance(harga_per_jam, float) and not isinstance(harga_per_jam, int) or harga_per_jam < 0:
        print("Error: Harga per jam harus angka positif.")
        return
    if not isinstance(nomor_pc, int) or nomor_pc < 0:
        print("Error: Nomor PC harus angka positif.")
        return
    total_biaya = harga_per_jam * durasi
    new_transaksi = {
        'id': get_next_id(),
        'waktu_mulai': waktu_mulai,
        'durasi': durasi,
        'harga_per_jam': harga_per_jam,
        'nomor_pc': nomor_pc,
        'total_biaya': total_biaya,
        'status': 'aktif'
    }
    data[1].append(new_transaksi)  
    print(f"Transaksi berhasil dibuat dengan ID: {new_transaksi['id']}")

def read_laporan(tanggal):
    if not isinstance(tanggal, str) or len(tanggal.split('-')) != 3:
        print("Error: Tanggal harus dalam format YYYY-MM-DD.")
        return
    harian = [t for t in data[1] if t['waktu_mulai'].split(' ')[0] == tanggal and t['status'] == 'aktif']
    total_pendapatan = sum(t['total_biaya'] for t in harian)
    print(f"Laporan Pendapatan untuk {tanggal}: Rp {total_pendapatan}")
    for t in harian:
        print(f"ID: {t['id']}, Waktu: {t['waktu_mulai']}")

def update_transaksi(id_transaksi, durasi_baru):
    if not isinstance(id_transaksi, int) or id_transaksi <= 0:
        print("Error: ID harus angka positif.")
        return
    if not isinstance(durasi_baru, int) or durasi_baru < 0:
        print("Error: Durasi harus angka positif.")
        return
    for t in data[1]:
        if t['id'] == id_transaksi and t['status'] == 'aktif':
            t['durasi'] = durasi_baru
            t['total_biaya'] = t['harga_per_jam'] * durasi_baru
            print(f"Transaksi ID {id_transaksi} diupdate.")
            return
    print("Transaksi tidak ditemukan.")

def delete_transaksi(id_transaksi):
    if not isinstance(id_transaksi, int) or id_transaksi <= 0:
        print("Error: ID harus angka positif.")
        return
    for t in data[1]:
        if t['id'] == id_transaksi:
            t['status'] = 'dibatalkan'
            print(f"Transaksi ID {id_transaksi} dibatalkan.")
            return
    print("Transaksi tidak ditemukan.")

def main_menu():
    print("Selamat datang! Pilih: 1. Registrasi  2. Login  3. Keluar")
    pilihan_awal = input("Masukkan pilihan: ")
    if pilihan_awal == '1':
        register_user()  
        role = login()  
    elif pilihan_awal == '2':
        role = login()
    else:
        return
    
    while role:
        os.system('cls' if os.name == 'nt' else 'clear')
        if role == 'admin':
            print("1. Buat Transaksi  2. Laporan  3. Update  4. Hapus  5. Keluar")
        else:
            print("1. Buat Transaksi  2. Keluar")  
        
        pilihan = input("Pilih: ")
        if pilihan == '1':
            waktu_mulai = input("Waktu mulai (YYYY-MM-DD): ")  
            durasi = int(input("Durasi: "))  
            harga_per_jam = float(input("Harga/jam: "))
            nomor_pc = int(input("Nomor PC: "))
            create_transaksi(waktu_mulai, durasi, harga_per_jam, nomor_pc)
        elif pilihan == '2' and role == 'admin':  
            read_laporan(input("Tanggal: "))
        elif pilihan == '2' and role != 'admin':  
            break  
        elif pilihan == '3' and role == 'admin':
            update_transaksi(int(input("ID: ")), int(input("Durasi baru: ")))
        elif pilihan == '4' and role == 'admin':
            delete_transaksi(int(input("ID: ")))
        elif pilihan == '5' and role == 'admin':
            break
        else:
            print("Pilihan tidak valid.")
        
        input("Tekan Enter")

if __name__ == "__main__":
    main_menu()
