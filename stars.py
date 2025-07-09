def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

# Example usage:
if __name__ == "__main__":
    ch = input("Enter a character: ")
    if len(ch) == 1 and ch.isalpha():
        if is_vowel(ch):
            print(f"{ch} is a vowel.")
        else:
            print(f"{ch} is not a vowel.")
    else:
        print("Please enter a single alphabetic character.")