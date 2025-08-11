# Ask user to enter their first name
# Ask user to enter their last name
# Print user's fullname in UPPERCASE
# e.g. If user's fullname is Michael Hammond, it should rather print MICHAEL HAMMOND

first_name = input("Enter your first name: \n")
last_name = input("Enter your last name: \n")
print("Your full name is : " + first_name.upper() +" "+ last_name.upper())

# OR

first_name = input("Enter your first name: \n")
last_name =  input("Enter your last name: \n")
full_name = first_name +" "+ last_name
full_name = full_name.upper()
print("Your full name is: " + full_name)

