money = float(input("введите сумму: "))

per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}

TKB = float((per_cent['TKB']) * (money / 100))
SKB = float((per_cent['TKB']) * (money / 100))
VTB = float((per_cent['TKB']) * (money / 100))
SBER = float((per_cent['TKB']) * (money / 100))

print(TKB)
print(SKB)
print(VTB)
print(SBER)

letters = [TKB, SKB, VTB, SBER]
print("Максимальная сумма, которую вы можете заработать", max(letters))
