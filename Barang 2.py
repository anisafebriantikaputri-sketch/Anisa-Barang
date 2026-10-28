print("=" * 50)
print("     KASIR MINIMARKET - CEK DISKON MEMBER")
print("=" * 50)

nama_pembeli = input("Nama Pelanggan\t\t\t: ")
print(nama_pembeli)
input_kartu = input("Punya Kartu Member? (y/t)\t: ").strip().lower()
print(input_kartu)

try:
  total_belanja = int(
      input("Masukkan Total Belanja (Rp)\t: Rp ").replace(".", "").replace(",", "")
  )
  print(total_belanja)
except ValueError:
  total_belanja = 0

A = total_belanja >= 100000
b = (input_kartu == 'y')

dapat_diskon = A or b

print("\n" + "=" * 50)
print("                STRUK PENGECEKAN")
print("=" * 50)
print(f"Pelanggan        : {nama_pembeli}")
print(f"Belanja >= 100rb (A): {A}")
print(f"Punya Member (b)     : {b}")
print(f"Total Belanja    : Rp {total_belanja:,}".replace(",", "."))
print("-" * 50)

if dapat_diskon:
  print(f"Hasil            : Selamat {nama_pembeli}, Anda berhak")
  print("                   mendapatkan diskon khusus!")
else:
  print(f"Hasil            : Maaf {nama_pembeli},")
  print("                   kamu tidak mendapatkan diskon")
  print("                   khusus untuk pemilik kartu member.")

print("=" * 50)