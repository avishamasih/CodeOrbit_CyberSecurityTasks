"""
Password Strength Checker
--------------------------
A simple Python script that checks whether a password is strong or weak,
based on length, character variety, and gives suggestions for improvement.

Author: <Avisha Masih>
Internship: CodeOrbit Tech - Cyber Security Internship
"""

import string


def check_password_strength(password: str) -> dict:
    """
    Analyze a password and return a report dict with:
    - score (0-5)
    - strength label
    - list of missing criteria (suggestions)
    """
    length_ok = len(password) >= 8
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    criteria = {
        "At least 8 characters long": length_ok,
        "Contains lowercase letters (a-z)": has_lower,
        "Contains uppercase letters (A-Z)": has_upper,
        "Contains numbers (0-9)": has_digit,
        "Contains special characters (!@#$...)": has_special,
    }

    score = sum(criteria.values())

    if score <= 2:
        strength = "Weak"
    elif score in (3, 4):
        strength = "Moderate"
    else:
        strength = "Strong"

    missing = [rule for rule, passed in criteria.items() if not passed]

    return {
        "password": password,
        "score": score,
        "max_score": len(criteria),
        "strength": strength,
        "missing": missing,
    }


def print_report(report: dict) -> None:
    print("\n--- Password Strength Report ---")
    print(f"Password checked : {'*' * len(report['password'])}")
    print(f"Score            : {report['score']} / {report['max_score']}")
    print(f"Strength         : {report['strength']}")

    if report["missing"]:
        print("\nTo improve your password, add the following:")
        for tip in report["missing"]:
            print(f"  - {tip}")
    else:
        print("\nGreat! Your password meets all the recommended criteria.")
    print("---------------------------------\n")


def main():
    print("=== Password Strength Checker ===")
    print("(Note: your password is not stored or sent anywhere.)\n")

    while True:
        pwd = input("Enter a password to check (or 'q' to quit): ")
        if pwd.lower() == "q":
            print("Goodbye!")
            break
        report = check_password_strength(pwd)
        print_report(report)


if __name__ == "__main__":
    main()