password = "Python is awesome"

user_input = input("Enter the password : ").strip()

if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")