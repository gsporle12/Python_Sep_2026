#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: This script will simulate a high street bank PIN ATM.

master_pin = "1234"
pin = None
attempts = 0


while pin != master_pin and attempts < 3:
    pin = input("Please enter your PIN: ")
    if pin == master_pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Please try again.")
        attempts += 1
        print(f"You have {3 - attempts} attempts left.")
else:
    # Executes only when the while loop becomes False. (If attempts are above 3)
    print("Maximum number of attempts. Please go away.")

print("Done.")