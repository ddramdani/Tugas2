# Membuat program sederhana prnjulan tiket transportasi
while True:     
    print("="*20,"TIKET TRASFORTASI BUS","="*20)
# input user
    nama = input("Nama Pembeli\t = ")
    kode = input("Kode Jurusan\n1. Bandung\n2. Jakarta\n3. Jogyakarta\n   = ")
    jumlah =int(input("Jumlah Tiket\t = "))
    
# looping / perulangan
    if kode == "1":
        kota = "Bandung"
        harga = 150000
    elif kode == "2":
        kota = "Jakarta"
        harga = 200000
    elif kode == "3":
        kota = "Yogyakarta"
        harga = 450000
    else:
        print("Pilih Kota Tujuanmu")
# rumus 
    total = (jumlah*harga)
# output
    print("="*20,"TIKET TRASFORTASI BUS","="*20)
    print(f"Nama Pembeli = {nama}")
    print(f"Kode Jurusan = {kode}")
    print(f"Kota Tujuan = {kota}")
    print(f"Jumlah Tiket = {jumlah}")
    print(f"Total Pembayaran Tiket = Rp. {total}")
    
    selesai = input("Beli Tiket Lagi? (Y/N) = ")
    if selesai == "N":
        break
print("="*21,"SELAMAT SAMPAI TUJUAN","="*21)




