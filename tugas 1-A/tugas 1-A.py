import math

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3

def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def main():
    print("Pilih operasi:")
    print("1. Menghitung Luas Segitiga")
    print("2. Menghitung Volume Bola")
    print("3. Menghitung Volume Balok")

    operasi = int(input("Masukkan nomor operasi yang dipilih: "))

    if operasi == 1:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = hitung_luas_segitiga(alas, tinggi)
        print("Luas segitiga adalah:", luas)
    elif operasi == 2:
        jari_jari = float(input("Masukkan jari-jari bola: "))
        volume = hitung_volume_bola(jari_jari)
        print("Volume bola adalah:", volume)
    elif operasi == 3:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = hitung_volume_balok(panjang, lebar, tinggi)
        print("Volume balok adalah:", volume)
    else:
        print("Operasi tidak valid.")

if __name__ == "__main__":
    main()
