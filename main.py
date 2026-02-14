import argparse
import os
import getpass
from datetime import datetime
from colorama import Fore, init
from checker import check_password
from generator import generate_password
from pdf_report import save_pdf_report

init(autoreset=True)


def format_report(password, result):
    lines = []
    lines.append("PASSWORD SECURITY REPORT")
    lines.append("=" * 40)
    lines.append(f"Password: {password}")
    lines.append(f"Generated at: {datetime.now()}")
    lines.append("-" * 40)

    for key, value in result.items():
        lines.append(f"{key}: {value}")

    return "\n".join(lines)


def save_txt_report(report_text):
    os.makedirs("reports", exist_ok=True)

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join("reports", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_text)

    return filepath


def print_colored_result(result):
    print("\nPassword analysis:\n")

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
    parser.add_argument("--hidden", action="store_true", help="Enter password in hidden mode")
    parser.add_argument("--save", action="store_true", help="Save report as TXT")
    parser.add_argument("--pdf", action="store_true", help="Save report as PDF")

    args = parser.parse_args()

    password = None
    result = None

    if args.generate:
        password = generate_password(args.generate)
        print(Fore.GREEN + f"\nGenerated password: {password}\n")
        result = check_password(password)

    elif args.check:
        password = args.check
        result = check_password(password)

    elif args.hidden:
        password = getpass.getpass("Enter password (hidden): ")
        result = check_password(password)

    else:
        password = getpass.getpass("Enter password (hidden): ")
        result = check_password(password)

    print_colored_result(result)

    if args.save:
        report = format_report(password, result)
        filename = save_txt_report(report)
        print(Fore.CYAN + f"\nTXT report saved to {filename}")

    if args.pdf:
        filename = save_pdf_report(password, result)
        print(Fore.CYAN + f"PDF report saved to {filename}")


if __name__ == "__main__":
    main()