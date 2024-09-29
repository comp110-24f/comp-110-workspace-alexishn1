"""EX03 Assignment"""

__author__ = "730641729"


def input_guess(secret_word_len: int) -> str:
    guess = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(guess) != secret_word_len
    ):  # While Guess length is not equal to word length print try again
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Char is being searched in search_word & returns T or F if the char is in word"""
    assert len(char_guess) == 1  # Makes sure char_guess is only one character
    return char_guess in secret_word


def emojified(guess: str, secret: str) -> str:
    """Comapres guess and word and returns correct emoji str"""
    assert len(guess) == len(secret)  # Guess and word must be same length
    # Emojis
    WHITE_BOX: str = "\U00002B1C"  # White emoji
    GREEN_BOX: str = "\U0001F7E9"  # Green emoji
    YELLOW_BOX: str = "\U0001F7E8"  # Yellow emoji
    result: str = ""  # Result of emoji str
    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX  # If char matches display green box(correct)
        elif contains_char(secret, guess[index]):
            result += (
                YELLOW_BOX  # If char is in word but not right place display yellow box
            )
        else:
            result += WHITE_BOX  # If char is not in word display white box(incorrect)

        index += 1  # Keep moving to next character
    return result  # Return emoji


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1  # Turn starts at 1
    turn_max: int = 6  # Can only take 6 turns(guesses)
    win = False
    while turn_count <= turn_max and not win:
        print(f"=== Turn {turn_count}/{turn_max} ===")  # Shows how many turns used
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)  # Prints results of emoji

        if guess == secret:
            win = True  # Win changes to true and win message with display
        else:
            turn_count += (
                1  # If guess and secret word do not match then add to turn length
            )
    if win:
        print(
            f"You won in {turn_count}/{turn_max} turns!"
        )  # Displays message of winning
    else:
        print(
            f"X/{turn_max} - Sorry, try again tomorrow!"
        )  # Displays message of losing


if __name__ == "__main__":
    main(secret="codes")
