"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730641729"


def input_word() -> str:
    word = input("Enter a 5-character word: ")  # Input asks for word
    if len(word) == 5:  # if word is 5 characters then the word will be returned
        return word
    else:
        print(
            "Error: Word must contain 5 characters."
        )  # If word is not 5 characters it will print an error message
        exit()  # Exit if word does not have 5 character
        return word


def input_letter() -> str:
    letter = input("Enter a single character: ")  # Input asks for single letter
    if len(letter) == 1:  # If letter is single then letter will be returned
        return letter
    else:
        print(
            "Error: Character must be a single character."
        )  # If more than one character is entered error will display
        exit()  # Exit if not single character
        return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    match: int = 0  # Match variable is used count matches

    if word[0] == letter:  # Looks at first character in word
        print(letter + " found at index 0")
        match += 1  # Every time letter is found match count increases
    if word[1] == letter:
        print(letter + " found at index 1")
        match += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        match += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        match += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        match += 1

    if match == 0:  # No matches will print no matches found
        print("No instances of " + letter + " found in " + word)
    elif match == 1:  # 1 match will print 1 instance found
        print("1 instance of " + letter + " found in " + word)
    else:  # More than 1 uses instances
        print(str(match) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
