#Level 1

empty_tuple = tuple()
sis = ("Amalia", "Mary", "Olga")
bros =("Alex", "Valeriy")
siblings = sis + bros
how_many = len(siblings)
print(how_many)
family_members = siblings + ("Inna", "Sergey")
print(family_members)

#Level 2 task 1
*siblings, mother, father = family_members

print("Siblings:", siblings)
print("Mother:", mother)
print("Father:", father)

#Level 2 task 2
fruits = ("apple", "Pear")
vegetables = ("tomato", "potato")
animal_products = ("milk", "eggs")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
lst = list(food_stuff_tp)
lengh = len(lst)
mid_item_index = lengh // 2
mid_item = lst[mid_item_index]
print(mid_item)
print(lst[:3])
print(lst[3:])
del lst
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)