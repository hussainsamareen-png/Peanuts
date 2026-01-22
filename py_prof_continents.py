"ontology/birthPlace_label"
import json

# Filtering for entries with profession and birthplace as labels
allpeople=[]
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"data/{letter}_people.json", encoding='utf-8') as file:
        people=json.load(file)
        for dict in people:
            if "ontology/profession_label" in dict:
                if "ontology/birthPlace_label" in dict:
                    allpeople.append(dict)

# Creating exhaustive list of all countries in continent + worldwide (for people with birthplace as list ries where they might be city,country ot country, city, etc.)
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

# Adding to overall data but each entry as as [continent, profession]. 
    # Similar to prof-by-zodiac, if/else commands are added for when birthplace and profession are lists 
contdata=[]

for dict in allpeople:
    place=dict["ontology/birthPlace_label"]
    if type(dict["ontology/profession_label"]) is list:
        if type(place) is list:
            for item in place:
                if item in allcountries:
                    country=item
                for item in dict["ontology/profession_label"]:
                    prof=item
                    if country in asia:
                        entry=[]
                        entry.append("Asia")
                        entry.append(prof)
                        contdata.append(entry)
                    elif country in europe:
                        entry=[]
                        entry.append("Europe")
                        entry.append(prof)
                        contdata.append(entry)
                    elif country in na:
                        entry=[]
                        entry.append("North America")
                        entry.append(prof)
                        contdata.append(entry)
                    elif country in sa:
                        entry=[]
                        entry.append("South America")
                        entry.append(prof)
                        contdata.append(entry)
                    elif country in oceania:
                        entry=[]
                        entry.append("Oceania")
                        entry.append(prof)
                        contdata.append(entry)
                    elif country in africa:
                        entry=[]
                        entry.append("Africa")
                        entry.append(prof)
                        contdata.append(entry)
        else:
            for item in dict["ontology/profession_label"]:
                    if place in asia:
                        entry=[]
                        entry.append("Asia")
                        entry.append(item)
                        contdata.append(entry)
                    elif place in europe:
                        entry=[]
                        entry.append("Europe")
                        entry.append(item)
                        contdata.append(entry)
                    elif place in na:
                        entry=[]
                        entry.append("North America")
                        entry.append(item)
                        contdata.append(entry)
                    elif place in sa:
                        entry=[]
                        entry.append("South America")
                        entry.append(item)
                        contdata.append(entry)
                    elif place in oceania:
                        entry=[]
                        entry.append("Oceania")
                        entry.append(item)
                        contdata.append(entry)
                    elif place in africa:
                        entry=[]
                        entry.append("Africa")
                        entry.append(item)
                        contdata.append(entry)
    else:
        if type(place) is list:
            for item in place:
                if item in asia:
                    entry=[]
                    entry.append("Asia")
                    entry.append(dict["ontology/profession_label"])
                    contdata.append(entry)
                elif item in europe:
                    entry=[]
                    entry.append("Europe")
                    entry.append(dict["ontology/profession_label"])
                    contdata.append(entry)
                elif item in na:
                    entry=[]
                    entry.append("North America")
                    entry.append(dict["ontology/profession_label"])
                    contdata.append(entry)
                elif item in sa:
                    entry=[]
                    entry.append("South America")
                    entry.append(dict["ontology/profession_label"])
                    contdata.append(entry)
                elif item in oceania:
                    entry=[]
                    entry.append("Oceania")
                    entry.append(dict["ontology/profession_label"])
                    contdata.append(entry)
                elif item in africa:
                    entry=[]
                    entry.append("Africa")
                    entry.append(dict["ontology/profession_label"])
                    contdata.append(entry)
        else:
            if place in asia:
                    entry=[]
                    entry.append("Asia")
                    entry.append(dict["ontology/profession_label"])
                    contdata.append(entry)
            elif place in europe:
                entry=[]
                entry.append("Europe")
                entry.append(dict["ontology/profession_label"])
                contdata.append(entry)
            elif place in na:
                entry=[]
                entry.append("North America")
                entry.append(dict["ontology/profession_label"])
                contdata.append(entry)
            elif place in sa:
                entry=[]
                entry.append("South America")
                entry.append(dict["ontology/profession_label"])
                contdata.append(entry)
            elif place in oceania:
                entry=[]
                entry.append("Oceania")
                entry.append(dict["ontology/profession_label"])
                contdata.append(entry)
            elif place in africa:
                entry=[]
                entry.append("Africa")
                entry.append(dict["ontology/profession_label"])
                contdata.append(entry)


# Making CSV
print(contdata)
import csv

with open('profession_by_continent.csv', mode='w',  newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(contdata)

# print(sample2)