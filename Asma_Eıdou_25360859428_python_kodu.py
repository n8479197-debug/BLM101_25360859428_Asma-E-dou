# Brookshear makinesi için HEX karakterler
HEX = "0123456789ABCDEF"

def decode():
    # Kullanıcıdan 4 haneli HEX kodu al
    kod = input("4 haneli HEX kodu giriniz: ").upper()

    # Uzunluk kontrolü
    if len(kod) != 4:
        print("Hatalı giriş! Kod 4 haneli olmalıdır.")
        return

    # HEX karakter kontrolü
    for h in kod:
        if h not in HEX:
            print("Hatalı giriş! Sadece 0-9 ve A-F kullanılabilir.")
            return

    # Kodu parçalara ayır
    opcode = kod[0]          # işlem kodu
    register = kod[1]        # kaydedici numarası
    address = kod[2] + kod[3]  # bellek adresi (2 haneli)

    # Opcode’a göre yorumlama
    if opcode == "1":
        # LOAD from memory
        print(f"{address} adresindeki bellek hücresinin içeriğini, "
              f"{int(register, 16)} numaralı kaydediciye yükle.")

    elif opcode == "2":
        # LOAD immediate
        print(f"{address} değerini, "
              f"{int(register, 16)} numaralı kaydediciye yükle.")

    elif opcode == "3":
        # STORE to memory
        print(f"{int(register, 16)} numaralı kaydedicideki veriyi, "
              f"{address} adresine kaydet.")

    elif opcode == "4":
        # MOVE register to register
        print(f"{int(kod[2], 16)} numaralı kaydedicinin içeriğini, "
              f"{int(kod[3], 16)} numaralı kaydediciye kopyala.")

    elif opcode == "5":
        # ADD registers
        print(f"{int(kod[2], 16)} ve {int(kod[3], 16)} numaralı kaydedicileri topla, "
              f"sonucu {int(register, 16)} numaralı kaydediciye yaz.")

    elif opcode == "6":
        print("Mantıksal VE (AND) işlemi.")

    elif opcode == "7":
        print("Mantıksal VEYA (OR) işlemi.")

    elif opcode == "8":
        print("Mantıksal ÖZEL VEYA (XOR) işlemi.")

    elif opcode == "9":
        print("Koşullu dallanma (branch) işlemi.")

    elif opcode == "A":
        print("Kaydırma (shift) işlemi.")

    elif opcode == "B":
        print("Alt program çağrısı.")

    elif opcode == "C":
        # HALT
        print("Program durduruldu (HALT).")

    else:
        print("Bu opcode desteklenmiyor.")


# Programı çalıştır
decode()