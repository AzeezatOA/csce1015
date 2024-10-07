# Credit Card Validator version .1
# This is the world's worst credit card number validator. It checks to see if the number is 16 digits long and that is it.  

# anything that starts with a pound sign (hashtag if you are under 30) is a comment. The computer ignores these.

#a function that uses the luhn code
import luhn
def is_credit_card_valid(card_number):
    return luhn.verify(card_number)
# Let's tell the world whose awful credit card validator this is.
print ("Azeezat Akinboro Modified This Credit Card Validator")

# Let's get the card number from the user
card_number = input("Enter your 16-digit credit card number: ")

# Check if card number is 16 digits long

# len means 'length', and the '==' is testing one thing against the other. A single equal sign would set one thing equal to the other (not what we want to do). 
# card_number.isdigit() is checking if this is numbers instead of someone typing 'cheeseburger' for their credit card number.

if is_credit_card_valid(card_number):     
    print ("The credit card number is valid.")
else:
    print ("The credit card number is invalid.") 
