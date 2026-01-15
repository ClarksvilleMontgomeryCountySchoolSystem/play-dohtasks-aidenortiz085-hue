
"""
ANSWER BOX - Copy the strings you need:

"standing up or flopped down?"
") Keep it round.\n"
") Attach two pieces using {color2} hanging downward.\n"
") Name this creation: "Dog""
") Roll a smaller ball using {color1} for the head.\n"
"hot dog or round like a ball?"
") Roll a ball using {color1} for the body.\n"
") Attach two pointed pieces using {color2} upright.\n"
") Attach the head to the body.\n"
") Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n"
") Stretch it out.\n"
"""

def main():
    color1 = "brown"
    color2 = "black"
    print("1)hot dog or round like a ball?")
    choice1 = input()
    if choice1 == "hot dog":
        print("2)) Stretch it out.\n")
    elif choice1 == "round like a ball":
        print(f"2)) Roll a ball using {color1} for the body.\n")
    print(f"3) Roll a smaller ball using {color1} for the head.\n")
    print("4) Attach the head to the body.\n")
    print("5)standing up or flopped down?")
    choice2 = input()
    if choice2 == "standing up":
        print(f"6) Attach two pointed pieces using {color2} upright.\n")
    elif choice2 == "flopped down":
        print(f"6) Attach two pieces using {color2} hanging downward.\n")
    print("7) Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n")


if __name__ == "__main__":
    main()
