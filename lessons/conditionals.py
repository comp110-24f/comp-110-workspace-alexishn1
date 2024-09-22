"""Practice with Conditionals"""


# 1
def less_than_10(num: int) -> None:
    """Tell me if num is <10"""
    dub: int = num * 2
    print(dub)
    if num < 10:
        print("Small number")
    else:
        print("Big number")


less_than_10(num=11)


# 2
def should_I_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:
        print("Eat food")  # then block
    else:
        print("Do your homework instead")  # else block
    print("I am proud of you")


should_I_eat(hungry=True)


# 3
def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match"


print(check_first_letter(word="happy", letter="h"))



# 4
def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold"
        print("Bring a jacket!")
    else:
        if weather == "hot"
            print("Keep cool out there!")
        else:
            print("I don't recognize this weather")
        return weather