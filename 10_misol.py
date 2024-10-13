"""Foydalanuvchidan ikkita son kiritishni so'rang. Ularni avval stringga o'girib qo'shing,
keyin integerga o'girib qo'shing va natijalarni solishtiring."""

num1 = int(input("Son kiriting: "))
num2 = int(input("Son kiriting: "))

strPlus = str(num1) + str(num2)
intPlus = num1 + num2
print(f"Str natijasi: {strPlus} \n Int natijasi: {intPlus}")