"""Foydalanuvchidan ikkita mahsulotning narxini float shaklda kiritishni so'rang. Qaysi
mahsulot arzon ekanligini aniqlang.​"""

product1 = float(input("Narxni floatda kiriting: "))
product2 = float(input("Narxni floatda kiriting: "))

if product1 > product2:
    print(f"{product2} - arzon")
else:
    print(f"{product1} - arzon")