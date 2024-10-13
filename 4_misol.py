"""Foydalanuvchi bo'shliqlar bilan boshlangan va tugagan biror mattni kiritadi.
Shu matndan barcha bo'shliqlarni olib tashlang. faqat o'ng yoki chap tomondagi
bo'shliqlarni olib tashlab natijani ekranga chiqaring. """

space_word = input("Bo'shliq so'z kiriting: ")
print(f"Strip {len(space_word.strip())}")
print(f"Right Strip {len(space_word.rstrip())}")
print(f"Left Strip {len(space_word.lstrip())}")