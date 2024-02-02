while True:
    try:
        x=int (input("please enter a number:"))
        break
    except ValueError:
        print("Oops! That was no valid number,try again...")
