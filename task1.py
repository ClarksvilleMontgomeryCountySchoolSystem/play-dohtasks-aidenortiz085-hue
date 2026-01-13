def main():
    # Enter your color.
    color1 = "green"

    print(f"1) Use {color1} to roll a medium-sized ball.\n")
    choice1 = input("big or small? ")
    # == Is used to test for equality.
    if choice1 == "big":
        print("2) Flatten the ball into a wide disc.\n")
    else:
        print("2) Keep it as a ball.\n")
    print("3) Roll four small pieces into short ropes.\n")
    print("4) Attach them to the bottom.\n")
    print(f"5) Use {color1} to roll a small ball.\n")
    print("6) Attach it to one side.\n")
    #Go to user - Include a space after the ? in your prompt.
    # Collect input. Use choice2 Prompt:"option 1 or option 2? "
    choice2 = input("option 1 or option 2? ")
    # Use == to check the User's choice.
    # Remember you are checking equality to a string. You must use quotes.
    if choice2 == "option 1":
        print("7) Pinch the small ball to make it pointy.\n")
    else:
        print("7) Keep the small ball round.\n")
    print("8) Poke two tiny holes in the small ball for eyes.\n")
    print('9) Write "Turtle" on the name card.')

if __name__ == "__main__":
    main()
