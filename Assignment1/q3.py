password = input("Enter password: ")

lower = False
upper = False
digit = False
special = False

for ch in password:
    if ch >= 'a' and ch <= 'z':
        lower = True
    elif ch >= 'A' and ch <= 'Z':
        upper = True
    elif ch >= '0' and ch <= '9':
        digit = True
    elif ch in "$#@":
        special = True

if lower and upper and digit and special and len(password) >= 6 and len(password) <= 16:
    print("Valid password")
else:
    print("Invalid password")
