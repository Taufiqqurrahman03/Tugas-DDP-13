from Animal import Animal

class ikan(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,Warna,bisa_dimakan):
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.Warna = Warna
        self.bisa_dimakan = bisa_dimakan

    def info_ikan(self):
        super().info_animal(),
        print("warna \t\t\t : ",self.Warna ,
        "\n bisa dimakan \t\t : ",self.bisa_dimakan)

ikan_mas = ikan("ikan mas","pelet","air","bertelur","emas","bisa")
ikan_mas.info_ikan()
print("==================================================================")
ikan_pausorca = ikan ("Paus Orca","plankton","laut","melahirkan","hitam putih","bisa")
ikan_pausorca.info_ikan()