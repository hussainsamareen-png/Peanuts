# data/*.json --> ignore file command.

import json

# apeople=[]
# with open("data\A_people.json", encoding='utf-8') as file:
#     Apeople= json.load(file)
#     for dict in Apeople:
#         if "ontology/profession_label" in dict:
#             print(str(dict["ontology/profession_label"]))
#             apeople.append(dict)
# print(apeople)

abc= ['A','B', 'C', 'D', 'E', 'F', 'G', 'H',
       'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         "Q", "R", 'S', 'T', "U", "V", 'W', 'X', "Y", "Z"]

profpeople=[]
for letter in abc:
    with open(f"data/{letter}_people.json", encoding='utf-8') as file:
        people= json.load(file)
        for dict in people:
            if "ontology/profession_label" in dict:
                dict["ontology/profession_label"]
                profpeople.append(dict)
print(profpeople)

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