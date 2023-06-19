def check_character_case(character):
    if character.isupper():
        return "Uppercase"
    elif character.islower():
        return "Lowercase"
    else:
        return "Not an alphabet"


# Main program
input_character = input("Enter a character: ")

case_type = check_character_case(input_character)

print(f"The character '{input_character}' is {case_type}.")
