def baca_artikel(nama_file):
    with open(nama_file, 'r', encoding='utf-8') as file:
        return file.read()

def cari_kata(artikel, kata_dicari):
    artikel_lower = artikel.lower()
    kata_dicari_lower = kata_dicari.lower()
    # Pisahkan artikel menjadi kata-kata
    kata_list = artikel_lower.split()
    # Hitung kemunculan kata persis
    jumlah = sum(1 for kata in kata_list if kata.strip('.,!?()[]{}:;"\'') == kata_dicari_lower)
    return f"kata '{kata_dicari}' ditemukan sebanyak {jumlah} kali"

def ganti_kata(artikel, kata_lama, kata_baru):
    artikel_kata = artikel.split()
    hasil_kata = []

    for kata in artikel_kata:
        kata_bersih = kata.strip('.,!?()[]{}:;"\'')
        tanda = kata[len(kata_bersih):] if len(kata) > len(kata_bersih) else ''
        
        if kata_bersih.lower() == kata_lama.lower():
            if kata_bersih.isupper():
                kata_baru_fix = kata_baru.upper()
            elif kata_bersih[0].isupper():
                kata_baru_fix = kata_baru.capitalize()
            else:
                kata_baru_fix = kata_baru
            hasil_kata.append(kata_baru_fix + tanda)
        else:
            hasil_kata.append(kata)
    return ' '.join(hasil_kata)

def urut_kata(artikel):
    artikel_lower = artikel.lower()
    kata_list = artikel_lower.split()
    # Hapus tanda baca
    kata_bersih = [kata.strip('.,!?()[]{}:;"\'') for kata in kata_list]
    kata_unik = sorted(set(kata_bersih))
    return kata_unik

def main():
    artikel = baca_artikel('artikel.txt')
    
    while True:
        print("\nMenu Pilihan:")
        print("1. Cari kata")
        print("2. Ganti kata")
        print("3. Urutkan kata")
        print("4. Keluar")
        
        pilihan = input("masukkan pilihan 1-4: ")
        
        if pilihan == '1':
            kata_dicari = input("masukkan kata yang ingin dicari: ")
            print(cari_kata(artikel, kata_dicari))
            
        elif pilihan == '2':
            kata_lama = input("masukkan kata yang ingin diganti: ")
            kata_baru = input("masukkan kata pengganti: ")
            artikel_baru = ganti_kata(artikel, kata_lama, kata_baru)
            print("\nhasil penggantian:")
            print(artikel_baru)

            simpan = input("simpan ke file baru (artikel_baru.txt)? (y/n): ")
            if simpan.lower() == 'y':
                with open('artikel_baru.txt', 'w', encoding='utf-8') as file:
                    file.write(artikel_baru)
            
        elif pilihan == '3':
            kata_urut = urut_kata(artikel)
            print("\ndaftar kata terurut:")
            for kata in kata_urut:
                print(kata)
            
        elif pilihan == '4':
            print("terima kasih!")
            break
            
        else:
            print("pilihan tidak valid!")

if __name__ == "__main__":
    main()

