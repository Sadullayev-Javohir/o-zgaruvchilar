"""Foydalanuvchidan ismingiz, yoshingiz va sevimli rangingizni so'rang. Olingan ma'lumotlar
bilan quyidagi formatda matn chiqaring: Salom, [ism]. Siz [yosh] yoshdasiz va sizning
sevimli rangingiz [rang]."""

firstName = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))
likeColor = input("Sevimli rangingizni kiriting: ")
print(f"Salom, {firstName}. Siz {age} yoshdasiz va sizning sevimli rangingiz {likeColor}.")
