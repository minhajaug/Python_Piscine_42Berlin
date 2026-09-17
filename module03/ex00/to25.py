#!/usr/bin/env python3

x = int(input("Enter a number less than 25\n"))

if x > 25:
    print("Error")
else: 
    while x <= 25:
        print(f"Inside the loop my variable is {x}")
        x=x+1
 
