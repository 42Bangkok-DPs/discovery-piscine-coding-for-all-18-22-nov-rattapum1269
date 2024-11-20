First_number = int(input("Enter the first number :").strip())
second_number = int(input("Enter the second number :").strip())

result = First_number * second_number

print(f"{First_number} x {second_number} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")