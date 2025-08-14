from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S21", "+7 900 000 00 00"),
    Smartphone("Apple", "Iphon 16", "+7 900 000 00 01"),
    Smartphone("LG", "G63", "+7 900 000 00 02"),
    Smartphone("Huawei", "H7", "+7 900 000 00 03"),
    Smartphone("Pokko", "P53Plus", "+7 900 000 00 04")
]

for smartfone in catalog:
    print(f"{smartfone.mark_fone} - {smartfone.model_fone}. {smartfone.number_fone}")
