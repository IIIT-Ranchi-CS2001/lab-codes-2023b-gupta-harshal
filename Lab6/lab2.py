name = {"Tom", "Jerry", "Pikachu", "Spidey", "Doremon", "ChotaBheem", "Nagraaj", "Balveer", "Motu", "Patlu"}
plan = {"Spidey", "Motu", "Patlu"}
mil = {"Nagraj", "Pikachu", "Spidey"}
cla = {"Doremon", "Balveer"}

print("Attended both: ", plan & mil)
print("Attended only one: ", plan ^ mil)
print("Bunked Class: ", name - plan - mil - cla)