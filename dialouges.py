import functions

def space():
    print( "" )

def greetings():
    print( "****************************" )
    print( "Hello adventurer, you seem to need some dice." )
    print( "Fortunately for you, I myself have some of the best dice in the whole kingdom!" )
    print( "Just tell me, what you need." )
    print( "****************************" )

def introduction():
    print( "****************************" )
    print( "Aaahh, you see, my gambling young friend, ..." )
    print( "I used to be a gambler myself, but then I took a D5 to the knee ... The pointy part ..." )
    print( "Now my only joy is to help the young ones with their gambling." )
    print( "So let me help you." )
    print( "****************************" )

def show_selection( dices ):
    print( "****************************" )
    print( "You have selected the following dice:" )

    if len( dices ) < 1:
        print( "Oh my, you have chosen no dice so far!" )
    else:
        print( ", ".join( functions.numbers_to_dice( dices ) ) )
    
    print( "****************************" )

def main_options():
    print( "CHOOSE AN OPTION:" )
    print( "[1] Let the dice roll." )
    print( "[2] Please show me the Dice we are rolling right now." )
    print( "[3] I would like to add a dice." )
    print( "[4] I don't need one of them any more." )
    print( "[5] Excuse me, who are you, again?" )
    print( "[6] I don't have time for that. BE GONE!" )

def dice_result( values, total ):
    print( "****************************" )
    print( "Alea iacta est (The die is cast)" )
    print( values )
    print( "Total: " + str( total ) )
    print( "****************************" )

def offer_new_dice():
    print( "****************************" )
    print( "You can choose one of my Dice. I have every Dice from a D1 to a D36." )
    print( "Just name a dice and we can add them to the list." )
    print( "****************************" )

def error_no_dice():
    print( "****************************" )
    print( "Not so fast, young adventurer!" )
    print( "You haven't chosen any dice to throw!" )
    print( "****************************" )

def error_add_wrong_dice():
    print( "****************************" )
    print( "What did you say, young adventurer?" )
    print( "That doesn't sound like a dice I have ever heard of." )
    print( "Try calling it 'Dsoandso' and say the number of sides where I said soandso" )
    print( "****************************" )

def error_remove_wrong_dice():
    print( "****************************" )
    print( "What did you say, young adventurer?" )
    print( "That one is not even on the list." )
    print( "Try calling it 'Dsoandso' and say the number of sides where I said soandso" )
    print( "****************************" )
