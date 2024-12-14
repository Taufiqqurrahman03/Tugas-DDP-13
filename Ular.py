from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,berbisa,warna,):
      super().__init__(nama, makanan, hidup, berkembang_biak)
      self.berbisa = berbisa 
      self.warna = warna
   
    def info_ular(self):
       super().info_animal(),
       print(" berbisa \t\t : " , self.berbisa,
             "\n warnanya \t\t : " ,self.warna)
       
Ular_piton = Ular("piton","tikus","didarat","bertelur","tidak","Hijau Hitam")
Ular_piton.info_ular()
print("==========================================================")
Ular_cobra = Ular("king cobra","Tikus","Didarat","Bertelur","ya","hitam")
Ular_cobra.info_ular()

    