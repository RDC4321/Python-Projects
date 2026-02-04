from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Level", [5, 7, 10])
table.align["Pokemon Name"] = "c"
table.align["Type"] = "c"
table.align["Level"] = "c"

print(table)