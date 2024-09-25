"""
 LATIHAN 1 PRAKTIKUM PBO RD 
 NAMA : EDWIN DARREN HASANNUDIN
 NIM : 122140111
"""

# # Latihan 

# # kalkulator sederhana  
# print(20*"=")
# print("Kalkulator Sederhana")
# print(20*"=" + "\n")

# angka_1 = float(input("masukan angka 1 = "))
# operator = input("operator (+,-,x,/) : ")
# angka_2 = float(input("masukan angka 2 = "))

# # percabangannya 

# if operator == "+":
#     hasil = angka_1 + angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "-":
#     hasil = angka_1 - angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "x" or operator == "*": 
#     hasil = angka_1 * angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "/": 
#     hasil = angka_1 / angka_2
#     print(f"hasilnya adalah {hasil}")
# else: 
#     print("masukan yang bener dong!, aku pusying")

# print("Akhir dari program!")

# while True: print(eval(input("Input : ")))

def tambah(angka_1, angka_2):
    return angka_1 + angka_2

def kurang(angka_1, angka_2):
    return angka_1 - angka_2

def kali(angka_1, angka_2):
    return angka_1 * angka_2

def bagi(angka_1, angka_2):
    if angka_2 != 0:
        return angka_1 / angka_2
    else:
        return "Error: Pembagian oleh 0"

def kalkulator_sederhana():
    while True:
        print(20 * "=")
        print("Kalkulator Sederhana")
        print(20 * "=" + "\n")

        angka_1 = float(input("Masukkan angka 1 = "))
        operator = input("Operator (+, -, x, /) atau ketik 'exit' untuk keluar: ")

        if operator.lower() == 'exit':
            print("Terima kasih, program kalkulator selesai.")
            break

        angka_2 = float(input("Masukkan angka 2 = "))

        if operator == "+":
            hasil = tambah(angka_1, angka_2)
        elif operator == "-":
            hasil = kurang(angka_1, angka_2)
        elif operator == "x" or operator == "*":
            hasil = kali(angka_1, angka_2)
        elif operator == "/":
            hasil = bagi(angka_1, angka_2)
        else:
            hasil = "Masukan yang benar dong!, aku pusying"

        print(f"Hasilnya adalah {hasil}")

# Panggil fungsi kalkulator_sederhana
kalkulator_sederhana()
