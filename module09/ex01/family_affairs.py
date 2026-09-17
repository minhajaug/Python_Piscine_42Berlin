#!/usr/bin/env python3
def find_the_redheads(family):   
    #return [k for k, v in family.items() if v == "red"]

    def rule(k):
        return family[k] == "red"

    return list(filter(rule, family))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
