from turtle import *
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Anime:",["One Piece", "Yu Yu Hakusho", "Fullmetal Alchemist Brotherhood", "Attack on Titan", "Code Geass",
                           "My Hero Academia", "Jujutsu Kaisen"])
table.add_column("My Rating:", ["10", "10", "10", "10", "10", "7", "9"])
table.add_column("Recommend for Beginners?", ["No", "No", "Yes", "Yes", "Yes", "Yes", "Yes"])
table.align = "c"
print(table)