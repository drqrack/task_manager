# Open the file emails.txt in READ mode
# Read and split the data using \n to get a list
# Loop over the list of emails and print a generated username for each of them,
# i.e username is all characters before the @

file = open("email.txt", "r")
emails = file.read().split("\n")

# for email in emails:
#     print(f"{email.split("@")[0]}")     #splits the email from the @ into two, then display the first index, i.e [0]


# Different approach
# for email in emails:
#     print(email.split("@")[0])

# Different approach
for email in emails:
    username = email.split("@")
    print(username[0])