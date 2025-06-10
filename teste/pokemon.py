from prettytable import PrettyTable

x = PrettyTable(["Pokémon", "Class"])
x.add_rows(
    [
        ["Pikachu", "Eletric"],
        ["Squirtle", "Water"]
    ]
)

x.padding_width = 5
x.align = "l"

print(x)