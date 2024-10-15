"""Foydalanuvchidan son kiritishni so'rang va shu son 10 dan katta yoki kichikligini
tekshirib, natijani True yoki False sifatida ekranga chiqaring.​"""

num = int(input("Son kiriting: "))

# if num > 10:print(True)
# else: print(False)

print(f" 10 dan katta {num > 10}")
print(f" 10 dan kichik {num <= 10}")