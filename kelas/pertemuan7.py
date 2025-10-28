# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)

# luas_persegi(4)
# volume_persegi(6)

# def faktorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")

# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
# menu = input("PILIH MENU> ")
# print ("\n")

# if menu == "1":
#     show_data()
# elif menu == "2":
#     insert_data()
# elif menu == "3":
#     edit_data()
# elif menu == "4":
#     delete_data()
# elif menu == "5":
#     exit()
# else:
#     print ("Salah pilih!")

# # Fungsi untuk menampilkan semua data
# film = []
# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#     for indeks in range(len(film)):
#         print(indeks, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")

#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")

# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     else:
#         print('Tidak ada di menu')


# while True():
#     show_menu()

# try:
#     angka = int(input('Masukkan Angka\t: '))
# except ValueError:
#     print('input bukan berupa angka')
# else :
#     print(angka)

# try:
#     usn = input('Username : ')
#     if len(usn) < 0 or usn.strip() == '':
#         raise ValueError('input nama tidak boleh kosong atau hanya berisi spasi saja.')
# except ValueError as e:
#     print(e)

