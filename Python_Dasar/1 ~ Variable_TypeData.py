# Komentar diawali dengan tanda pagar #, Komentar ini tidak akan dijalankan
# Variable tidak boleh dimulai dengan nomor
# Variable tidak boleh ada spasi
# Variable tidak boleh menggunakan simbol
# Penamaan Variable untuk python umumnya menggunakan snake case (contoh_variable)

# Deklarasi Variable
angka_pertama = 10

# Integer
integer = 1
print(integer)

# Float
float = 1.5
print(float)

# Di String, List, dan Tuple ada yang namanya index / nomor penempatan Value atau Isi
# Index diawali dari nomor / angka 0
# Pada contoh dibawah index 0 berisi angka 1, index 1 berisi "apa" dan seterusnya
# Index juga bisa dihitung dari belakang dengan cara memberikan nilai minus (-)
# Jika ingin memunculkan Value atau Isi pada index tertentu maka tinggal panggil seperti ini
# nama_variable[index]

# String
string = "halo"
print(string)
print(string[0])
print(string[-1])

# List ~ Value atau Isi dapat diubah
list = [1, "apa", 1, "apa"]
print(list)
print(list[0])
print(list[-1])

# Tuple ~ Value atau Isi tidak dapat diubah
tuple = (1, "apa", 1, "apa")
print(tuple)

# Set ~ Value atau isi tidak dapat diubah tetapi bisa dikurangi atau ditambah
# Nilai yang double tidak akan dimunculkan
# Bersifat unorderable sehingga tidak berlaku index
set = {"a", "b", "a"}
print(set)

# Dictionary
# Mempunyai Key dan Value
# Key harus menggunakan string
# Jika ingin memanggil atau memunculkan atau mencetak nilai tertentu
# Gunakanlah key

dict = {
    "nama": "aku",
    "umur": 100
}
print(dict)
print(dict["nama"])

# Boolean hanya berisi True atau False
bool = True
print(bool)