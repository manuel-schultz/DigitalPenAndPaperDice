import functions
import dialouges

dice = []

dialouges.greetings()
dialouges.space()
dialouges.space()
dialouges.space()
dialouges.space()

while True:
    dialouges.main_options()
    functions.wait_for_main_choice( dice )
    dialouges.space()
    dialouges.space()
