def main():
    print("Welcome to the tip calculator!")

    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    amt = bill * (tip+100)/100
    share = amt / people
    final_amt = "{:.2f}".format(share)
    print(f"Each person should pay: ${final_amt}")


if __name__ == "__main__":
    main()