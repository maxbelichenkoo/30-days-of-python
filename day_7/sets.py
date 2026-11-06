# Level 1 1-5
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length_it = len(it_companies)
it_companies.add("Twitter")
it_companies.update(["Alphabet", "NVIDIA"])
it_companies.remove("IBM")
it_companies.discard("Salesforce")
print(it_companies)

# Level 2 1-7
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union = A.union(B)
print(union)
intersection = A.intersection(B)
print(intersection)
issubset = A.issubset(B)
print(issubset)
isdisjoint = A.isdisjoint(B)
print(isdisjoint)
symmetric = A.symmetric_difference(B)
print(symmetric)
del A, B

#Level 3 1st
age = [22, 19, 24, 25, 26, 24, 25, 24]
length_list = len(age)
age = set(age)
length_set = len(age)
if length_list > length_set:
    print("The list is bigger than the set.")
elif length_set > length_list:
    print("The set is bigger than the list.")
else:
    print("The list and set have the same length.")

# Level 3 3rd

sentence = "I am a teacher and I love to inspire and teach people."
words_list = sentence.lower().replace(".", "").split()
unique_words = set(words_list)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))