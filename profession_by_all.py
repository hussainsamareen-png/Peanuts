import json

allpeople=[]
with open(f"data/A_people.json", encoding='utf-8') as file:
        people=json.load(file)
        for dict in people:
            if "ontology/profession_label" in dict:
                if "ontology/birthPlace_label" in dict:
                    allpeople.append(dict)
                elif "ontology/birthDate" in dict:
                    allpeople.append(dict)
                elif "ontology/religion_label" in dict:
                    allpeople.append(dict)

# Change birthdate YY-MM-DD to MMDD int -> Assign zodiac
for dict in allpeople:
    if "ontology/birthDate" in dict:
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
    else:
        dict["zodiac"]=""
    # if "ontology/birthPlace_label" in dict:
        

print(allpeople)