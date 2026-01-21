import json

# Run for all A-Z
selectpeople=[]
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"data/{letter}_people.json", encoding='utf-8') as file:
        allpeople=json.load(file)
        for person in allpeople:
            if "ontology/profession_label" in person:
                if "ontology/birthPlace_label" in person:
                    selectpeople.append(person)
                elif "ontology/birthDate" in person:
                    selectpeople.append(person)
                elif "ontology/religion_label" in person:
                    selectpeople.append(person)

# Change birthdate YY-MM-DD to MMDD int -> Assign zodiac
for person in selectpeople:
    if "ontology/birthDate" in person:
        birthday=person["ontology/birthDate"]
        if type(birthday) is list:
            birthday.pop(0)
        else:
            birthdaymd=birthday[5:]
            birthdaymd=birthdaymd.replace("-","")
        birthdaymd=int(birthdaymd)
        # print(birthdaymd)
        if birthdaymd<120 or birthdaymd>1220:
            person["zodiac"]="capricorn"
        elif birthdaymd>119 and birthdaymd<219:
            person["zodiac"]="aquarius"
        elif birthdaymd>218 and birthdaymd<321:
            person["zodiac"]="pisces"
        elif birthdaymd>320 and birthdaymd<420:
            person["zodiac"]="aries"
        elif birthdaymd>419 and birthdaymd<521:
            person["zodiac"]="taurus"
        elif birthdaymd>520 and birthdaymd<621:
            person["zodiac"]="gemini"
        elif birthdaymd>620 and birthdaymd<723:
            person["zodiac"]="cancer"
        elif birthdaymd>722 and birthdaymd<823:
            person["zodiac"]="leo"
        elif birthdaymd>822 and birthdaymd<923:
            person["zodiac"]="virgo"
        elif birthdaymd>922 and birthdaymd<1023:
            person["zodiac"]="libra"
        elif birthdaymd>1022 and birthdaymd<1122:
            person["zodiac"]="scorpio"
        elif birthdaymd>1121 and birthdaymd<1221:
            person["zodiac"]="sagittarius"
    else:
        person["zodiac"]="NA"
    # if "ontology/birthPlace_label" in person:
    
# Lists
    # Countries in continents
    allcountries=["China", "Indonesia", "Bangladesh", "Philippines", "Turkey", "Thailand", "South Korea", "Afghanistan", "Uzbekistan", "Yemen", "North Korea", "Kazakhstan", "Cambodia", "Azerbaijan", "Tajikistan", "Laos", "Kyrgyzstan", "Singapore", "State of Palestine", "Georgia", "Armenia", "Bahrain", "Cyprus", "Maldives", "Taiwan", "Macao", "India", "Pakistan", "Japan", "Vietnam", "Iran", "Myanmar", "Iraq", "Saudi Arabia", "Malaysia", "Nepal", "Sri Lanka", "Syria", "Jordan", "United Arab Emirates", "Israel", "Lebanon", "Turkmenistan", "Oman", "Kuwait", "Mongolia", "Qatar", "Timor-Leste", "Bhutan", "Brunei", "Hong Kong",
    "Germany", "France", "Spain", "Poland", "Netherlands", "Czech Republic", "Portugal", "Hungary", "Austria", "Switzerland", "Denmark", "Slovakia", "Ireland", "Moldova", "Albania", "North Macedonia", "Latvia", "Montenegro", "Malta", "Andorra", "Liechtenstein", "Holy See", "Isle of Man", "Gibraltar", "Russia", "United Kingdom", "Italy", "Ukraine", "Romania", "Belgium", "Greece", "Sweden", "Belarus", "Serbia", "Bulgaria", "Finland", "Norway", "Croatia", "Bosnia and Herzegovina", "Lithuania", "Slovenia", "Estonia", "Luxembourg", "Iceland", "Monaco", "San Marino", "Channel Islands", "Faeroe Islands",
    "Antigua and Barbuda", "The Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "French Guiana", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela",
    "Nigeria", "Egypt", "Tanzania", "Kenya", "Algeria", "Morocco", "Mozambique", "Madagascar", "Côte d'Ivoire", "Burkina Faso", "Malawi", "Senegal", "Somalia", "Guinea", "Benin", "Tunisia", "Togo", "Libya", "Liberia", "Mauritania", "Namibia", "Botswana", "Lesotho", "Equatorial Guinea", "Eswatini", "Comoros", "Sao Tome & Principe", "Réunion", "Mayotte", "Ethiopia", "DR Congo", "South Africa", "Uganda", "Sudan", "Angola", "Ghana", "Cameroon", "Niger", "Mali", "Zambia", "Chad", "Zimbabwe", "Rwanda", "Burundi", "South Sudan", "Sierra Leone", "Congo", "Central African Republic", "Eritrea", "Gambia", "Gabon", "Guinea-Bissau", "Mauritius", "Djibouti", "Cabo Verde", "Seychelles", "Western Sahara", "Saint Helena",
    "American Samoa", "Australia", "Cook Islands", "Federated States of Micronesia", "Fiji", "French Polynesia", "Guam", "Hawaii", "Western New Guinea", "Kiribati", "Marshall Islands", "Nauru", "New Caledonia", "New Zealand", "Niue", "Norfolk Island", "Northern Mariana Islands", "Palau", "Papua New Guinea", "Pitcairn Islands", "Samoa", "Solomon Islands", "Timor-Leste", "Tokelau", "Tonga", "Tuvalu", "Vanuatu", "Wallis and Futuna"]
    asia=["China", "Indonesia", "Bangladesh", "Philippines", "Turkey", "Thailand", "South Korea", "Afghanistan", "Uzbekistan", "Yemen", "North Korea", "Kazakhstan", "Cambodia", "Azerbaijan", "Tajikistan", "Laos", "Kyrgyzstan", "Singapore", "State of Palestine", "Georgia", "Armenia", "Bahrain", "Cyprus", "Maldives", "Taiwan", "Macao", "India", "Pakistan", "Japan", "Vietnam", "Iran", "Myanmar", "Iraq", "Saudi Arabia", "Malaysia", "Nepal", "Sri Lanka", "Syria", "Jordan", "United Arab Emirates", "Israel", "Lebanon", "Turkmenistan", "Oman", "Kuwait", "Mongolia", "Qatar", "Timor-Leste", "Bhutan", "Brunei", "Hong Kong"]
    europe=["Germany", "France", "Spain", "Poland", "Netherlands", "Czech Republic", "Portugal", "Hungary", "Austria", "Switzerland", "Denmark", "Slovakia", "Ireland", "Moldova", "Albania", "North Macedonia", "Latvia", "Montenegro", "Malta", "Andorra", "Liechtenstein", "Holy See", "Isle of Man", "Gibraltar", "Russia", "United Kingdom", "Italy", "Ukraine", "Romania", "Belgium", "Greece", "Sweden", "Belarus", "Serbia", "Bulgaria", "Finland", "Norway", "Croatia", "Bosnia and Herzegovina", "Lithuania", "Slovenia", "Estonia", "Luxembourg", "Iceland", "Monaco", "San Marino", "Channel Islands", "Faeroe Islands"]
    na=["Antigua and Barbuda", "The Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    sa=["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "French Guiana", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
    africa=["Nigeria", "Egypt", "Tanzania", "Kenya", "Algeria", "Morocco", "Mozambique", "Madagascar", "Côte d'Ivoire", "Burkina Faso", "Malawi", "Senegal", "Somalia", "Guinea", "Benin", "Tunisia", "Togo", "Libya", "Liberia", "Mauritania", "Namibia", "Botswana", "Lesotho", "Equatorial Guinea", "Eswatini", "Comoros", "Sao Tome & Principe", "Réunion", "Mayotte", "Ethiopia", "DR Congo", "South Africa", "Uganda", "Sudan", "Angola", "Ghana", "Cameroon", "Niger", "Mali", "Zambia", "Chad", "Zimbabwe", "Rwanda", "Burundi", "South Sudan", "Sierra Leone", "Congo", "Central African Republic", "Eritrea", "Gambia", "Gabon", "Guinea-Bissau", "Mauritius", "Djibouti", "Cabo Verde", "Seychelles", "Western Sahara", "Saint Helena"]
    oceania=["American Samoa", "Australia", "Cook Islands", "Federated States of Micronesia", "Fiji", "French Polynesia", "Guam", "Hawaii", "Western New Guinea", "Kiribati", "Marshall Islands", "Nauru", "New Caledonia", "New Zealand", "Niue", "Norfolk Island", "Northern Mariana Islands", "Palau", "Papua New Guinea", "Pitcairn Islands", "Samoa", "Solomon Islands", "Timor-Leste", "Tokelau", "Tonga", "Tuvalu", "Vanuatu", "Wallis and Futuna"]

    # Religion list
    christian=["Christianity", "Catholic Church", "Espiscopal", "Eastern Orthodox Church", "Protestant", "Methodism", "Quaker", "Lutheranism", "Espiscopal", "Presbyterianism", "Russian Orthodox Church", "Presbyterian Church", "Church of England", "Baptists", "Christian", "Catholicism", "Roman Catholic Church", "Anglicanism", "Congregational Church", "Church of God Ministry of Jesus Christ International", "Serbian Orthodox Church", "Greek", "Baptists", "United Methodist Church", "Protestantism", "Universalist Church of America", "Romanian Orthodox Church", "Armenian Apostolic Church", "Dutch Reformed Church", "Methodist Episcopal Church", "Assemblies of God", "The Church of Jesus Christ of Latter-day Saints", "Born again (Christianity)", "Orthodox Autocephalous Church of Albania", "Catholic Church in the Philippines", "Independent Church", "United Church of Canada", "Evangelicalism", "Church of Sweden", "Traditionalist Catholic", "Nondenominational Christianity", "Southern Baptist Convention", "Mormons", "Church of the United Brethren in Christ", "Episcopal Church (United States)", "Anglican Church of Australia", "Church of Greece", "African Methodist Episcopal Zion Church", "Christian Church (Disciples of Christ)", "Evangelical Lutheran Church of Finland", "Church of the Nazarene", "Church of God Ministry of Jesus Christ International", "Maronite Church", "Presbyterian Church in Ireland", "Evangelical Church in Germany", "Southern Baptist Convention", "Free Presbyterian Church of Ulster", "Remonstrants", "Churches of Christ", "New Hope Christian Fellowship", "Church of Norway", "Pentecostalism", "Cumberland Presbyterian Church", "Presbyterian Church (USA)", "Mennonite", "Calvinism", "Seventh-day Adventist Church", "Reformed Churches in South Africa", "Orthodox Autocephalous Church of Albania", "Coptic Orthodox Church of Alexandria", "Charismatic Movement", "Wesleyan Methodist Church (Great Britain)", "African Methodist Episcopal Church", "Church of Scotland", "Puritans", "Elim Pentecostal Church", "Bulgarian Exarchate", "Georgian Orthodox Church", "Church of the Brethren", "Christian and Missionary Alliance", "Evangelical Church in the Rhineland", "Free Church of Scotland (1843–1900)", "United Free Church of Scotland", "Ukrainian Orthodox Eparchy of Central Canada", "General Association of General Baptists", "Baptist Union of Scotland", "Canadian Baptists of Ontario and Quebec", "Christian Reformed Church in North America", "Christian and Missionary Alliance", "Uniting Church in Australia", "Primitive Baptists", "Pentecostal Assemblies of Canada", "Fifth Monarchists", "Anglican Church of Canada", "Evangelical Free Church of America", "Iglesia ni Cristo"]
    jewish=["Judaism", "Jews", "Sephardi Jews", "Orthodox Judaism"]
    buddhist=["Buddhism", "Theravada", "Mahayana", "Buddhism in Sri Lanka"]
    hindu=["Hindu", "Hinduism", "Jainism", "Bengali Hindus", "Lingayatism", "Kayastha", "Hindu-Lingayath", "Matua Mahasangha"]
    islam=["Islam", "Shia Islam", "Sunni Islam", "Muslim", "Bektashi Order", "Alawites", "Twelver", "Alevism", "Lahore Ahmadiyya Movement for the Propagation of Islam", "Salafi movement"]
    atheist=["Agnosticism", "Atheists", "List of Jewish atheists and agnostics"]

# Assigning birth place into continent
for person in selectpeople:
    if "ontology/birthPlace_label" in person:
        place=person["ontology/birthPlace_label"]
        if type(person["ontology/birthPlace_label"]) is list:
            for item in place:
                if item in allcountries:
                    country=item
                    if country in asia:
                        person["birthcont"]="Asia"
                    elif country in europe:
                        person["birthcont"]="Europe"
                    elif country in na:
                        person["birthcont"]="North America"
                    elif country in sa:
                        person["birthcont"]="South America"
                    elif country in oceania:
                        person["birthcont"]="Oceania"
                    elif country in africa:
                        person["birthcont"]="Africa"
        else:
            country=person["ontology/birthPlace_label"]
            if country in asia:
                person["birthcont"]="Asia"
            elif country in europe:
                person["birthcont"]="Europe"
            elif country in na:
                person["birthcont"]="North America"
            elif country in sa:
                person["birthcont"]="South America"
            elif country in oceania:
                person["birthcont"]="Oceania"
            elif country in africa:
                person["birthcont"]="Africa"
            else:
                person["birthcont"]="NA"
    else:
        person["birthcont"]="NA"


# Add all into one data
data=[
    ["Zodiac", "Continent", "Religion", "Profession"],
]

# Add birthcont and zodiac for people who may have had multiple and run through every item and found nothing.
for person in selectpeople:
    if "birthcont" not in person:
        person["birthcont"]="NA"
    if "zodiac" not in person:
        person["zodiac"]="NA"


# Compile all into 1 csv
for person in selectpeople:
    if "ontology/religion_label" in person:
        # Multiple religions
        if type(person["ontology/religion_label"]) is list:
            for item in person["ontology/religion_label"]:
                if item in christian:
                    person["religion"]="Christian"
                elif item in jewish:
                    person["religion"]="Jew"
                elif item in buddhist:
                    person["religion"]="Buddhist"
                elif item in islam:
                    person["religion"]="Muslim"
                elif item in hindu:
                    person["religion"]="Hindu"
                elif item in atheist:
                    person["religion"]="Atheist/Agnostics"
                else:
                    person["religion"]="NA"
                if type(person["ontology/profession_label"]) is list:
                    for item in person["ontology/profession_label"]:
                        onto=item
                        entry=[]
                        entry.append(person["zodiac"])
                        entry.append(person["birthcont"])
                        entry.append(person["religion"])
                        entry.append(onto)
                        data.append(entry)
                else:
                    entry=[]
                    entry.append(person["zodiac"])
                    entry.append(person["birthcont"])
                    entry.append(person["religion"])
                    entry.append(person["ontology/profession_label"])
                    data.append(entry)
        # One religion
        else:
            if person["ontology/religion_label"] in christian:
                person["religion"]="Christian"
            elif person["ontology/religion_label"] in jewish:
                person["religion"]="Jew"
            elif person["ontology/religion_label"] in buddhist:
                person["religion"]="Buddhist"
            elif person["ontology/religion_label"] in islam:
                person["religion"]="Muslim"
            elif person["ontology/religion_label"] in hindu:
                person["religion"]="Hindu"
            elif person["ontology/religion_label"] in atheist:
                person["religion"]="Atheist/Agnostics"
            else:
                person["religion"]="NA"
            if type(person["ontology/profession_label"]) is list:
                for item in person["ontology/profession_label"]:
                    onto=item
                    entry=[]
                    entry.append(person["zodiac"])
                    entry.append(person["birthcont"])
                    entry.append(person["religion"])
                    entry.append(onto)
                    data.append(entry)
            else:
                entry=[]
                entry.append(person["zodiac"])
                entry.append(person["birthcont"])
                entry.append(person["religion"])
                entry.append(person["ontology/profession_label"])
                data.append(entry)
    # No religion
    else:
        person["religion"]="NA"
        if "ontology/profession_label" in person:
            if type(person["ontology/profession_label"]) is list:
                for item in person["ontology/profession_label"]:
                    onto=item
                    entry=[]
                    entry.append(person["zodiac"])
                    entry.append(person["birthcont"])
                    entry.append(person["religion"])
                    entry.append(onto)
                    data.append(entry)
            else:
                entry=[]
                entry.append(person["zodiac"])
                entry.append(person["birthcont"])
                entry.append(person["religion"])
                entry.append(person["ontology/profession_label"])
                data.append(entry)
                
import csv

# Make CSV file
with open('profession_by_all.csv', mode='w',  newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)
