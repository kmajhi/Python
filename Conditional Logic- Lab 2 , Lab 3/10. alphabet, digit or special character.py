def check_character_type(character):
    if character.isalpha():
        return "Alphabet"
    elif character.isdigit():
        return "Digit"
    else:
        return "Special Character"


# Main program
input_character = input("Enter a character: ")

character_type = check_character_type(input_character)

print(f"The character '{input_character}' is a {character_type}.")
