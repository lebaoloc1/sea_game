print("\nViet Nam\n")
vie_gold = int(input("Please enter the number of gold medals: "))
vie_silver = int(input("Please enter the number of silver medals: "))
vie_bronze = int(input("Please enter the number of bronze medals: "))
vie_score = vie_gold * 3 + vie_silver * 2 + vie_bronze

print("\nSingapore\n")
sin_gold = int(input("Please enter the number of gold medals: "))
sin_silver = int(input("Please enter the number of silver medals: "))
sin_bronze = int(input("Please enter the number of bronze medals: "))
sin_score = sin_gold * 3 + sin_silver * 2 + sin_bronze

print("\nNational\tGold\tSilver\tBronze\tScore")
print(f"Viet Nam \t{vie_gold}\t{vie_silver}\t{vie_bronze}\t{vie_score}")
print(f"Singapore \t{sin_gold}\t{sin_silver}\t{sin_bronze}\t{sin_score}")