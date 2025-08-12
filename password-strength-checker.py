import string

def main():
    print("===========================================")
    print("WELCOME TO THE PASSWORD strength CHECKER!!!")
    print("===========================================")
    print()
    password = input("Inform the password for the strength check: ")
    strength_check(password)

def strength_check(passwd):
    strength_score = 0

    # ----- At least 8 digits (2) -----
    if len(passwd) >= 8:
        strength_score += 2
    else:
        print("Your password is too short.")

    # ----- A combination of lower and uppercase letter (4) -----
    if any(char.islower() for char in passwd) and any(
        char.isupper() for char in passwd
    ):
        strength_score += 4
    else:
        print(
            "The password does not contain a combination of uppercase adn lowercase letters."
        )

    # ----- Numbers (10) -----
    if any(char.isdigit() for char in passwd):
        strength_score += 10
    else:
        print("The password does not contain any numbers.")

    # ----- Symbols (! @ # $) (10) -----
    symbols = list(string.punctuation)
    if any(char in symbols for char in passwd):
        strength_score += 10
    else:
        print(
            "The password does not contain symbols."
        )

    # ----- Inform score (max. = 26) -----
    if strength_score >= 17.33:
        print(f"Password points: {strength_score}")
        print("Your password is STRONG!!! 💪 💪 💪")
    elif strength_score >= 8.67:
        print(f"Password points: {strength_score}")
        print("Your password is average. 😑 😑 😑")
    else:
        print(f"Password points: {strength_score}")
        print("Your password is WEAK. 💩 💩 💩")


if __name__ == "__main__":
    main()
