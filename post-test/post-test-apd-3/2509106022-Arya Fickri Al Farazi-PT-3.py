def login ():
    username = input("Masukkan username ")
    password = input ("Masukkan password ")
    return True if username == "Arya" and password == "022" else False

def hitung_harga(jenis):
    return (25000 if jenis == "sampo" else 18000 if jenis == "sabun mandi" else 9000 if jenis == "pasta gigi" else 0)

print ("Daftar barang: ")
print ("1. sampo - Rp25.000")
print ("2. sabun mandi - Rp18.000")
print ("3. pasta gigi - Rp9.000")

member = input("Apakah anda member ? (ya/tidak): ").lower()

if member == "ya":
    login_status = login()
    print(f"Login {'berhasil' if login_status else 'gagal'}")
    if login_status:
        jenis_barang = input("Pilih barang (sampo/sabun mandi/pasta gigi): ").lower()
        total_harga = hitung_harga(jenis_barang)
        if total_harga == 0:
            print("barang tidak tersedia")
        else:
            diskon = total_harga * 0.15
            harga_setelah_diskon = total_harga - diskon
            print(f"harga sebelum diskon: Rp{total_harga:.2f}")
            print(f"total diskon: Rp{diskon:.2f}")
            print(f"harga sesudah diskon diskon: Rp{harga_setelah_diskon:.2f}")
    else:
        print("Tidak dapat melanjutkan transaksi.")
else:
    jenis_barang = input("Pilih barang (sampo/sabun mandi/pasta gigi): ").lower()
    total_harga = hitung_harga(jenis_barang)
    if total_harga == 0:
        print("Barang tidak tersedia.")
    else:
        print(f"Total harga tanpa diskon: Rp{total_harga:.2f}")