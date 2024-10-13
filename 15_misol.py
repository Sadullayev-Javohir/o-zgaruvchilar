"""Foydalanuvchidan aylananing radiusini float shaklda kiritishni so'rang. Aylananing uzunligi
va yuzasini hisoblang (π = 3.14 deb oling).​"""

R = float(input("Radiusni floatda kiriting: "))
Pi = 3.14
L = 2 * Pi * R
S = Pi * (R ** 2)
print(f"Aylananing uzunligi: {L}\nYuzasi: {S}")