from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.ukuran = ukuran

    def info_Ikan(self):
        super().info_animal()
        print("habitat \t: ", self.habitat, 
              "\nUkuran \t: ", self.ukuran)

# Membuat objek dari kelas Ikan
Ikan_Hiu = Ikan("Hiu", "Daging", "Laut", "Telur", "Laut", "Besar")
Ikan_Hiu.info_Ikan()
print("==========================================")
Ikan_Mas = Ikan("Mas", "Pakan Ikan", "Air Tawar", "Telur", "Kolam", "Kecil")
Ikan_Mas.info_Ikan()