import re

def baca_artikel(nama_file):
    with open(nama_file, 'r', encoding='utf-8') as file:
        return file.read()

def cari_kata(artikel, kata_dicari):
    artikel_lower = artikel.lower()
    kata_dicari_lower = kata_dicari.lower()
    jumlah = len(re.findall(r'\b' + kata_dicari_lower + r'\b', artikel_lower))
    return f"kata '{kata_dicari}' ditemukan sebanyak {jumlah} kali"

def ganti_kata(artikel, kata_lama, kata_baru):
    def pengganti(match):
        if match.group(0).isupper():
            return kata_baru.upper()
        elif match.group(0)[0].isupper():
            return kata_baru.capitalize()
        return kata_baru
    
    hasil = re.sub(r'\b' + kata_lama + r'\b', pengganti, artikel, flags=re.IGNORECASE)
    return hasil

def urut_kata(artikel):
    kata_list = re.findall(r'\b\w+\b', artikel.lower())
    kata_unik = sorted(set(kata_list))
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
