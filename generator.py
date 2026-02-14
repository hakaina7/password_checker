import secrets
import string


def generate_password(length=16):
    if length < 8:
        raise ValueError("Password length must be at least 8")

    alphabet = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))

        # гарантируем наличие всех типов символов
        if (
            any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)
        ):
            return password