from prettytable import PrettyTable

table = PrettyTable()

table.add_column("pokemonn",["pika","squi","char"])

table.add_column("type",["elec","water","fire"])

table.align = "l"

print(table)