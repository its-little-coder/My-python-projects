import string
password = input("Enter your password: ")
has_special = any(char in string.punctuation for char in password)
points = 0
has_number = any(char.isdigit() for char in password)
print("\n----length checking----")

if len(password) >= 8:
    print("Length is good!")
    points += 1
else:
    print("Too short, needs 8+ characters")

print("\n----uppercase checking----")

if password != password.lower():
    print("Has uppercase letter!")
    points += 1
else:
    print("No uppercase letter")

print("\n----lowercase checking----")

if password != password.upper():
    print("Has lowercase letter!")
    points += 1
else:
    print("No lowercase letter!")

print("\n----Number checking----")

if has_number:
    print("Has numbers!")
    points += 1
else:
    print("Does not have numbers")

print("\n----special character----")

if has_special:
    print("Has special characters----")
    points += 1
else:
    print("Does not have special charecters")

print("\n----final result----")

if points == 5:
    print("your pasword is: Unbreakable")
elif points == 4:
    print("your password is: very strong")
elif points == 3:
    print("your password is: strong")
elif points == 2:
    print("your password is: Medium")
else:
    print("your password is: Bad")
