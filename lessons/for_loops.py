"""For loops practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# Tell every pet they're good boy!
for puppy in pets:
    print("Good boy, " + puppy + "!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(str(idx) + ":" + names[idx])
