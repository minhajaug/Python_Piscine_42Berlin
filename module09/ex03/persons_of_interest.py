#!/usr/bin/env python3

def famous_births(people):
   result = dict(sorted(people.items(), key=lambda item: item[1]["date_of_birth"]))        
   for person, data in result.items():
       d = data["date_of_birth"]
       n = data["name"]
       print(f"{n} is a great scientist born in {d}.")
   return  

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
