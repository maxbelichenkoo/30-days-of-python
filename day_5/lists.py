#task 1-4
lst = []
ai_engineer = ["API", "Python", "LLM", "Transformers", "SQL"]
length = len(ai_engineer)
print(ai_engineer[0], ai_engineer[2], ai_engineer[4])

#task 5
mixed_data_types = ["Max", 18, 177, "single", "Odesa"]

#task 6-25
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2
last_index = len(it_companies) - 1
middle_element = it_companies[middle_index]
last_element = it_companies[last_index]
print(it_companies)
print(len(it_companies))
print(it_companies[0], middle_element, last_element)
it_companies[0] = "NVIDIA"
print(it_companies)
it_companies.append("Netflix")
print(it_companies)
middle_index2 = len(it_companies) // 2
it_companies.insert(middle_index2, "Adobe")
print(it_companies)
it_companies[2] = it_companies[2].upper()
print(it_companies)
hash = '#;  '.join(it_companies)
print(hash)
does_exist = "Android" in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
first3 = it_companies[0:3]
last3 = it_companies[-3:]
print(first3)
print(last3)
middle_element = len(it_companies) // 2
removed_company = it_companies.pop(middle_element)
print(it_companies)
del it_companies[0]
print(it_companies)
middle_element = len(it_companies) // 2
del it_companies[middle_element]
print(it_companies)
last_element = len(it_companies) - 1
del it_companies[last_element]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

#task 26-27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
summ = front_end + back_end
print(summ)
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(4, "Python")
full_stack.insert(5, "SQL")
print(full_stack)

#Level 2 task 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
first_age = ages[0]
print(first_age)
last_age = ages[-1]
print(last_age)
last_age_index = len(ages)
ages.insert(1, first_age)
ages.insert(last_age_index, last_age)
print(ages)
mid = last_age_index // 2

if last_age_index % 2 != 0:
 median = ages[mid]
else:
 median = (ages[mid - 1] + ages[mid]) / 2
print(int(median))
average_age = sum(ages) / len(ages)
print(int(average_age))
range = last_age - first_age
print(int(range))
min_diff = abs(first_age - average_age)
max_diff = abs(last_age - average_age)
if min_diff > max_diff:
    print(f"{min_diff} is greater than {max_diff}")
elif min_diff < max_diff:
    print(f"{max_diff} is greater than {min_diff}")
else:
    print("Both absolute differences are equal")

#Level 2 task 1-3

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

first = countries[0]
last = countries[-1]
middle_index = len(countries) // 2
middle_country = countries[middle_index]
print(middle_country)
n = len(countries)
mid = (n + 1) // 2

first_half = countries[:mid]
print(f"{len(first_half)}: {first_half}")

all_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = all_countries

print("first country:", country1)
print("second country:", country2)
print("third country:", country3)
print("Scandic countries:", scandic_countries)