def check_alphabet(character):
    if character.isalpha():
        print(f"{character} is an alphabet.")
    else:
        print(f"{character} is not an alphabet.")

# Example usage
char = input("Enter a character: ")
check_alphabet(char)
