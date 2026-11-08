#Level 1 ex 1

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number, end=" ")
print()

i = 0
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1

# Level 1 ex 2
print()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in range(10, -1, -1):
    print(number, end=" ")
print()

i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1

#Level 1 ex 3
for i in range(0, 8):
    print("#" * i)

#Level 1 ex 4
for i in range(8):
    for j in range(8): 
        print("# ", end="")
    print()

#Level 1 ex 5
x = range(11)
y = range(11)

for a, b in zip(x, y):
    result = a * b
    print(f"{a} * {b} = {result}")

#Level 1 ex 6
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)

#Level 1 ex 7

for i in range(101):
    if i % 2 == 0:
        print(i)

#Level 1 ex 8

for i in range(101):
    if i % 2 != 0:
        print(i)

#Level 2 ex 1
total = 0

for number in range(101):
    total += number

print(f"The sum of all numbers is {total}")

#Level 2 ex 2
all_evens = 0
all_odds = 0

for number in range(101):
    if number % 2 == 0:
        all_evens += number
    else:
        all_odds += number

print(f"The sum of all evens is {all_evens}. And the sum of all odds is {all_odds}.")    

#Level 3 ex 1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
for country in countries:
    if "land" in country:
       print(country)

#Level 3 ex 2

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print(reversed_fruits)

#Level 3 ex 3

from countries_data import countries_data 
all_languages = set()
language_count = {}
for country in countries_data:
    for language in country['languages']:
        all_languages.add(language)

print("Total languages: ", len(all_languages))

for country in countries_data:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

def get_count(pair):
    return pair[1]

sorted_languages = sorted(language_count.items(), key=get_count, reverse=True)

for language, count in sorted_languages[:10]:
    print(language, count)

def get_population(country):
    return country['population']

sorted_countries = sorted(countries_data, key=get_population, reverse=True)

for country in sorted_countries[:10]:
    print(country['name'], country['population'])

