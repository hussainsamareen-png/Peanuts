# data/*.json --> ignore file command.

import json

apeople=[]
with open("data/A_people.json", encoding='utf-8') as file:
    Apeople= json.load(file)
    for dict in Apeople:
        if "ontology/profession_label" in dict:
            # print(str(dict["ontology/profession_label"]))
            if "ontology/birthDate" in dict:
                apeople.append(dict)

for dict in apeople:
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

Apeople={}
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
for dict in apeople:
    if dict["zodiac"]=="aquarius":
        aquariusppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="capricorn":
        capricornppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="pisces":
        piscesppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="aries":
        ariesppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="taurus":
        taurusppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="gemini":
        geminippl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="cancer":
        cancerppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="leo":
        leoppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="virgo":
        virgoppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="libra":
        librappl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="scorpio":
        scorpioppl.append(dict["ontology/profession_label"])
    elif dict["zodiac"]=="saggitarius":
        sagittariusppl.append(dict["ontology/profession_label"])
print(aquariusppl)
print(taurusppl)




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