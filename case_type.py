# day = int(input("Enter your number: \n"))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Not a day")


users = input("Enter username: \n")

match users:
    case "Kofi" | "Kwadwo" | "Kwabena" | "Yaw":
        print("This is a boy")

    case "Ama" | "Abena" | "Akua" | "Afia":
        print("This is a girl")

    case _:
        print("None")

