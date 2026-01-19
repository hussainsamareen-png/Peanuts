# data/*.json --> ignore file command.

import json
with open("data\A_people.json", encoding='utf-8') as file:
    Apeople= json.load(file)


# abc= ['A',"B", "C", 'D', 'E', 'F', 'G', "H",
#        'I', 'J', 'K', 'L', "M", "N", "O", 'P',
#          "Q", "R", 'S', 'T', "U", "V", 'W', 'X', "Y", "Z"]

# for letter in abc:
#     with open(f"data\People\{letter}_people.json", encoding='utf-8') as file:
#     people= json.load(file)