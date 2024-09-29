"""Scope example"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char
    removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1
    return copy


word: str = "yoyo"  # Global variable
print(remove_chars(msg=word, char="y"))  # with keyword agruments
print(remove_chars(word, "o"))  # with positional agruments
