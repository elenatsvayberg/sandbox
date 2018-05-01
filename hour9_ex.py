from typing import Dict

states= {"VA":"Richmond", "NY":"NY", "NJ":"Trenton"}
print(states)
#states ={"FL":"Orlando"}
#print(states)
print(type(states))
states["NJ"]="Trenton1"
print(states)
states.pop("NJ")
print(states)
states["NJ"]="Trenton"
print(states)

birth_years = {"Alex": "1973", "Josh":"1973"}
birth_years["Elena"] = "1975"
print(birth_years["Elena"])
print("Alex" in birth_years)
print(birth_years.keys())
print(birth_years.values())
print(birth_years.pop("Alex"))
print(birth_years)
print()

d1 = {"1":"one", "2":"two","3":"three"}
d2 = {"1":"one", "2":"two","3":"three"}
d3 = {"1":"one", "3":"three","2":"Two"}
print(d1==d2)
print(d1==d3)
