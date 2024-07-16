#%%
my_list = [2,4,6,8]

for number in my_list: 
    print(number)
#%%
my_family = ["dad", "mom", "sister", "brother"]

for person in my_family:
    print(person)

#%%
summation = 0 
multiplier = 1
divider = 1

for n in range(1, 101): 
    # summation = summation + n
    summation += n
    multiplier *= n
    divider /= n

# %%
my_dictionary = {
    "First name": "Daniel",
    "Last name": "Kadyrov",
    "Pronoun": "His",
    "Age": 31
}

for key in my_dictionary.keys(): 
    # print(key)
    # print(my_dictionary[key])
    value = my_dictionary[key]

    print(f"{key.capitalize()} is {value}")


# %%
my_string = "The fox jumped over the lazy dog" 

for s in my_string.replace(" ", ""):
    print(s)


# %%
i = 10 

while i >= 5: 
    print(i)
    i -= 1 
# %%
i = 0 
person = my_family[i]

while person != "sister":
    print(person)
    person = my_family[i]
    i += 1 
# %%
s = None 

i = 0 
while s != "l":
    s = my_string[i]
    print(s)
    i+=1 
# %%
i = [0, 1, 2, 3, 4, 5]
j = [6, 7, 8, 9, 10] 

ii = range(0, 6, 1)
jj = range(6, 11, 1)
# %%
for num_i in i: 
    for num_j in j:
        print(f"i: {num_i}, j: {num_j}")
# %%
super_list = i + j 

for num in super_list: 
    if num < 5: 
        print(f"num is less than 5")
    elif num > 5: 
        print(f"num greater than 5")
    else: 
        print(f"num is 5")

# %%
for num in super_list: 
    if num%2 > 0: 
        print(f"{num} is odd")
    else: 
        if num == 0: 
            print(f"{num} is neither")
        else: 
            print(f"{num} is even")
#%%
vowels = "aeiou"
vowels = list(vowels)

vowel_count = {}

for s in my_string:
    if s in vowels: 
        if s in vowel_count.keys(): 
            vowel_count[s] += 1 
        else: 
            vowel_count[s] = 1


# %%
