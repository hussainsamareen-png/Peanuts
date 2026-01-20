# data/*.json --> ignore file command.

import json

abc= ['A','B', 'C', 'D', 'E', 'F', 'G', 'H',
       'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         "Q", "R", 'S', 'T', "U", "V", 'W', 'X', "Y", "Z"]

allpeople=[]
for letter in abc:
    with open(f"data/{letter}_people.json", encoding='utf-8') as file:
        people= json.load(file)
        for dict in people:
            if "ontology/profession_label" in dict:
                # print(str(dict["ontology/profession_label"]))
                if "ontology/birthDate" in dict:
                    allpeople.append(dict)

for dict in allpeople:
    birthday=dict["ontology/birthDate"]
    if type(birthday) is list:
        birthday.pop(0)
    else:
        birthdaymd=birthday[5:]
        birthdaymd=birthdaymd.replace("-","")
    birthdaymd=int(birthdaymd)
    # print(birthdaymd)
    if birthdaymd<120 or birthdaymd>1220:
        dict["zodiac"]="capricorn"
    elif birthdaymd>119 and birthdaymd<219:
        dict["zodiac"]="aquarius"
    elif birthdaymd>218 and birthdaymd<321:
        dict["zodiac"]="pisces"
    elif birthdaymd>320 and birthdaymd<420:
        dict["zodiac"]="aries"
    elif birthdaymd>419 and birthdaymd<521:
        dict["zodiac"]="taurus"
    elif birthdaymd>520 and birthdaymd<621:
        dict["zodiac"]="gemini"
    elif birthdaymd>620 and birthdaymd<723:
        dict["zodiac"]="cancer"
    elif birthdaymd>722 and birthdaymd<823:
        dict["zodiac"]="leo"
    elif birthdaymd>822 and birthdaymd<923:
        dict["zodiac"]="virgo"
    elif birthdaymd>922 and birthdaymd<1023:
        dict["zodiac"]="libra"
    elif birthdaymd>1022 and birthdaymd<1122:
        dict["zodiac"]="scorpio"
    elif birthdaymd>1121 and birthdaymd<1221:
        dict["zodiac"]="sagittarius"
    # print(apeople)

capricornppl=[]
aquariusppl=[]
piscesppl=[]
ariesppl=[]
taurusppl=[]
geminippl=[]
cancerppl=[]
leoppl=[]
virgoppl=[]
librappl=[]
scorpioppl=[]
sagittariusppl=[]
for dict in allpeople:
    if dict["zodiac"]=="aquarius":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                aquariusppl.append(item)
        else:
            aquariusppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="capricorn":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                capricornppl.append(item)
        else:
            capricornppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="pisces":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                piscesppl.append(item)
        else:
            piscesppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="aries":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                ariesppl.append(item)
        else:
            ariesppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="taurus":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                taurusppl.append(item)
        else:
            taurusppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="gemini":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                geminippl.append(item)
        else:
            geminippl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="cancer":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                cancerppl.append(item)
        else:
            cancerppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="leo":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                leoppl.append(item)
        else:
            leoppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="virgo":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                virgoppl.append(item)
        else:
            virgoppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="libra":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                librappl.append(item)
        else:
            librappl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="scorpio":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                scorpioppl.append(item)
        else:
            scorpioppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="sagittarius":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                sagittariusppl.append(item)
        else:
            sagittariusppl.append(dict["ontology/profession_label"])
# print(aquariusppl)
# print(taurusppl)

import csv

data = [
["Zodiac", "Professions"],
["Capricorn:", capricornppl],
["Aquarius:", aquariusppl],
["Pisces:", piscesppl],
["Aries:", ariesppl],
["Taurus:", taurusppl],
["Gemini:", geminippl],
["Cancer:", cancerppl],
["Leo:", leoppl],
["Virgo:", virgoppl],
["Libra:", librappl],
["Scorpio:", scorpioppl],
["Sagittarius:", sagittariusppl],
]

with open('profession_by_zodiac.csv', mode='w',  newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)


# Assign each person a zodiac sign, adding a new key:value pair
# zodiac:xxx
# Capricorn: December 21 - January 19
# Aquarius: January 20 - February 18
# Pisces: February 19 - March 20
# Aries: March 21 - April 19
# Taurus: April 20 - May 20
# Gemini: May 21 - June 20
# Cancer: June 21 - July 22
# Leo: July 23 - August 22
# Virgo: August 23 - September 22
# Libra: September 23 - October 22
# Scorpio: October 23 - November 21
# Sagittarius: November 22 - December 20


# abc= ['A','B', 'C', 'D', 'E', 'F', 'G', 'H',
#        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#          "Q", "R", 'S', 'T', "U", "V", 'W', 'X', "Y", "Z"]

# profpeople=[]
# for letter in abc:
#     with open(f"data/{letter}_people.json", encoding='utf-8') as file:
#         people= json.load(file)
#         for dict in people:
#             if "ontology/profession_label" in dict:
#                 dict["ontology/profession_label"]
#                 profpeople.append(dict)
# # print(profpeople)

# profpeoplefilter={}
# for dict in profpeople:
#     birthday=dict["ontology/birthDate"]
#     birthday=birthday.strip("-")
#     print(birthday)
#     # birthdaymd=birthday[4:]
#     # print(birthday)

    # profpeoplefilter["zodiac"]




# INFO WE NEED 
# BIRTH PLACE, BIRTH DATE, PROFESSION, RELIGION