import re
from entropy import calculate_entropy


def check_password(password):
    result = {}

    result["length"] = len(password)
    result["has_lowercase"] = bool(re.search(r"[a-z]", password))
    result["has_uppercase"] = bool(re.search(r"[A-Z]", password))
    result["has_digits"] = bool(re.search(r"[0-9]", password))
    result["has_special"] = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    result["is_common"] = is_common_password(password)

    result["entropy"] = round(calculate_entropy(password), 2)

    return result


def evaluate_strength(result):
    if result["is_common"]:
        return "Very Weak"

    score = 0

    if result["length"] >= 8:
        score += 1
    if result["has_lowercase"]:
        score += 1
    if result["has_uppercase"]:
        score += 1
    if result["has_digits"]:
        score += 1
    if result["has_special"]:
        score += 1
    if result["entropy"] > 50:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def is_common_password(password):
    try:
        with open("common_passwords.txt", "r", encoding="utf-8") as f:
            common_passwords = {line.strip() for line in f}
        return password in common_passwords
    except FileNotFoundError:
        return False