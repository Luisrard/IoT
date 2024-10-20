#21310369

import re

def capture_email():
    return input("Enter an email address: ")

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    email = capture_email()
    if is_valid_email(email):
        print("The email address is valid.")
    else:
        print("The email address is not valid.")

if __name__ == "__main__":
    main()
