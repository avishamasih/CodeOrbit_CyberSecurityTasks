# CodeOrbit Tech — Cyber Security Internship



![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)




![Internship](https://img.shields.io/badge/Internship-CodeOrbit%20Tech-teal)




![Status](https://img.shields.io/badge/Status-Completed-brightgreen)



A collection of beginner-friendly cybersecurity projects built during the **1-Month Cyber Security Internship at CodeOrbit Tech**. The projects cover password security, basic cryptography, and phishing awareness using plain Python with no external libraries.

**Author:** Avisha Masih

---

## Projects

| # | Project | Type | File |
|---|---------|------|------|
| 1 | Password Strength Checker | Python script | [`password_strength_checker.py`](CodeOrbit_Internship/password_strength_checker.py) |
| 2 | Caesar Cipher Encryption Tool | Python script | [`caesar_cipher_tool.py`](CodeOrbit_Internship/caesar_cipher_tool.py) |
| 3 | Phishing Email Identifier | Report / Checklist | [`pishing_email_identifier.md`](CodeOrbit_Internship/pishing_email_identifier.md) |

---

## 1. Password Strength Checker

Checks whether a password is **Weak**, **Moderate**, or **Strong** and tells the user exactly how to improve it.

**What it checks**
- Minimum length of 8 characters
- Lowercase letters (a-z)
- Uppercase letters (A-Z)
- Numbers (0-9)
- Special characters (!@#$...)

**Scoring:** 0–2 = Weak, 3–4 = Moderate, 5 = Strong

**Sample output**
```
--- Password Strength Report ---
Password checked : *****
Score            : 1 / 5
Strength         : Weak

To improve your password, add the following:
  - At least 8 characters long
  - Contains uppercase letters (A-Z)
  - Contains numbers (0-9)
  - Contains special characters (!@#$...)
```

The password is masked in the output and is never stored or sent anywhere.

---

## 2. Caesar Cipher Encryption Tool

Encrypts and decrypts text using the classic Caesar Cipher, where every letter is shifted by a fixed number of positions (the key).

**Features**
- User-defined shift key
- Handles both uppercase and lowercase letters
- Numbers, spaces, and symbols stay unchanged
- Shows the original, encrypted, and decrypted text together
- Input validation for the key

**Sample output**
```
Original message : Hello, World!
Shift key        : 3
Encrypted output : Khoor, Zruog!
Decrypted output : Hello, World!  (should match original)
```

---

## 3. Phishing Email Identifier

A report on how to spot phishing emails, including:
- An 8-point red-flag checklist (urgent language, mismatched links, spoofed senders, and more)
- Analysis of 5 sample emails, with a verdict and the signs behind each one
- Key takeaways for staying safe online

Read the report: [`pishing_email_identifier.md`](CodeOrbit_Internship/pishing_email_identifier.md)

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

1. Download or clone this repository.
2. Open a terminal inside the `CodeOrbit_Internship` folder.
3. Run any tool:

```bash
python password_strength_checker.py
python caesar_cipher_tool.py
```

---

## Skills Demonstrated

- Python fundamentals (functions, loops, string operations, input validation)
- Basic cryptography concepts
- Security awareness and phishing analysis
- Technical documentation

---

## About the Internship

These projects were completed as part of the Cyber Security Internship by [CodeOrbit Tech](https://www.codeorbittech.in), Bangalore, India.

## License

This project is for educational purposes.
