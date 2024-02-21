import os
import re
import sys

import dialouges
import random

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
    if main_choice == "1":
        dice_roll( dice )
    elif main_choice == "2":
        os.system( "cls" )
        dialouges.show_selection( dice )
    elif main_choice == "3":
        dice = add_dice( dice )
        os.system( "cls" )
        dialouges.show_selection( dice )
    elif main_choice == "4":
        dice = remove_dice( dice )
        os.system( "cls" )
        dialouges.show_selection( dice )
    elif main_choice == "5":
        os.system( "cls" )
        dialouges.introduction()
    elif main_choice == "6" or main_choice == "close" or main_choice == "c" or main_choice == "exit" or main_choice == "x":
        close_app()
    else:
        try_again()

# Create random numbers for all active dice. Also display results.
def dice_roll( dice ):
    if len( dice ) == 0:
        os.system( "cls" )
        dialouges.error_no_dice()
        return

    pips   = []
    values = ""
    total  = 0
        
    for d in dice:
        if d != 1:
            pip = random.randrange( 1, d + 1 )
        else:
            pip = 1
        pips.append( pip )
        total += pip

    for pip in pips:
        values += str( pip ) + ", "
    
    values = values[:-2]
    os.system( "cls" )
    dialouges.dice_result( values, total )

# Add one dice to the list of active dice.
def add_dice( dice ):
    os.system( "cls" )
    dialouges.offer_new_dice()
    dialouges.space()
    dialouges.space()

    while True:
        d            = input( "The dice, my heart demands is a: " )
        regex_result = re.search( "^[D|d](\d{1,2})$", d )

        if regex_result and int( regex_result.group( 1 ) ) < 37 and int( regex_result.group( 1 ) ) > 0:
            break
        else:
            os.system( "cls" )
            dialouges.error_add_wrong_dice()
            dialouges.space()
            dialouges.space()

    dice.append( int( regex_result.group( 1 ) ) )
    return dice

# Remove one dice of the list of active dice.
def remove_dice( dice ):
    while True:
        os.system( "cls" )
        dialouges.show_selection( dice )

        if len( dice ) < 1:
            return dice
        
        d            = input( "I don't need this one anymore:" )
        regex_result = re.search( "^[D|d](\d{1,2})$", d )

        if regex_result and int( regex_result.group( 1 ) ) in dice:
            break
        else:
            os.system( "cls" )
            dialouges.error_remove_wrong_dice()
            dialouges.space()
            dialouges.space()

    dice.remove( int( regex_result.group( 1 ) ) )
    return dice

# An empty function to redo the main choosing event.
def try_again():
    # Do nothing, Code will recall the main_choice functionality.
    # To fix the Expected indented block error we need to do something.
    os.system( "cls" )

# Close the python script.
def close_app():
    sys.exit()
