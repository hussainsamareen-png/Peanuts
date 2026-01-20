import json

allpeople=[]
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"data/{letter}_people.json", encoding='utf-8') as file:
        people= json.load(file)
        for dict in people:
            if "ontology/profession_label" in dict:
                # print(str(dict["ontology/profession_label"]))
                if "ontology/religion_label" in dict:
                    allpeople.append(dict)

data = [
    ["Religion", "Profession"],

]

for dict in allpeople:
    if type(dict["ontology/religion_label"]) is list:
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/religion_label"]:
                rel=item
                for item in dict["ontology/profession_label"]:
                    onto=item
                    entry=[]
                    entry.append(rel)
                    entry.append(onto)
                    data.append(entry)
        else:
            for item in dict["ontology/religion_label"]:
                entry=[]
                entry.append(item)
                entry.append(dict["ontology/profession_label"])
                data.append(entry)
    else:
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["ontology/religion_label"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["ontology/religion_label"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
        


print(data)
import csv

with open('profession_by_religion.csv', mode='w',  newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)