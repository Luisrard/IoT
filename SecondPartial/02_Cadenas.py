#21310369

def capture_text():
    return input("Enter a text string: ")

def is_first_letter_upper(text: str):
    return text[0].isupper()

def count_words(text: str):
    return len(text.split())

def list_words(text: str):
    return text.split()

def reverse_string(text: str):
    return text[::-1]

def capitalize_last_letter(text: str):
    words = text.split()
    modified_words = [word[:-1] + word[-1].upper() for word in words]
    return ' '.join(modified_words)

def main():
    string = capture_text()
    print("Is the first letter uppercase?", is_first_letter_upper(string))
    print("Number of words:", count_words(string))
    print("List of words:", list_words(string))
    print("Reversed string:", reverse_string(string))
    print("String with last letter of each word capitalized:", capitalize_last_letter(string))

if __name__ == "__main__":
    main()
