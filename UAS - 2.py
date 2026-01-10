import random

def permainan_tebak_angka():
    while True:
        # Pilih angka rahasia secara acak dari 1 hingga 100
        angka_rahasia = random.randint(1, 100)
        kesempatan = 5  # Jumlah maksimal tebakan
        
        print("\nAngka rahasia sudah dipilih (1-100). Tebak sekarang!")
        
        while kesempatan > 0:
            # Minta input tebakan dari pemain
            try:
                tebakan = int(input("Masukkan tebakan Anda: "))
            except ValueError:
                print("Input harus angka! Coba lagi.")
                continue
            
            # Berikan petunjuk berdasarkan tebakan
            if tebakan == angka_rahasia:
                print("Benar! 🎉 Anda menang.")
                break
            elif tebakan < angka_rahasia:
                print("Terlalu kecil! Coba angka lebih besar.")
            else:
                print("Terlalu besar! Coba angka lebih kecil.")
            
            kesempatan -= 1
            print(f"Kesempatan tersisa: {kesempatan}")
        
        # Jika kesempatan habis tanpa tebakan benar
        if kesempatan == 0:
            print(f"Kesempatan habis! Angka rahasia: {angka_rahasia}")
        
        # Tanya apakah ingin main lagi
        ulang = input("Main lagi? (ya/tidak): ").lower()
        if ulang != 'y':
            print("Terima kasih telah bermain!")
            break

# Jalankan permainan
permainan_tebak_angka()