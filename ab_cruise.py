print("Hello, Welcome to Air Breeze Cruise Lines.")
print("Please enter the correct information when prompted.")

passanger = input("What is your first and last name? ")

print(f'Welcome {passanger}')

age = int(input("How old are you? "))
if age >= 21:
    print('You are old enough, please enter.')
    
elif age <= 21:
    print("Sorry you are not allowed to enter unless accomponied by an adult 21 or over.  ")

if age >= 21:
    print("Here is your ticket please proceed to the line.")
    
if age <= 21:
    print("Please return with an adult 21 years or older. Thanks")
    
print("Thanks for visiting Air Breeze Cruise Lines.")
    