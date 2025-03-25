nilai_siswa = (
    ("Reza", 85),
    ("Andriana", 90),
    ("Rusdi", 78),
    ("Ambatukam", 92)
)

def cetak_nilai_siswa(nilai_siswa):
    print("Nama Siswa\tNilai")
    for siswa in nilai_siswa:
        print(f"{siswa[0]}\t\t{siswa[1]}")

cetak_nilai_siswa(nilai_siswa)
