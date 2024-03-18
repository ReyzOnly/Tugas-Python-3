
def hitung_imt(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan ** 2)

def tentukan_status_gizi(imt):
    if imt < 18.5:
        return "Kurus"
    elif 18.5 <= imt < 25:
        return "Normal"
    elif 25 <= imt < 30:
        return "Gemuk"
    else:
        return "Obesitas"

def main():
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (m): "))

    imt = hitung_imt(berat_badan, tinggi_badan)

    status_gizi = tentukan_status_gizi(imt)

    print("IMT Anda adalah:", imt)
    print("Status gizi Anda adalah:", status_gizi)

if __name__ == "__main__":
    main()
