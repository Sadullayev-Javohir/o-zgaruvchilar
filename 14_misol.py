"""Foydalanuvchidan to'rtburchakning uzunligi va eni kiritilishini so'rang. To'rtburchakning
perimetrini va yuzasini hisoblang."""

width = int(input("uzunligini kiriting: "))
height = int(input("uzunligini kiriting: "))

P = 2 * (width + height)
S = width * height

print(f"To'rtburchakning perimetri: {P} \nYuzasi: {S}")