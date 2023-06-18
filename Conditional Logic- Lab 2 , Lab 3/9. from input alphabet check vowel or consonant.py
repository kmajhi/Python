def check_vowel_consonant(character):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if character.lower() in vowels:
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")

# Example usage
char = input("Enter an alphabet: ")
check_vowel_consonant(char)
