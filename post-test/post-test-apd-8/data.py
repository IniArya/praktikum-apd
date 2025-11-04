from datetime import datetime
# Data global untuk menyimpan users dan transaksi
data = {
    'users': {},
    'transaksi': {}
}
# Konstanta
HARGA_PER_JAM = 12000
MAX_PC = 10
# Inisialisasi admin default
if 'admin' not in data['users']:
    data['users']['admin'] = {'password': '123', 'role': 'admin'}