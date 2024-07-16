#%%
first_name = "Daniel"
last_name = "Kadyrov"

height_feet = 5
height_inches = 11

total_height_in_inches = height_feet * 12 + height_inches

list_of_interests = ["Surfing", "Biking", "Surfing", "Eating"]

profile = {
    "First": first_name, 
    "Last": last_name, 
    "Height (feet)": total_height_in_inches // 12,
    "Height (inches)": total_height_in_inches % 12,
    "Interests": list_of_interests, 
    "Number of Interests": len(list_of_interests)
}

#%%
paragraph = f"{profile["First"]} {profile["Last"]} is {profile["Height (feet)"]}\' {profile["Height (inches)"]}\" tall. They have {profile["Number of Interests"]} interests."
print(paragraph)
# %%
