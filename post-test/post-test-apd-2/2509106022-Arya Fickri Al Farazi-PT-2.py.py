nama = input("Nama pasien\t\t: ")
tinggi_badan = float(input("Tinggi badan (cm)\t: "))
berat_badan = float(input("Berat badan (kg)\t: "))


berat_ideal = tinggi_badan - 100
status_list = ["Normal", "Kelebihan Berat Badan"]
status = status_list[int(berat_badan > berat_ideal)]


print("-" * 60)
print(f"| {'HASIL CEK BERAT BADAN':^56} |")
print("-" * 60)
print(f"| Nama Pasien\t: {nama:<40} |")
print(f"| Tinggi Badan\t: {tinggi_badan:<6.1f} cm{'':<31} |")
print(f"| Berat Badan\t: {berat_badan:<6.1f} kg{'':<31} |")
print(f"| Berat Ideal\t: {berat_ideal:<6.1f} kg{'':<31} |")
print(f"| Status\t: {status:<40} |")
print("-" * 60)                        