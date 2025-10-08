import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    attempts = 3
    while attempts > 0:
        print(f"Sisa percobaan: {attempts}")
        username = input("Masukkan username: ").strip()
        if not username or username.isspace():
            print("Username tidak boleh kosong atau hanya spasi. Coba lagi.")
            attempts -= 1
            continue
        password = input("Masukkan password: ").strip()
        if not password or password.isspace():
            print("Password tidak boleh kosong atau hanya spasi. Coba lagi.")
            attempts -= 1
            continue
        if username == "Arya" and password == "022":
            return True
        else:
            print("Username atau password salah")
            attempts -= 1
    return False

def tampilkan_menu_belanja():
    print("\n=== MENU BELANJA ===")
    print("1. Sampo - Rp25.000")
    print("2. Sabun Mandi - Rp18.000")
    print("3. Pasta Gigi - Rp9.000")
    print("4. Checkout")
    print("===================")

def hitung_harga_produk(pilihan):
    if pilihan == "1":
        return 25000, "Sampo"
    elif pilihan == "2":
        return 18000, "Sabun Mandi"
    elif pilihan == "3":
        return 9000, "Pasta Gigi"
    else:
        return 0, ""

clear_screen()

while True:
    
    status_member = input("Apakah Anda member? (y/n): ").lower().strip()
    is_member = False
    
    if status_member == "y":
        print("\n--- LOGIN ---")
        is_member = login()
        if not is_member:
            print("Login gagal setelah 3 percobaan. Anda dianggap sebagai non-member.")
    else:
        print("Anda dianggap sebagai non-member.")
    
    
    keranjang = ""
    total_harga = 0
    print("\nMulai belanja...")
    
    while True:
        tampilkan_menu_belanja()
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == "4":
            break
        
        harga, nama_produk = hitung_harga_produk(pilihan)
        if harga == 0:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            continue
        
        keranjang += f"{nama_produk}, "
        total_harga += harga
        print(f"{nama_produk} berhasil ditambahkan ke keranjang.")
        print(f"Total belanja sementara: Rp{total_harga:,}")
    
    
    if total_harga == 0:
        print("\nKeranjang kosong. Tidak ada transaksi.")
    else:
        print("\n=== STRUK BELANJA ===")
        daftar_belanja = keranjang.rstrip(", ") if keranjang else "Tidak ada produk"
        print(f"Daftar produk yang dibeli: {daftar_belanja}")
        
        if is_member:
            diskon = total_harga * 0.15
            total_bayar = total_harga - diskon
            print(f"Total harga sebelum diskon: Rp{total_harga:,}")
            print(f"Jumlah diskon (15%): Rp{diskon:,.0f}")
            print(f"Total yang harus dibayar: Rp{total_bayar:,.0f}")
        else:
            print(f"Total yang harus dibayar: Rp{total_harga:,}")
        
        print("====================")
    
    
    transaksi_baru = input("\nApakah ingin memulai transaksi baru? (y/n): ").lower().strip()
    if transaksi_baru != "y":
        print("Terima kasih telah berbelanja.")
        break
    else:
        clear_screen()
