import argparse
from datetime import datetime
from colorama import Fore, Style, init
from checker import check_password
from generator import generate_password

init(autoreset=True)


def format_report(password, result):
    lines = []
    lines.append("PASSWORD SECURITY REPORT")
    lines.append("=" * 30)
    lines.append(f"Password: {password}")
    lines.append(f"Generated at: {datetime.now()}")
    lines.append("-" * 30)

    for key, value in result.items():
        lines.append(f"{key}: {value}")

    return "\n".join(lines)


def save_report(report_text):
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_text)
    return filename


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

    parser.add_argument("--generate", type=int, help="Generate secure password")
    parser.add_argument("--check", type=str, help="Check password strength")
    parser.add_argument("--save", action="store_true", help="Save report to file")

    args = parser.parse_args()

    if args.generate:
        password = generate_password(args.generate)
        print(Fore.GREEN + f"Generated password: {password}")

        if args.save:
            result = check_password(password)
            report = format_report(password, result)
            filename = save_report(report)
            print(Fore.CYAN + f"Report saved to {filename}")

    elif args.check:
        result = check_password(args.check)
        print_colored_result(result)

        if args.save:
            report = format_report(args.check, result)
            filename = save_report(report)
            print(Fore.CYAN + f"Report saved to {filename}")

    else:
        password = input("Enter password: ")
        result = check_password(password)
        print_colored_result(result)

        if args.save:
            report = format_report(password, result)
            filename = save_report(report)
            print(Fore.CYAN + f"Report saved to {filename}")


if __name__ == "__main__":
    main()