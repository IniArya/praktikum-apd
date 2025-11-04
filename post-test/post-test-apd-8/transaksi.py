from data import data, HARGA_PER_JAM, MAX_PC
from prettytable import PrettyTable

def get_next_id():
    return len(data['transaksi']) + 1  

def hitung_total_aktif(transaksi_list, index=0, count=0):
    if index >= len(transaksi_list):
        return count
    if transaksi_list[index]['status'] == 'aktif':
        count += 1
    return hitung_total_aktif(transaksi_list, index + 1, count)

def create_transaksi(waktu_mulai, durasi, nomor_pc):
    try:
        date_part = waktu_mulai.split(' ')[0]
        if len(date_part.split('-')) != 3:
            raise ValueError("Waktu mulai harus dalam format YYYY-MM-DD.")
        
        if not isinstance(durasi, int) or durasi <= 0:
            raise ValueError("Durasi harus angka positif.")
        if not isinstance(nomor_pc, int) or nomor_pc <= 0 or nomor_pc > MAX_PC:
            raise ValueError(f"Nomor PC harus angka positif dan maksimal {MAX_PC}.")
        
        total_biaya = HARGA_PER_JAM * durasi
        new_transaksi = {
            'id': get_next_id(),
            'waktu_mulai': waktu_mulai,
            'durasi': durasi,
            'total_biaya/jam': total_biaya,
            'nomor_pc': nomor_pc,
            'total_biaya': total_biaya,
            'status': 'aktif'
        }
        data['transaksi'][new_transaksi['id']] = new_transaksi
        print(f"Transaksi berhasil dibuat ID: {new_transaksi['id']}, Dengan Harga/Jam: Rp 12.00, Total Biaya Menjadi: Rp {total_biaya}")
    except ValueError as e:
        print(f"Error: {e}")

def read_laporan(tanggal):
    try:
        if not isinstance(tanggal, str) or len(tanggal.split('-')) != 3:
            raise ValueError("Tanggal harus dalam format YYYY-MM-DD.")
        harian = [t for t in data['transaksi'].values() if t['waktu_mulai'].split(' ')[0] == tanggal and t['status'] == 'aktif']
        total_pendapatan = sum(t['total_biaya'] for t in harian)
        
        # Menggunakan PrettyTable untuk output laporan
        table = PrettyTable()
        table.field_names = ["ID", "Waktu Mulai", "Durasi (Jam)", "Nomor PC", "Total Biaya"]
        for t in harian:
            table.add_row([t['id'], t['waktu_mulai'], t['durasi'], t['nomor_pc'], f"Rp {t['total_biaya']}"])
        
        print(f"Laporan Pendapatan untuk {tanggal}: Rp {total_pendapatan}")
        print(table)
    except ValueError as e:
        print(f"Error: {e}")

def update_transaksi(id_transaksi, durasi_baru):
    try:
        if id_transaksi not in data['transaksi']:
            raise ValueError("Transaksi tidak ditemukan.")
        if not isinstance(durasi_baru, int) or durasi_baru <= 0:
            raise ValueError("Durasi harus angka positif.")
        t = data['transaksi'][id_transaksi]
        if t['status'] == 'aktif':
            t['durasi'] = durasi_baru
            t['total_biaya'] = HARGA_PER_JAM * durasi_baru
            print(f"Transaksi ID {id_transaksi} diupdate.")
        else:
            print("Transaksi tidak aktif.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_transaksi(id_transaksi):
    try:
        if id_transaksi not in data['transaksi']:
            raise ValueError("Transaksi tidak ditemukan.")
        t = data['transaksi'][id_transaksi]
        t['status'] = 'dibatalkan'
        print(f"Transaksi ID {id_transaksi} dibatalkan.")
    except ValueError as e:
        print(f"Error: {e}")