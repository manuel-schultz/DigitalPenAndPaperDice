import dialouges
import random
import re
import sys

# Receiving an array of numbers and return an array with dice like D6.
def numbers_to_dice( numbers ):
    dices = []

    for n in numbers:
        dices.append( number_to_dice( n ) )
    return dices

# Receiving asingle number and return a single dice like D6.
def number_to_dice( n ):
    return "D" + str( n )

# Wait for user main input and call actions acordingly.
def wait_for_main_choice( dice ):
    main_choice = input( "I choose: " )
    match main_choice:
        case "1":
            dice_roll( dice )
        case "2":
            dialouges.space()
            dialouges.space()
            dialouges.show_selection( dice )
        case "3":
            dice = add_dice( dice )
        case "4":
            dice = remove_dice( dice )
        case "5":
            dialouges.space()
            dialouges.space()
            dialouges.introduction()
        case "6" | "close" | "exit" | "c":
            close_app()
        case _:
            try_again()

# Create random numbers for all active dice. Also display results.
def dice_roll( dice ):
    dialouges.space()
    dialouges.space()

    if len( dice ) == 0:
        dialouges.error_no_dice()
        return

    pips   = []
    values = ""
    total  = 0
        
    for d in dice:
        if d != 1:
            pip = random.randrange( 1, d )
        else:
            pip = 1
        pips.append( pip )
        total += pip

    for pip in pips:
        values += str( pip ) + ", "
    
    values = values[:-2]
    dialouges.dice_result( values, total )

# Add one dice to the list of active dice.
def add_dice( dice ):
    dialouges.space()
    dialouges.space()
    dialouges.offer_new_dice()
    dialouges.space()
    dialouges.space()

    while True:
        d            = input( "The dice, my heart demands is a: " )
        regex_result = re.search( "^[D|d](\d{1,2})$", d )

        if regex_result and int( regex_result.group( 1 ) ) < 37 and int( regex_result.group( 1 ) ) > 0:
            break
        else:
            dialouges.space()
            dialouges.space()
            dialouges.error_add_wrong_dice()
            dialouges.space()
            dialouges.space()

    dice.append( int( regex_result.group( 1 ) ) )
    return dice

# Remove one dice of the list of active dice.
def remove_dice( dice ):
    dialouges.space()
    dialouges.space()
    while True:
        dialouges.show_selection( dice )

        if len( dice ) < 1:
            return dice
        
        d            = input( "I don't need this one anymore:" )
        regex_result = re.search( "^[D|d](\d{1,2})$", d )

        if regex_result and int( regex_result.group( 1 ) ) in dice:
            break
        else:
            dialouges.space()
            dialouges.space()
            dialouges.error_remove_wrong_dice()
            dialouges.space()
            dialouges.space()
        
    dice.remove( int( regex_result.group( 1 ) ) )
    return dice

# An empty function to redo the main choosing event.
def try_again():
    # Do nothing, Code will recall the main_choice functionality.
    # To fix the Expected indented block error we need to do something.
    a = 1

# Close the python script.
def close_app():
    sys.exit()
