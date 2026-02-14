import argparse
from colorama import Fore, Style, init
from checker import check_password
from generator import generate_password

init(autoreset=True)


def print_colored_result(result):
    print("\nPassword analysis:")

    for key, value in result.items():
        if key == "strength":
            if value in ["Weak", "Very Weak"]:
                print(Fore.RED + f"{key}: {value}")
            elif value == "Medium":
                print(Fore.YELLOW + f"{key}: {value}")
            else:
                print(Fore.GREEN + f"{key}: {value}")
        else:
            print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(description="Password Security Tool")

    parser.add_argument(
        "--generate",
        type=int,
        help="Generate secure password with given length"
    )

    parser.add_argument(
        "--check",
        type=str,
        help="Check strength of given password"
    )

    args = parser.parse_args()

    if args.generate:
        password = generate_password(args.generate)
        print(Fore.GREEN + f"Generated password: {password}")

    elif args.check:
        result = check_password(args.check)
        print_colored_result(result)

    else:
        password = input("Enter password: ")
        result = check_password(password)
        print_colored_result(result)


if __name__ == "__main__":
    main()
