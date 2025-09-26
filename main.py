# class uy:
#     def __init__(self, uy_raqami, uy_rangi, uy_sotiki, xonalar_soni):
#         self.uy_raqami = uy_raqami
#         self.uy_rangi = uy_rangi
#         self.sotiki = uy_sotiki
#         self.xonalar_soni = xonalar_soni
#     def info(self):
#         return f"{self.raqami} -uy, {self.uy_rangi} rang, {self.uy_sotiki} shuncha {self.xonalar_soni} shuncha"
# uy1 = uy()

# class Kutubxona:
    
#     def __init__(self, nom):
#         self.nom = nom
#         self.kitoblar = {}
    
#     def kitoblar_royxati(self):
#         if len(self.kitoblar):
#             for kitob_nomi, kitob_narxi in self.kitoblar.items():
#                 print(kitob_nomi, kitob_narxi)
#         else:
#             print("kitoblar mavjud emas!")
        
#     def kitob_qoshish(self, kitob_nomi, kitob_narxi):
#         self.kitoblar[kitob_nomi] = kitob_narxi
#         print(f"yangi: {kitob_nomi} kitobi muvofavqiyatli qo'shildi.")

# kutubxona_1 = Kutubxona("davlat 1-kutubxonasi")
# # kutubxona_1.kitoblar_royxati()
# kutubxona_1.kitob_qoshish("O'tkan kunlar", 50000)
# kutubxona_1.kitob_qoshish("Yulduzli tunlar", 90000)
# kutubxona_1.kitob_qoshish("COC", 30000)
# # kutubxona_1.kitoblar_royxati()
# kutubxona_2 = Kutubxona("kichik kutubxonacha")
# kutubxona_2.kitoblar_royxati()

# class Talaba:
#     def __init__(self, ism, yosh, universitet_nomi = "Tatu"):
#         self.ism = ism
#         self.yosh = yosh
#         self.universitet_nomi = universitet_nomi
#     def ismi(self):
#         return f"{self.ism} uning ismi"
#     def yoshi(self):
#         return f"{self.yosh} uning yoshi shu"
#     def institut(self):
#         return f"{self.universitet_nomi} u shu yerda o'qiydi"
    

# talaba1 = Talaba("ali", 22, "INHA")
# print(talaba1.ismi())
# print(talaba1.yoshi())
# talaba2 = Talaba("Toshmat", 19)

# print(talaba2.institut())


# class car:
#     def __init__(self, model, narx, rang, tezlik):
#         self.model = model 
#         self.narx = narx
#         self.rang = rang
#         self.tezlik = tezlik
#     def get_modeli(self):
#         return f"mashina modeli {self.model}"
#     def get_narxi(self):
#         return f"{self.model} narxi ${self.narx}"
#     def get_rangi(self):
#         return f"{self.model} rangi {self.rang} rangda"
#     def get_tezlik(self):
#         return f"{self.model} max tezligi soatiga {self.tezlik} km/s"

# car1 = car("BMW", 30000, "ko'k", 260)
# print(car1.get_modeli())
# print(car1.get_narxi())
# print(car1.get_rangi())
# print(car1.get_tezlik())
# car2 = car("MERS", 20000, "qora", 200)
# print(car2.get_modeli())
# print(car2.get_narxi())
# print(car2.get_rangi())
# print(car2.get_tezlik())
# car3 = car("DOODGE", 24000, "sariq", 240)
# print(car3.get_modeli())
# print(car3.get_narxi())
# print(car3.get_rangi())
# print(car3.get_tezlik())


# class Car:
#     nom = "default"
#     def __init__(self, nom):
#         self.nom = nom
    

#     def info(self):
#         return self.nom

#     @classmethod
#     def class_method_info(self):
#         return self.nom
    
#     @staticmethod
#     def static_method_info():
#         return "shunchaki metod"

# car1 = Car("nexia")
# print(car1.info())
# print(car1.class_method_info())
# print(car1.static_method_info())
# print(Car("1").static_method_info())


# class maktab:
#     def __init__(self, nomi, manzil, oquvchilar_ismi, direktor_ismi):
#         self.nomi = nomi
#         self.manzil = manzil
#         self.oquvchilar_ismi = oquvchilar_ismi
#         self.direktor_ismi =direktor_ismi
#     def nomi(self):
#         return f"{self.nomi} {self.manzil} {self.oquvchilar_ismi} {self.direktor_ismi}"
# maktab1 = maktab(203, "uchtepa", "asilbek", "eshmat")
# print(maktab1)

class oquvchi:
    def __init__(self, ism, manzil, baho=1, yosh=1):
        self.ism = ism
        self.manzil = manzil
        self.baho = baho
        self.yosh = yosh
    def get_ism(self):
        return f"{self.ism}"
    def get_manzil(self):
        return f"{self.manzil}"
    def get_baho(self):
        return f"{self.baho}"
    def get_yosh(self):
        return f"{self.yosh}"
oquvchi1 = oquvchi("aziz", "bogdod")
print(oquvchi1.get_ism())
print(oquvchi1.get_manzil())
oquvchi2 = oquvchi("shahlo", "russia")
print(oquvchi2.get_ism())
print(oquvchi2.get_manzil())
 