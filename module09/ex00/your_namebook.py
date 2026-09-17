#!/usr/bin/env python3

def array_of_names(p): 

    pairs = []
    for key, value in persons.items():
        pairs.append(f"{key.capitalize()} {value.capitalize()}")
    return pairs

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
