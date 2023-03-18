# Ini adalah Lanjutan Dari String Type Data

# Enter atau Garis Baru pada String bisa menggunakan \n
print("Hello \nWorld")

# Penggunaan Petik Satu atau Dua tergantung kondisi
# Misalnya ketika ingin mencetak kata Jum'at itu mengharuskan Petik Dua
# Jika menggunakan petik satu
# print('Jum'at') ini akan error
print("Jum'at")

# Mengetahui Jumlah Karakter String
# Gunakan Len() untuk mengetahui jumlahnya, spasi juga ikut terhitung
print(len("Apakah Hari Ini Hari Minggu ?"))

# Mengambil beberapa Karakter Tertentu dalam Index
# Berlaku juga untuk mengambil index dari belakang
# Abaikan Value 2 Index, yang artinya Index 0,1 tidak akan dimunculkan
abjad = "abcdefghijklmn"
print(abjad[2:])

# Abaikan Seluruh Value Index kecuali 2 Index dari belakang
print(abjad[-2:])

# Ambil Value 2 Index, yang artinya hanya Index 0,1 yang dimunculkan
print(abjad[:2])

# Ambil Seluruh Value Index kecuali 2 Index dari belakang
print(abjad[:-2])

# Ambil Value Index dari Index 2 sampai Index 5
print(abjad[2:5])

# Ambil Value Index dengan loncatan 2
# Index 0 diambil Index 1 diabaikan Index 2 diambil dan seterusnya
print(abjad[::2])

# Ambil Value Index dari Index 2 sampai Index 7 dengan loncatan 2
print(abjad[2:7:2])

# Membalikan Karakter yang akhir jadi awal dan awal jadi akhir
print(abjad[::-1])

# String bisa menggunakan Operator
sapa = "Hello "
print(sapa * 10)

# Merubah style String
# Upper untuk huruf besar semua
# Lower untuk huruf kecil semua
kata = "Aku adalah Manusia"
print(kata.upper())
print(kata.lower())

# Merubah String menjadi List
print(kata.split())

# Merubah String menjadi List dengan huruf a kecil sebagai pemisah
print(kata.split("a"))

# Memasukan String lain dengan metode format
print("Aku adalah {}".format("Manusia"))

# Bisa juga menggunakan tuple
print("Apa {} yang {} {}".format("itu", "terjadi", "lagi"))

# Bisa juga menggunakan indeksnya
print("Apa {2} yang {0} {1}".format("itu", "terjadi", "lagi"))
print("Apa {0} yang {0} {0}".format("itu", "terjadi", "lagi"))

# Bisa juga menggunakan key value
print("Apa {tiga} yang {dua} {satu}".format(satu="itu", dua="terjadi", tiga="lagi"))

# Bisa juga digabungkan dengan formating float atau integer
angka = 100 / 77
print("Ini hasil tanpa format {}".format(angka))
print("Ini hasil dengan format {a:1.3f}".format(a=angka))

# Memasukan variable dengan tambahan huruf f
# Ini berlaku di python versi 3.6 katas
nama = "zilong"
hobi = "makan"
print(f"Halo saya {nama} hobi saya {hobi}")