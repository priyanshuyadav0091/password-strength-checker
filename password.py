import string

def check_password(password):
    length_ok = len(password) >= 8
    upper_ok = any(c.isupper() for c in password)
    lower_ok = any(c.islower() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_ok = any(c in string.punctuation for c in password)

    score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])

    print("\nPassword Strength Check:")

    if score == 5:
        print("✔ Strong Password")
    elif 3 <= score < 5:
        print("✔ Medium Password")
    else:
        print("✘ Weak Password")

    print("\nMissing Requirements:")
    if not length_ok: print("- Minimum 8 characters")
    if not upper_ok: print("- At least one uppercase letter")
    if not lower_ok: print("- At least one lowercase letter")
    if not digit_ok: print("- At least one number")
    if not special_ok: print("- At least one special character (*, #, @, etc.)")

# Main program
password = input("Enter your password: ")
check_password(password)
