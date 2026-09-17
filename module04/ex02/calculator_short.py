#!/usr/bin/env python3

#I wanna make use of idea that operator (stuff like +, -, /, * etc) can be expressed as a function
#Functions can be assigned to variables, so stuff like: 
#   [def func(a,b): something] and then [x = f] is totally allowed 
# (NOT x = f() - thats a different thing)
#operator module has all of these operations as functions, so I import it

import operator

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")

ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}

for symbol, op in ops.items():
    print(f"{first} {symbol} {second} = {op(first, second)}")

