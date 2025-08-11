# Ask user to input an integer
# Determine the modulo  of the integer
# If remainder is equal to 0, print Even
# Else print Odd

# number = int(input("Enter your number: \n"))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

    # OR

# entry = int(input("Enter the integer \n"))
# integer = entry%2

# if integer == 0:
#         print("Even")
# else:
#         print("Odd")

# ANOTHER QUESTION

# Ask user to input their score as a number
# If score is between 90 to 100 (inclusive) print grade A
# If score is between 80 to 89 (inclusive) print grade B
# If score is between 70 to 79 (inclusive) print grade C
# If score is between 60 to 69 (inclusive) print grade D
# If score is between 0 to 59 (inclusive) print grade F

score = int(input("Enter your score: \n"))

if score >=90 and score <= 100:
    print("Grade A")

elif score >=80 and score <= 89:
    print("Grade B")

elif score >=70 and score <= 79:
    print("Grade C")

elif score >=60 and score <= 69:
    print("Grade D")

elif score >=0 and score <= 59:
    print("Grade F")
