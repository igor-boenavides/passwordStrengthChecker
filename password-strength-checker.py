import string


def main():
    print("WELCOME TO THE PASSWORD strength CHECKER!!!")
    passwd = input("Inform the password for the strength check: ")
    score = digit_minimum(passwd) + upperlower(passwd) + has_digit(passwd) + has_symbols(passwd)
    tell_score(score)

# ----- At least 8 digits (2) -----
def digit_minimum(passwd):
    if len(passwd) >= 8:
        return 2
    else:
        print("Your password is too short.")
        return 0


# ----- A combination of lower and uppercase letter (4) -----
def upperlower(passwd):
    if any(char.islower() for char in passwd) and any(
        char.isupper() for char in passwd
    ):
        return 4
    else:
        print("The password does not contain a combination of uppercase adn lowercase letters.")
        return 0


# ----- Numbers (10) -----
def has_digit(passwd):
    if any(char.isdigit() for char in passwd):
        return 10
    else:
        print("The password does not contain any numbers.")
        return 0

# ----- Symbols (! @ # $) (10) -----
def has_symbols(passwd):
    symbols = list(string.punctuation)
    if any(char in symbols for char in passwd):
        return 10
    else:
        print("The password does not contain symbols.")
        return 0

# ----- Inform score (max. = 26) -----
def tell_score(points):
    if points >= 17.33:
        print(f"Password points: {points}")
        print("Your password is STRONG!!! 💪 💪 💪")
    elif points >= 8.67:
        print(f"Password points: {points}")
        print("Your password is average. 😑 😑 😑")
    else:
        print(f"Password points: {points}")
        print("Your password is WEAK. 💩 💩 💩")


if __name__ == "__main__":
    main()
