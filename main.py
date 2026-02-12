from checker import check_password

def main():
    password = input("Enter password: ")
    result = check_password(password)

    print("\nPassword analysis:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()