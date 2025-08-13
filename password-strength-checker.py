import string


def main():
    print("WELCOME TO THE PASSWORD strength CHECKER!!!")
    passwd = input("Inform the password for the strength check: ")
    score = 0
    digit_minimum(passwd, score)
    upperlower(passwd, score)
    has_digit(passwd, score)
    has_symbols(passwd, score)

# ----- At least 8 digits (2) -----
def digit_minimum(passwd, score):
    if len(passwd) >= 8:
        score += 2
    else:
        print("Your password is too short.")


# ----- A combination of lower and uppercase letter (4) -----
def upperlower(passwd, score):
    if any(char.islower() for char in passwd) and any(
        char.isupper() for char in passwd
    ):
        score += 4
    else:
        print("The password does not contain a combination of uppercase adn lowercase letters.")


# ----- Numbers (10) -----
def has_digit(passwd, score):
    if any(char.isdigit() for char in passwd):
        score += 10
    else:
        print("The password does not contain any numbers.")

# ----- Symbols (! @ # $) (10) -----
def has_symbols(passwd, score):
    symbols = list(string.punctuation)
    if any(char in symbols for char in passwd):
        score += 10
    else:
        print(
            "The password does not contain symbols."
        )

# ----- Inform score (max. = 26) -----
def tell_score(score):
    if score >= 17.33:
        print(f"Password points: {score}")
        print("Your password is STRONG!!! 💪 💪 💪")
    elif score >= 8.67:
        print(f"Password points: {score}")
        print("Your password is average. 😑 😑 😑")
    else:
        print(f"Password points: {score}")
        print("Your password is WEAK. 💩 💩 💩")


if __name__ == "__main__":
    main()
