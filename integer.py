#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 3, 2022
# This program asks for an integer
# and tells you if the integer is
# positive, negative, or zero


def main():
    # input
    print("This program asks for an integer")
    print("and tells you if the integer is")
    print("positive, negative, or zero")
    print("")
    user_num = int(input("Enter any integer: "))

    # process/output
    if user_num < 0:
        print("Your number is negative.")
    elif user_num > 0:
        print("Your number is positive.")
    elif user_num == 0:
        print("Your number is zero.")
    else:
        print("An irregularity has occurred.")


if __name__ == "__main__":
    main()
