import random

welcome_message = "WELCOME TO CUYPY GAMES"
cuypy_position = random.randint(1, 4)

print("****************************")
print(f"** {welcome_message} **")
print("****************************")

nama_user = input("Masukkan nama kamu: ")
print(f"Halo {nama_user}, coba perhatikan kolom di bawah ini |_| |_| |_| |_|")

while True:
    try:
        pilihan_user = int(input("Menurut kamu di goa nomor berapa yang ada isinya? [1 / 2 / 3 / 4]: "))
        if pilihan_user not in [1, 2, 3, 4]:
            print("Masukkan angka antara 1 hingga 4.")
            continue

        konfirmasi = input(f"Apakah kamu yakin dengan pilihanmu {pilihan_user}? Y/N: ").upper()
        if konfirmasi == "Y":
            break
        elif konfirmasi == "N":
            print("Tidak yakin? Coba lagi!")
        else:
            print("Input tidak valid, silakan masukkan Y atau N.")
    except ValueError:
        print("Input tidak valid, masukkan angka yang benar.")

print()

if pilihan_user == cuypy_position:
    print(f"Selamat {nama_user}, kamu menang! Posisi Cuypy ada di {cuypy_position} dan pilihanmu adalah nomor {pilihan_user}.")
else:
    print(f"Pilihan kamu tidak ada isinya, posisi Cuypy sebenarnya ada di nomor {cuypy_position}.")
