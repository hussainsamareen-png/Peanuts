import json
# Filtering for people with an entry of profession and religion by labels
allpeople=[]
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"data/{letter}_people.json", encoding='utf-8') as file:
        people= json.load(file)
        for dict in people:
            if "ontology/profession_label" in dict:
                # print(str(dict["ontology/profession_label"]))
                if "ontology/religion_label" in dict:
                    allpeople.append(dict)

# Creating final python data table
data = [
    ["Religion", "Profession"],

]

# Creating exhaustive list of some religions that we want to filter
christian=["Christianity", "Catholic Church", "Espiscopal", "Eastern Orthodox Church", "Protestant", "Methodism", "Quaker", "Lutheranism", "Espiscopal", "Presbyterianism", "Russian Orthodox Church", "Presbyterian Church", "Church of England", "Baptists", "Christian", "Catholicism", "Roman Catholic Church", "Anglicanism", "Congregational Church", "Church of God Ministry of Jesus Christ International", "Serbian Orthodox Church", "Greek", "Baptists", "United Methodist Church", "Protestantism", "Universalist Church of America", "Romanian Orthodox Church", "Armenian Apostolic Church", "Dutch Reformed Church", "Methodist Episcopal Church", "Assemblies of God", "The Church of Jesus Christ of Latter-day Saints", "Born again (Christianity)", "Orthodox Autocephalous Church of Albania", "Catholic Church in the Philippines", "Independent Church", "United Church of Canada", "Evangelicalism", "Church of Sweden", "Traditionalist Catholic", "Nondenominational Christianity", "Southern Baptist Convention", "Mormons", "Church of the United Brethren in Christ", "Episcopal Church (United States)", "Anglican Church of Australia", "Church of Greece", "African Methodist Episcopal Zion Church", "Christian Church (Disciples of Christ)", "Evangelical Lutheran Church of Finland", "Church of the Nazarene", "Church of God Ministry of Jesus Christ International", "Maronite Church", "Presbyterian Church in Ireland", "Evangelical Church in Germany", "Southern Baptist Convention", "Free Presbyterian Church of Ulster", "Remonstrants", "Churches of Christ", "New Hope Christian Fellowship", "Church of Norway", "Pentecostalism", "Cumberland Presbyterian Church", "Presbyterian Church (USA)", "Mennonite", "Calvinism", "Seventh-day Adventist Church", "Reformed Churches in South Africa", "Orthodox Autocephalous Church of Albania", "Coptic Orthodox Church of Alexandria", "Charismatic Movement", "Wesleyan Methodist Church (Great Britain)", "African Methodist Episcopal Church", "Church of Scotland", "Puritans", "Elim Pentecostal Church", "Bulgarian Exarchate", "Georgian Orthodox Church", "Church of the Brethren", "Christian and Missionary Alliance", "Evangelical Church in the Rhineland", "Free Church of Scotland (1843–1900)", "United Free Church of Scotland", "Ukrainian Orthodox Eparchy of Central Canada", "General Association of General Baptists", "Baptist Union of Scotland", "Canadian Baptists of Ontario and Quebec", "Christian Reformed Church in North America", "Christian and Missionary Alliance", "Uniting Church in Australia", "Primitive Baptists", "Pentecostal Assemblies of Canada", "Fifth Monarchists", "Anglican Church of Canada", "Evangelical Free Church of America", "Iglesia ni Cristo"]
jewish=["Judaism", "Jews", "Sephardi Jews", "Orthodox Judaism"]
buddhist=["Buddhism", "Theravada", "Mahayana", "Buddhism in Sri Lanka"]
hindu=["Hindu", "Hinduism", "Jainism", "Bengali Hindus", "Lingayatism", "Kayastha", "Hindu-Lingayath", "Matua Mahasangha"]
islam=["Islam", "Shia Islam", "Sunni Islam", "Muslim", "Bektashi Order", "Alawites", "Twelver", "Alevism", "Lahore Ahmadiyya Movement for the Propagation of Islam", "Salafi movement"]
atheist=["Agnosticism", "Atheists", "List of Jewish atheists and agnostics"]

# Adding each entry to data -> if/else commands for multiple entries in profession + religion for they show as multiple entries
for dict in allpeople:
    if type(dict["ontology/religion_label"]) is list:
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/religion_label"]:
                if item in christian:
                    rel="Christian"
                elif item in jewish:
                    rel="Jew"
                elif item in buddhist:
                    rel="Buddhist"
                elif item in islam:
                    rel="Muslim"
                elif item in hindu:
                    rel="Hindu"
                elif item in atheist:
                    rel="Atheist/Agnostics"
                for item in dict["ontology/profession_label"]:
                    onto=item
                    entry=[]
                    entry.append(rel)
                    entry.append(onto)
                    data.append(entry)
        else:
            for item in dict["ontology/religion_label"]:
                if item in christian:
                    rel="Christian"
                elif item in jewish:
                    rel="Jew"
                elif item in buddhist:
                    rel="Buddhist"
                elif item in islam:
                    rel="Muslim"
                elif item in hindu:
                    rel="Hindu"
                elif item in atheist:
                    rel="Atheist/Agnostics"
                entry=[]
                entry.append(rel)
                entry.append(dict["ontology/profession_label"])
                data.append(entry)
    else:
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                if dict["ontology/religion_label"] in christian:
                    rel="Christian"
                elif dict["ontology/religion_label"] in jewish:
                    rel="Jew"
                elif dict["ontology/religion_label"] in buddhist:
                    rel="Buddhist"
                elif dict["ontology/religion_label"] in islam:
                    rel="Muslim"
                elif dict["ontology/religion_label"] in hindu:
                    rel="Hindu"
                elif dict["ontology/religion_label"] in atheist:
                    rel="Atheist/Agnostics"
                entry=[]
                entry.append(rel)
                entry.append(item)
                data.append(entry)
        else:
            if dict["ontology/religion_label"] in christian:
                rel="Christian"
            elif dict["ontology/religion_label"] in jewish:
                rel="Jew"
            elif dict["ontology/religion_label"] in buddhist:
                rel="Buddhist"
            elif dict["ontology/religion_label"] in islam:
                rel="Muslim"
            elif dict["ontology/religion_label"] in hindu:
                rel="Hindu"
            elif dict["ontology/religion_label"] in atheist:
                rel="Atheist/Agnostics"
            entry=[]
            entry.append(rel)
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
        

# Making CSV 
print(data)
import csv

with open('profession_by_religion.csv', mode='w',  newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)