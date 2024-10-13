"""Foydalanuvchidan ikkita son kiritishni so'rang. Ushbu sonlar ustida qo'shish, ayirish,
ko'paytirish, bo'lish va darajaga ko'tarish amallarini bajaring va natijalarni ekranga
chiqaring."""

num1 = int(input("Son kiriting: "))
num2 = int(input("Son kiriting: "))

qoshish = num1 + num2
ayirish = num1 - num2
bolish = num1 / num2
kopaytirish = num1 * num2
qoldiq = num1 % num2

print(f"{num1} + {num2} = {qoshish}")
print(f"{num1} - {num2} = {ayirish}")
print(f"{num1} / {num2} = {bolish}")
print(f"{num1} * {num2} = {kopaytirish}")
print(f"{num1} % {num2} = {qoldiq}")