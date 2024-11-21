#!/usr/bin/env python3
while True:
 
    user_input = input("What you gotta say: ").strip()
    if user_input.lower() == "stop":
        break
    print("I got that! Anything else?")