"""Foydalanuvchi biror matn kiritadi. Shu matnni quyidagicha ekranga chiqaring:
katta harflarda, kichik harflarda, sarlavha usulida (title), birinchi harfini katta qilib."""

word = input("So'z kiriting: ")
print(f"Upper {word.upper()}")
print(f"Lower {word.lower()}")
print(f"Title {word.title()}")
print(f"Capitalize {word.capitalize()}")
