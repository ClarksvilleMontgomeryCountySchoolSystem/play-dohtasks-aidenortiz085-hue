"""
ANSWER BOX - Copy the strings you need:

"long body or round body?"
") Add a small bump using {color2} to the back.\n"
") Roll a smaller ball using {color1} for the head.\n"
") Keep it as a ball.\n"
"long tail or short tail?"
") Roll a ball using {color1}.\n"
") Add four small legs to the bottom using {color1}.\n"
") Roll a thin rope using {color2} and attach to the back.\n"
") Name this creation: "Mouse""
") Roll the ball into an egg shape.\n"
") Add two dots for eyes and a tiny nose.\n"
") Attach the head to one end of the body.\n"
"""

def main():
    color1 = "gray"
    color2 = "pink"
    print(f"1) Roll a ball using {color1}.\n")
    choice1 = input("long body or round body? ").lower()
    # CAUTION: You must include the word "body" when checking!
    if "body" in choice1 and "long" in choice1:
        print("2) Roll the ball into an egg shape.\n")
    elif "body" in choice1 and "round" in choice1:
        print("2) Keep it as a ball.\n")
    print(f"3) Roll a smaller ball using {color1} for the head.\n")
    print("4) Attach the head to one end of the body.\n")
    choice2 = input("long tail or short tail? ").lower()
    if "tail" in choice2 and "long" in choice2:
        print(f"5) Roll a thin rope using {color2} and attach to the back.\n")
    elif "tail" in choice2 and "short" in choice2:
        print(f"5) Add a small bump using {color2} to the back.\n")
    print(f"6) Add four small legs to the bottom using {color1}.\n")
    print("7) Add two dots for eyes and a tiny nose.\n")
    print('8) Name this creation: "Mouse"')







if __name__ == "__main__":
    main()
