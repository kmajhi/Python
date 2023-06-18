def count_notes(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    notes_count = {}

    for note in denominations:
        if amount >= note:
            count = amount // note
            notes_count[note] = count
            amount -= count * note

    print("Total number of notes:")
    for note, count in notes_count.items():
        print(f"{note} rupee notes: {count}")

# Example usage
amt = int(input("Enter the amount: "))
count_notes(amt)
