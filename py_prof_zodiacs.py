# data/*.json --> ignore file command.

import json

# Filtering for entries with profession and birthdate as labels
allpeople=[]
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"data/{letter}_people.json", encoding='utf-8') as file:
        people= json.load(file)
        for dict in people:
            if "ontology/profession_label" in dict:
                # print(str(dict["ontology/profession_label"]))
                if "ontology/birthDate" in dict:
                    allpeople.append(dict)

# Changing birthdates into MMDD (integer) format => Assigning zodiac signs to all filtered entries 
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
        dict["zodiac"]="Capricorn"
    elif birthdaymd>119 and birthdaymd<219:
        dict["zodiac"]="Aquarius"
    elif birthdaymd>218 and birthdaymd<321:
        dict["zodiac"]="Pisces"
    elif birthdaymd>320 and birthdaymd<420:
        dict["zodiac"]="Aries"
    elif birthdaymd>419 and birthdaymd<521:
        dict["zodiac"]="Taurus"
    elif birthdaymd>520 and birthdaymd<621:
        dict["zodiac"]="Gemini"
    elif birthdaymd>620 and birthdaymd<723:
        dict["zodiac"]="Cancer"
    elif birthdaymd>722 and birthdaymd<823:
        dict["zodiac"]="Leo"
    elif birthdaymd>822 and birthdaymd<923:
        dict["zodiac"]="Virgo"
    elif birthdaymd>922 and birthdaymd<1023:
        dict["zodiac"]="Libra"
    elif birthdaymd>1022 and birthdaymd<1122:
        dict["zodiac"]="Scorpio"
    elif birthdaymd>1121 and birthdaymd<1221:
        dict["zodiac"]="Sagittarius"
    # print(apeople)

# New data with header
data = [
["Zodiac", "Profession"],

]

# Adding each entry as [zodiac, profession] 
    # If/else added for if profession is a list 
for dict in allpeople:
    if dict["zodiac"]=="Aquarius":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Capricorn":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Pisces":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Aries":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Taurus":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Gemini":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Cancer":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Leo":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Virgo":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Libra":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Scorpio":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
    elif dict["zodiac"]=="Sagittarius":
        if type(dict["ontology/profession_label"]) is list:
            for item in dict["ontology/profession_label"]:
                entry=[]
                entry.append(dict["zodiac"])
                entry.append(item)
                data.append(entry)
        else:
            entry=[]
            entry.append(dict["zodiac"])
            entry.append(dict["ontology/profession_label"])
            data.append(entry)
# print(aquariusppl)
# print(taurusppl)


print(data)
import csv

# Make and save .csv file with one profession per row
with open('profession_by_zodiac.csv', mode='w',  newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

#print(writer)

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





# INFO WE NEED 
# BIRTH PLACE, BIRTH DATE, PROFESSION, RELIGION
