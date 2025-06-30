# Modular Chatbot
# Author: Koy Chen & Lynn Qiao
# 15 Apr 2025

# Imports
import random
import time
import os
import sys

# -----------------------------------------------------------------------------

# Platform-specific imports
if os.name == 'nt':  # Windows
    import msvcrt
else:  # Unix-like systems (Linux/macOS)
    import termios
    import tty

# Game state
game_state = {
    "Late": False,
    "GrahamAnger": 0,
    "GraysonAnger": 0,
    "Composure": 0,  
    "Dogbrained": False,
    "Instinct": 0,
    "Office_Remark": False,
    "Office_Silent": False,
    "Office_CallOut": False,
    "GraysonTrustInGraham": 0,
    "GrahamTrustInGrayson": 0,
}


# -----------------------------------------------------------------------------


# Utility Functions
def clear():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Cross-platform get_key function
def get_key():
    """Get a single keypress, supporting arrows and enter."""
    if os.name == 'nt':  # Windows
        first_char = msvcrt.getch()  # Read a single character
        if first_char == b'\xe0' or first_char == b'\x00':  # Arrow keys or special keys
            next_char = msvcrt.getch()
            return first_char + next_char
        else:
            return first_char
    else:  # Unix-like systems
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)  # Set terminal to raw mode
            first_char = sys.stdin.read(1)
            if first_char == '\x1b':  # Escape sequence (e.g., arrow keys)
                next_two = sys.stdin.read(2)
                return first_char + next_two
            else:
                return first_char
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore terminal settings



def arrow_menu(options):
    """Display a menu and allow the player to navigate with arrow keys."""
    index = 0
    print("\n[PLAYER CHOICE - WHAT DO YOU DO?]\n")  # Add spacing before the menu
    while True:
        # Redraw the menu in place
        for i, opt in enumerate(options):
            prefix = "> " if i == index else "  "
            print(f"{prefix}{opt}")
        key = get_key()
        if os.name == 'nt':  # Windows key mappings
            if key == b'\xe0H':  # Up arrow
                index = (index - 1) % len(options)
            elif key == b'\xe0P':  # Down arrow
                index = (index + 1) % len(options)
            elif key == b'\r':  # Enter
                return index
        else:  # Unix-like key mappings
            if key == '\x1b[A':  # Up arrow
                index = (index - 1) % len(options)
            elif key == '\x1b[B':  # Down arrow
                index = (index + 1) % len(options)
            elif key == '\r' or key == '\n':  # Enter
                return index
        # Move the cursor back to the start of the menu
        print(f"\033[{len(options)}A", end="")  # Move up by the number of options

def select(choices):
    """Display a choice menu and return the selected index."""
    selected = arrow_menu(choices)
    clear()  # Clear the screen after the choice is made
    delay_print1(f"You chose: {choices[selected]}")  # Display the chosen option
    time.sleep(2.5)
    clear()
    return selected



def bold_text(text):
    """Return bolded text."""
    return f"\033[1m{text}\033[0m"

def italic_text(text):
    """Return italicized text."""
    return f"\033[3m{text}\033[0m"

def delay_print(s, delay=0.6):
    """Print text with a delay between characters."""
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def delay_print1(s, delay=0.1):
    """Print text with a faster delay."""
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def delay_print2(s, delay=0.05):
    """Print text with a very fast delay."""
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def delay_print3(s, delay=0.025):
    """Print text with an ultra-fast delay."""
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

#SPEAKING FUNCTION
speak = {
    "graham_speak": bold_text("GRAHAM"),
    "grayson_speak": bold_text("GRAYSON")
}
# POV Function
povs = {
    "graham_pov": bold_text("————YOU ARE GRAHAM————"),
    "grayson_pov": bold_text("————YOU ARE GRAYSON————")
}


#-----------------------------------------------------------------------------


# Intro
def main() -> tuple[str, str]:
    delay_print1("Hey there!\n")
    delay_print1("Welcome to our game, No Svoboda.\n")
    time.sleep(1)
    delay_print2("This is a 2 player story game, set in an apocalyptic world. ")
    time.sleep(0.5)
    delay_print2("You will need a friend to play with.")
    time.sleep(3.5)
    
    clear()
    delay_print("...")
    time.sleep(2)

    delay_print3("Your choices will affect how your story plays out throughout the game.")
    time.sleep(4)
    clear()

    # Grab the user's name
    delay_print2("Before we start, I'd like to know your names!\n")
    time.sleep(1)
    player_1 = input ("Player 1, please enter your name: ")
    player_2 = input ("Player 2, please enter your name: ")
    time.sleep(1)

    delay_print2(f"Great! ")
    time.sleep(0.5)
    delay_print2(f"{player_1}, ")
    time.sleep(0.5)
    delay_print2(f"{player_2}, ")
    time.sleep(0.5)
    delay_print2(f" It's a pleasure to meet you both.")
    time.sleep(4)
    clear()
    time.sleep(2)
    return player_1, player_2

if __name__ == "__main__":
    player_1, player_2 = main()

    
    # Character Bios
    characters = {
        "1": {
            "name": bold_text("Graham Emil Svoboda"),
            "bio": f"{bold_text('Age:')} 25\n"
                   f"{bold_text('Occupation:')} Junior Field Analyst at the National Incident Intelligence Agency.\n"
                   f"{bold_text('Job:')} Analyzing data, supporting missions, and assisting in operations.\n"
                   "The nine months before you opened your eyes were the only stillness, "
                   "and solace you’d ever know.\n"
                   "Ever since, you’ve spent your waking days bathed in endless sensory hell, "
                   "the world screaming at you for your stolen peace.\n"
                   "Everywhere you go, you’re burdened to see everything, "
                   "everywhere, "
                   "all at once.\n"
                   "The girl in the corner of the coffee shop turns the page of her book every five sips,\n"
                   "the guy at the counter smells of smoke, "
                   "and constantly eyes her.\n"
                   "You never say more than you need to, "
                   "you’ve seen well enough that actions speak for themselves.\n"
                   "You are perceptive, "
                   "cynical, "
                   "intuitive, "
                   "and a little bit mystical.\n"
        },
        "2": {
            "name": bold_text("Grayson Viktor Novák"),
            "bio": f"{bold_text('Age:')} 28\n"
                   f"{bold_text('Occupation:')} Deputy Director at the National Incident Intelligence Agency.\n"
                   f"{bold_text('Job:')} Overseeing operations, managing teams, and making crucial decisions in high-stake situations.\n"
               "You’re a man of control——over people, "
                   "over situations, "
                   "over your own mind. "
                   "It’s a skill that’s gotten you this far in life.\n"
                   "You clawed your way up from nothing. "
                   "Now you sit at the top.\n"
                   "You’ve seen things most people can’t even imagine, "
                   "and you’ve learned to survive by being sharp, "
                   "strategic, "
                   "and above all, "
                   "untouchable.\n"
        }
    }


    # Display characters
    print("Here are the characters you can choose from:\n")
    time.sleep(1)
    for key, char in characters.items():
       delay_print3(f"{key}. {char['name']}\n")
       delay_print3(f"{char['bio']}\n")
    time.sleep(2)

    # Player 1 chooses a character
    while True:
        player_1_choice = input(f"{player_1}, please choose your character (1 or 2): ")
        if player_1_choice in characters:
            player_1_character = characters[player_1_choice]["name"]
            break
        else:
            print("Invalid choice. Please choose 1 or 2.\n")

    # Player 2 chooses a character
    while True:
        player_2_choice = input(f"{player_2}, please choose your character (1 or 2): ")
        if player_2_choice in characters:
            player_2_character = characters[player_2_choice]["name"]
            if player_2_choice != player_1_choice:
                break
            else:
                print("That character is already taken. Please choose a different character.\n")
                

    # Display chosen characters

    clear()
    time.sleep(1)
    delay_print("...")
    time.sleep(1)
    clear()

    delay_print2(f"Great! ")
    time.sleep(0.3)
    delay_print2(f"{player_1}, ")
    time.sleep(0.3)
    delay_print2(f"you have chosen {player_1_character}.")
    time.sleep(1)
    delay_print2(f"\n{player_2}, ")
    time.sleep(0.3)
    delay_print2(f"you have chosen {player_2_character}.")
    time.sleep(1)
    delay_print2("\nThe game will start in 5 seconds...")
    time.sleep(5)

    clear()
    time.sleep(1)
    delay_print("...")
    time.sleep(1)
    clear()


# -----------------------------------------------------------------------------


# Game Start
# Scene 0A: Morning Routine
# Graham's POV
print(povs["graham_pov"])
delay_print1(italic_text("Somewhere in Prague, May 12, 1997"))
delay_print2(italic_text("\nThe world hasn't ended yet——"))
time.sleep(0.2)
delay_print2(italic_text("but something feels off."))
print("\n")
time.sleep(1)

delay_print2("You see the woman next door carefully tending to her plants.")
time.sleep (0.3)
delay_print2("\nHer husband hugs her from behind and they laugh together, ")
time.sleep (0.2)
delay_print2("the woman tilting her head to look up at him.")
time.sleep (0.25)
delay_print2("\nMixed in with the soft song of their love,")
time.sleep (0.1)
delay_print2(" are dissonant notes of things unsaid.")
time.sleep (1.5)
print("\n")

delay_print2("You can’t tell if you’re imagining it because of what you know——")
time.sleep(0.35)
delay_print2("or if it's really hanging there.")
time.sleep(1)
delay_print2("\nIt's so revolting,")
time.sleep(0.3)
delay_print2(" yet tender.")
time.sleep(0.5)
delay_print2("\nIt makes you dizzy and sick trying to rationalize it.")
time.sleep(1)
print("\n")

delay_print2("You should look away.")
time.sleep(0.6)
delay_print2(" Or you’ll be late.")
time.sleep(0.8)
delay_print2("\nOr worse——")
time.sleep(0.4)
delay_print2("actually throw up.")
time.sleep(4)
print("\n")

choices = [
     "LOOK AWAY",
    "DWELL ON THOUGHT"
 ]
selected = select(choices)
    
if selected == 0:  # LOOK AWAY
    delay_print2("If you throw up right now, you ")
    delay_print2(italic_text("will "))
    delay_print2("look crazy.")
    time.sleep(0.5)
    delay_print2("\nYou look crazy enough as it is, and you’re not enough of a masochist ")
    time.sleep(0.3)
    delay_print2("yet ")
    time.sleep(0.3)
    delay_print2("to enjoy vomiting")
    time.sleep(0.5)
    delay_print2("——or getting yelled at for being late again.")
    time.sleep(3)
    
elif selected == 1:  # DWELL ON THOUGHT
    game_state["Late"] = True
    delay_print2("It makes you sick because you know in ten minutes, ")
    time.sleep(0.3)
    delay_print2("she’ll kiss her husband goodbye, ")
    time.sleep(0.5)
    delay_print2("and in twenty,")
    time.sleep(0.5)
    delay_print2(" she’ll invite the neighbor guy in.")
    time.sleep(1)
    delay_print2("\nBut more so, it makes you sick how it’s the same everywhere——")
    time.sleep(0.5)
    delay_print2("actors playing roles.")
    time.sleep(1)
    print("\n")

    delay_print2("And evidently, ")
    time.sleep(0.4)
    delay_print2("you can’t rip your eyes away from the stage.")
    time.sleep(2)
    print("\n")
    delay_print2("You ")
    delay_print1(italic_text("are "))
    time.sleep(0.1)
    delay_print2("going to be late,")
    time.sleep(0.3)
    delay_print2(" but what matters more is the thrumming ache in your head now.")
    time.sleep(0.5)
    delay_print2("\nThe feeling of fingers digging into your brain, squeezing——")
    time.sleep(0.1)
    delay_print1(italic_text("kneading."))
    time.sleep(0.5)
    delay_print2("\nBut there’s nothing you can do about that.")
    time.sleep(3.5)

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()




# -----------------------------------------------------------------------------



# Scene 0B: Morning Routine
# Grayson's POV
print(povs["grayson_pov"])
delay_print1(italic_text("Somewhere else in Prague,"))
delay_print1(italic_text(" May 12,"))
delay_print1(italic_text(" 1997"))
print("\n")
time.sleep(1)

delay_print2("There’s a stain on the collar of your shirt.")
time.sleep(0.8)
delay_print2(" You rub at it as an attempt to get it off.")
time.sleep(0.8)
print("\n")

delay_print2(" It doesn’t come off.")
time.sleep(0.6)
delay_print2(" Figures.")
time.sleep(1.3)
print("\n")

delay_print2("You check yourself in the mirror.")
time.sleep(0.8)
delay_print2("\nTie, a little off-center.")
time.sleep(0.4)
delay_print2(" It's better that way.")
time.sleep(0.5)
delay_print2(" Perfect symmetry feels desperate.")
time.sleep(0.7)

delay_print2("\nHair, ")
time.sleep(0.3)
delay_print2("dark and combed back, ")
time.sleep(0.7)
delay_print2("neat.")
time.sleep(0.8)
delay_print2("\nEyes, ")
time.sleep(0.3)
delay_print2("olive, narrow, calculated.")
time.sleep(0.8)
delay_print2("\nJaw, ")
time.sleep(0.4)
delay_print2("a little overdue for a shave, but it’ll do.")
time.sleep(2)
print("\n")

delay_print2("You grab your coat, and your half-empty pack of cigarettes.")
time.sleep(0.6)
delay_print2("\nNot for stress.")
time.sleep(0.4)
delay_print2(" Just habit.")
time.sleep(1)

delay_print2("\nThe apartment’s spotless.")
time.sleep(0.5)
delay_print2(" Like you never lived in it.")
time.sleep(1.3)
print("\n")

delay_print2("The hallway smells like old leather and damp stone.")
time.sleep(0.6)
delay_print2(" The fourth-floor neighbor’s dog barks at you as you pass.")
time.sleep(3)
print("\n")

choices = [
    "IGNORE",
    "INTIMIDATE"
]
selected = select(choices)

if selected == 0:  # IGNORE
    delay_print2("You don’t even spare it a glance——")
    time.sleep(0.5)
    delay_print2("but it stops.")
    time.sleep(0.4)
    delay_print2(" Victory.")
    time.sleep(3)

  

elif selected == 1:  # INTIMIDATE
    delay_print2("You stop, and turn, locking eyes with the dog.")
    time.sleep(0.7)
    delay_print2(" You glare with all the malice you can muster,")
    time.sleep(0.5)
    delay_print2(" waiting for it to submit and shut up.")
    time.sleep(2)

    delay_print2("\nIt doesn’t.")
    time.sleep(0.7)
    delay_print2(" The dog just barks louder.")
    time.sleep(1.5)
    delay_print2(" You roll your eyes,")
    time.sleep(0.5)
    delay_print2(" muttering under your breath,")
    time.sleep(0.5)
    delay_print2(" and walk away.")
    time.sleep(3)

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()







# -----------------------------------------------------------------------------





# Scene 1A: Office Arrival
# Grayson's POV
print(povs["grayson_pov"])
delay_print2("The streets outside are damp, ")
time.sleep(0.3)
delay_print2("grey, ")
time.sleep(0.3)
delay_print2("and irritatingly alive. ")
time.sleep(0.8)
delay_print2("You light a cigarette and start walking.")
time.sleep(0.7)
delay_print2("\nThe sky is that ugly shade of early-morning blue. ")
time.sleep(1)
delay_print2("You walk faster, ")
time.sleep(0.4)
delay_print2("not rushing——just avoiding thought.")
time.sleep(2)
print("\n")

delay_print2("The office looms. ")
time.sleep(0.9)
delay_print2("You already know what today is going to be. ")
time.sleep(0.5)
delay_print2("Annoying. ")
time.sleep(0.3)
delay_print2("Pointless.")
time.sleep(1)

delay_print2("\nYou shove the door open. ")
time.sleep(0.5)
delay_print2("Inside, ")
time.sleep(0.3)
delay_print2("you immediately clock the rookie analyst")
time.sleep(0.5) 
delay_print2("——dazed, skittish. ")
time.sleep(0.4)
delay_print2("Already sick of him.")
time.sleep(1)

delay_print2("\nYou toss your coat over the chair like it offended you. ")
time.sleep(0.7)
delay_print2("This is your kingdom.")
time.sleep(0.5)
print("\n")

delay_print2("And he?")
time.sleep(0.5)
delay_print2("\nHe’s today’s entertainment.")
time.sleep(1.2)
print("\n")

delay_print2("You lean back, your gaze fixed on the rookie.")
time.sleep(0.5)
delay_print2("\nHe looks even more pathetic in person——")
time.sleep(0.3)
delay_print2("wiry frame, ")
time.sleep(0.3)
delay_print2("sleeves too long like he inherited that shirt from a brother he hates.")
time.sleep(0.7)
delay_print2("\nHis dark-colored hair curls awkwardly where it’s still damp, ")
time.sleep(0.3)
delay_print2("like he showered but didn’t dry it——")
time.sleep(0.3)
delay_print2("points for effort?")
time.sleep(1)
print("\n")

delay_print2("The poor guy looks lost,")
time.sleep(0.5)
delay_print2("like he’s already regretting today.")
time.sleep(0.5)
delay_print2("\nHis eyes are shifting between the papers in front of him and the cup of coffee that’s been sitting there for too long.")
time.sleep(0.7)
delay_print2("\nThe tension in the air is almost funny——")
time.sleep(0.5)
delay_print2("it’s like he’s trying to make himself invisible, ")
time.sleep(0.5)
delay_print2("and it’s almost pitiful.")
time.sleep(4)
print("\n")

# Player choice
choices = [
    "REMARK",
    "STAY SILENT",
    "CONFRONT"
]

# Display choice menu and get the player's selection
selected = select(choices)

# Handle the player's choice
if selected == 0:  # REMARK
    game_state["Office_Remark"] = True
    delay_print2("You tap your fingers on the desk,")
    time.sleep(0.2)
    delay_print2(" eyes cold.")
    time.sleep(1)
    delay_print2(italic_text('\n"How long do you think you’ll last here before you completely screw up, '))
    time.sleep(0.1)
    delay_print2(italic_text('rookie?"'))
    time.sleep(1)
    delay_print2("\nHis jaw tightens, but he doesn't answer.")
    time.sleep(1)
    delay_print2("\nHe’ll crack, ")
    time.sleep(0.3)
    delay_print2(italic_text("eventually."))
    time.sleep(3.5)

elif selected == 1:  # STAY SILENT
    game_state["Office_Silent"] = True
    delay_print2("You lean back in your chair, ")
    time.sleep(0.3)
    delay_print2("arms crossed,")
    time.sleep(0.3)
    delay_print2(" watching the clock tick by.")
    time.sleep(0.8)
    delay_print2("\nThe rookie shifts nervously under your gaze, ")
    time.sleep(0.3)
    delay_print2("and you wait for him to cave.")
    time.sleep(0.8)
    delay_print2("\nThe tension’s thick, ")
    time.sleep(0.3)
    delay_print2("and you’re enjoying every second of it.")
    time.sleep(3.5)
    print("\n")

elif selected == 2:  # CONFRONT
    game_state["Office_CallOut"] = True
    delay_print2("You eye the pile of untouched paperwork in front of him.")
    time.sleep(0.8)
    delay_print2(italic_text('\n"Not even trying today, '))
    time.sleep(0.1)
    delay_print2(italic_text('huh? '))
    time.sleep(0.3)
    delay_print2(italic_text('At least pretend to look like you’re being productive."'))
    time.sleep(0.5)
    delay_print2("\nThe rookie shoots you a quick glance, ")
    time.sleep(0.3)
    delay_print2("trying to brush it off, ")
    time.sleep(0.3)
    delay_print2("but you can see him scramble to get to work.")
    time.sleep(3.5)
    print("\n")

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()




# -----------------------------------------------------------------------------



# Scene 1B: Office Hell
# Graham's POV
print(povs["graham_pov"])
delay_print1(italic_text("National Incident Intelligence Agency, "))
delay_print1(italic_text("Prague Headquarters,"))
delay_print1(italic_text(" May 12, 1997"))
print("\n")

delay_print2("You hate mornings, ")
time.sleep(.3)
delay_print2("You hate everything about them,") 
time.sleep(.3)
delay_print2(" from the cold to the noise, ")
time.sleep(.3)
delay_print2("to the sense of dread that settles in your stomach.")
time.sleep(.5)
delay_print2("\nBut the office——")
time.sleep(0.3)
delay_print2("you’re more on the fence about it.")
time.sleep(0.7)
delay_print2("\nSometimes it's peacefully monotonous,")
time.sleep(0.3)
delay_print2(" and other times even a room of papers gets on your nerves.")
time.sleep(0.5)
delay_print2("\nYou’re fickle like that.")
time.sleep(1.5)
print("\n")

delay_print2("You’re already at your desk when Grayson——")
time.sleep(0.25)
delay_print2("the deputy director——walks in.")
time.sleep(0.25)
delay_print2("walks in.")
time.sleep(0.5)
delay_print2(" You don’t need to look up to know it’s him.")
time.sleep(0.3)
delay_print2("\nYou can feel his presence enter a room like a cold wind——")
time.sleep(0.3)
delay_print2("tailored coat, ")
time.sleep(0.3)
delay_print2(" shiny shoes, ")
time.sleep(0.3)
delay_print2("that stupid face carved out of arrogance and expensive aftershave.")
time.sleep(1)
delay_print2("\nThe capricious lady that is your brain——")
time.sleep(0.3)
delay_print1(italic_text("(Lady? "))
time.sleep(0.3)
delay_print1(italic_text("No, "))
time.sleep(0.3)
delay_print1(italic_text("don’t question your brain,)——"))
time.sleep(0.5)
delay_print2("decides you hate paperwork, ")
time.sleep(0.2)
delay_print2(" and ")
time.sleep(0.075)
delay_print1(italic_text("that's"))
time.sleep(0.1)
delay_print2(" how you know.")
print("\n")

time.sleep(1.6)
delay_print2("You look down at yourself")
time.sleep(0.3)
delay_print2("creased shirt, ")
time.sleep(0.3)
delay_print2("pen ink already smudged on your sleeve.")
time.sleep(0.5)
delay_print2("\nThey say dress for the job you want,")
time.sleep(0.4)
delay_print2(" You’re dressed like the job is already over.")
time.sleep(1.4)
print("\n")

delay_print2("You can feel his eyes on you, ")
time.sleep(0.3)
delay_print2("sharp and unrelenting, ")
time.sleep(0.3)
delay_print2("piercing through the back of your head.")
time.sleep(0.5)
delay_print2("\nIt doesn’t help that every time you glance in his direction, ")
time.sleep(0.3)
delay_print2("he’s watching,")
time.sleep(0.4)
delay_print2(" waiting for you to screw up.")
time.sleep(0.8)
delay_print2("\nYou almost wonder if this is how everyone feels about you.")
time.sleep(2)
print("\n")

delay_print2("You don’t see it, but you know.")
time.sleep(0.5)
delay_print2(" Something changes in his breathing.")
time.sleep(0.3)
delay_print2("\nHe’s going to do something, ")
time.sleep(0.3)
delay_print2("because he thinks he’s better than you.")
time.sleep(0.5)
delay_print2(" It's a pattern.")
time.sleep(1)
delay_print2("\nAnd you know,")
time.sleep(0.3)
delay_print2(" but you won't try to stop it.")
time.sleep(0.5)
delay_print2(" Not because you’re powerless.")
time.sleep(0.3)
delay_print2("\nBut because it’s a spinning, spinning wheel,") 
time.sleep(0.3)
delay_print2(" of the same and the same and the same and the——")
time.sleep(0.1)
delay_print2("\nYou get it.")
time.sleep(2)
print("\n")

delay_print2("Everywhere you’ll find more of the same.")
time.sleep(0.5)
delay_print2(" Hollow suits.")
time.sleep(0.3)
delay_print2("\nThey think they have you all figured out don’t they?")
time.sleep(0.5)
delay_print2(" Aren’t you a lost lamb Graham?")
time.sleep(3)
print("\n")

choices = [
    "I'M MORE VILE THAN YOU THINK",
    "NONE OF THIS MATTERS"
]
selected = select(choices)

if selected == 0:  # I'M MORE VILE...
    if game_state["Late"] == True:
       game_state["GrahamAnger"] += 2
    else:
        game_state["GrahamAnger"] += 1
    
    delay_print2("You’d bite too. ")
    time.sleep(0.5)
    delay_print2("You don’t blow off steam on random interns——")
    time.sleep(0.3)
    delay_print2("and that's what makes you worse.")
    time.sleep(.5)

    delay_print2("\nYou’re mold in drywall, hiding behind thin wallpaper. ")
    time.sleep(.8)
    delay_print2("He doesn’t know what he’s poking.")
    delay_print("\n...")
    time.sleep(.4)
    print("\n")

    delay_print2("God, you need a hobby.")
    time.sleep(3)
  


elif selected == 1:  # NONE OF THIS MATTERS
    game_state["GrahamAnger"] -= 1

    delay_print2("You exist.")
    time.sleep(0.4)
    delay_print2(" He talks.")
    time.sleep(0.4)
    delay_print2(" He jeers.")
    time.sleep(0.4)
    delay_print2(" The world still spins.")
    time.sleep(.7)
    delay_print2("\nYou’re not sure you’re even angry anymore.")
    time.sleep(0.5)
    delay_print2(" He’s a product of many other actors and actions.")
    time.sleep(.5)
    delay_print2(" A predictable line.")
    time.sleep(.3)
    delay_print2("\nHe was hurt, ")
    time.sleep(0.2)
    delay_print2("so now he’ll hurt.")
    time.sleep(.5)
    delay_print("\n...")
    time.sleep(1)
    delay_print2("\nMaybe you’ve been reading too much Camus.")
    time.sleep(3)
   
clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()

# I'll figure out if i want to use this later
# def grahmangry():
#     delay_print2("Oh ")
#     time.sleep(.5)
#     delay_print2("my ")
#     time.sleep(.4)
#     delay_print2("gosh.\n")
#     time.sleep(.5)
#     delay_print2("He thinks he knows you. ")
#     time.sleep(.3)
#     delay_print2("Got you figured out, dancing in his palm?\n")
#     time.sleep(.3)
#     delay_print2("You could scream right now! ")
#     time.sleep(.3)
#     delay_print2("You could throw a chair! ")
#     time.sleep(.3)
#     delay_print2("You would do it!\n\n")
#     time.slee(.9)
#     delay_print2("But not right now,")
#     time.sleep(.3)
#     delay_print2("let him think he's special, like he's more than a trope you've seen over and over.\n")
#     time.sleep(.8)
#     delay_print2("If you do get the opportunity, something ")
#     delay_print2(italic_text("will "))
#     delay_print2("happen.")
#     time.sleep(.5)
#     delay_print2("It's really just karma at that point, no?")


if game_state["Office_Remark"] == True:
    game_state["GrahamAnger"] += 1

    delay_print2("The boss man taps his fingers on the desk.")
    time.sleep(0.5)
    delay_print2(" You’re almost more interested in the way his fingers probably leave imperceptible smudges on the table than you are in what he’s about to say.\n\n")
    time.sleep(.5)
    delay_print2(italic_text('\n"How long do you think you’ll last here before you completely screw up, '))
    time.sleep(0.1)
    delay_print2(italic_text('rookie?"'))
    time.sleep(1)
    print("\n")

    delay_print2("You don’t intend to ignore it——")
    time.sleep(0.3)
    delay_print2("not at first.")
    time.sleep(.5)
    delay_print2(" You really were just awfully entrenched in thinking about table smudges.")
    time.sleep(.5)
    delay_print2("\nBut when it does register, ")
    time.sleep(.3)
    delay_print2(" you don’t lament yourself for staying silent.")
    time.sleep(.5)
    delay_print2(" No, ")
    delay_print2(italic_text("‘good’"))
    delay_print2(", you think.")
    time.sleep(.5)
    delay_print2(" Let him talk.")
    time.sleep(0.5)
    delay_print2(" Let his voice echo off the walls.")
    time.sleep(4)
   


elif game_state["Office_Silent"] == True:

    game_state["GrahamAnger"] -= 1
    delay_print2("Oh.")
    time.sleep(.8)
    delay_print2("\nHe just stays silent.")
    time.sleep(.3)
    delay_print("\n...")
    time.sleep(.5)

    delay_print2("\nThank god!")
    time.sleep(.5)
    print("\n")

    delay_print2("He’s still staring at you,")
    time.sleep(.3)
    delay_print2(" but one less sensory issue to worry about is bliss to your overfunctioning brain.")
    time.sleep(.5)
    delay_print2("\nIf he wants to be a ghost and haunt the room,")
    time.sleep(.3)
    delay_print2(" let him.")
    time.sleep(1)
    delay_print2("\nMaybe if you will it enough, ")
    time.sleep(0.2)
    delay_print2("he’ll be like this all the time!")
    time.sleep(3)
    

        
elif game_state["Office_CallOut"] == True:
    game_state["GrahamAnger"] += 1

    delay_print2("When you observe the way someone’s face twitches before they speak, ") 
    time.sleep(.4)
    delay_print2 ("that’s usually when you can decide if you’ll like what they say or not.")
    time.sleep(.5)
    delay_print2("\nIn the case of the boss man, ")
    delay_print2("you decide before his brain even formulates what he’s going to say.")
    print("\n")
    time.sleep(.8)

    delay_print2(italic_text('\n"Not even trying today, '))
    time.sleep(0.1)
    delay_print2(italic_text('huh? '))
    time.sleep(0.3)
    delay_print2(italic_text('At least pretend to look like you’re being productive."'))
    time.sleep(0.5)
    print("\n")

    delay_print2("You preemptively frowned for this,")
    time.sleep(.5)
    delay_print2(" and lo and behold you were right in doing so.")
    time.sleep(.8)
    delay_print2("\nAnyhow, it does remind you that you’d much rather be doing something less mentally taxing——")
    time.sleep(.3)
    delay_print2("like the aforementioned paperwork.")
    time.sleep(.8)
    delay_print2("\nEven if it does make it look like you’re hurrying away because of him.")
    time.sleep(3)

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()




# -----------------------------------------------------------------------------  

        

#Scene 2: The Briefing Room
#Graham's POV
clear()
time.sleep(1)
print(povs["graham_pov"])
delay_print1(italic_text("Meeting Room——National Incident Intelligence Agency, Prague, May 12, 1997"))
time.sleep(1)
print("\n")

delay_print2("The fluorescent lights hum overhead, ")
time.sleep(0.3)
delay_print2("casting a sterile glow over the room.")
time.sleep(0.6)
delay_print2(" You sit at a long table, ")
time.sleep(0.3)
delay_print2("cluttered with files and paperwork.")
time.sleep(0.8)
delay_print2(" Across the table, ")
time.sleep(0.3)
delay_print2("Grayson lounges like he owns the place——")
time.sleep(0.4)
delay_print2("which he sort of does.")
time.sleep(1)
print("\n")

delay_print2("He’s flipping through a thin manila folder like it personally offended him.")
time.sleep(1)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(tapping the folder)\n"))
delay_print2("“Rural disturbance report.")
time.sleep(0.4)
delay_print2(" Three dead.")
time.sleep(0.4)
delay_print2(" One survivor.")
time.sleep(0.4)
delay_print2(" All official accounts redacted.")
time.sleep(0.7)
delay_print2(" Ain't that just great?”")
time.sleep(1.5)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(dryly)\n"))
delay_print2("“I thought redacting things was your department.”")
time.sleep(1)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(glancing up, unimpressed)\n"))
delay_print2("“I’m flattered.")
time.sleep(0.3)
delay_print2(" But this one’s above even me.")
time.sleep(1)
delay_print2(" No names,")
time.sleep(0.3)
delay_print2(" no clear timestamp.")
time.sleep(0.6)
delay_print2(" Just one line flagged in red——")
time.sleep(0.5)
delay_print2("Containment breach suspected.”")
time.sleep(2)
print("\n")

print(speak["graham_speak"])
delay_print2("“Suspected what?")
time.sleep(0.3)
delay_print2(" Disease?”")
time.sleep(1)
print("\n")

print("Grayson doesn’t smile this time.")
time.sleep(0.5)
delay_print2("He tosses the folder across to you.")
time.sleep(1)
print("\n")

print(speak["grayson_speak"])
delay_print2("“Whatever it is, it’s not your everyday case of food poisoning.")
time.sleep(0.6)
delay_print2(" Read the medical note on the last page.”")
time.sleep(1.5)
print("\n")

delay_print2("You flip it open.")
time.sleep(0.4)
delay_print2(" Notes scrawled in black ink:")
time.sleep(1)
print("\n")


delay_print2(italic_text("“Unresponsive to sedatives.”"))
time.sleep(0.3)
delay_print2(italic_text(" Reanimated minutes after death."))
time.sleep(0.4)
delay_print2(italic_text(" Aggression level extreme."))
time.sleep(0.3)
delay_print2(italic_text(" Protocol failsafe triggered——"))
time.sleep(0.4)
delay_print2(italic_text("containment "))
delay_print2(italic_text(bold_text(" unsuccessful.”")))
time.sleep(2)
print("\n")

delay_print2("You freeze.")
time.sleep(0.4)
delay_print2(" Slowly, you lower the folder.")
time.sleep(1)
print("\n")

print(speak["graham_speak"])
delay_print2("Your first instinct is: ")
time.sleep(0.2)
delay_print2("“This is fake.”")
time.sleep(1)
print("\n")

print(speak["grayson_speak"])
delay_print2("“Sure.")
time.sleep(0.4)
delay_print2(" Just like every conspiracy we ignore——")
time.sleep(0.5)
delay_print2("until it rips through the city.”")
time.sleep(1.5)
print("\n")

delay_print2("A moment of silence stretches between you both, thick with unspoken tension.")
time.sleep(1)
print("\n")

print(speak["grayson_speak"])
delay_print2("“They’re sending us.")
time.sleep(0.4)
delay_print2(" You ")
time.sleep(0.1)
delay_print2("and me.”")
time.sleep(1)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(scoffing)\n"))
delay_print2("“Together?”")
time.sleep(1)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(tone sharpening slightly)\n"))
delay_print2("“Yeah, together.")
time.sleep(0.4)
delay_print2(" I know, ")
time.sleep(0.3)
delay_print2("it’s so hard to believe they’d send their Deputy Director with a junior analyst instead of——")
time.sleep(0.3)
delay_print2("I don’t know, a fully trained operative.”")
time.sleep(1.5)
print("\n")

delay_print2("“Higher-ups think pairing up a pretty analyst with a dangerous bastard is good optics.")
time.sleep(0.6)
delay_print2(" We’re leaving for Southern Bohemia——")
time.sleep(0.2)
delay_print2("4:00pm, don’t be late.”")
time.sleep(2)
print("\n")


delay_print2("You want to argue.")
time.sleep(0.4)
delay_print2(" Or maybe laugh.")
time.sleep(0.4)
delay_print2(" Or question the pretty part.")
time.sleep(0.4)
delay_print2(" Can you file a workplace harassment complaint for that?")
time.sleep(0.6)
delay_print2("\nBut the word ")
time.sleep(0.1)
delay_print2(italic_text("reanimated"))
time.sleep(0.1)
delay_print2(" is still buzzing in your head like a warning siren.")
time.sleep(1.5)
print("\n")

delay_print2("You close the file.")
time.sleep(3)
print("\n")

choices = [
    "SARCASM",
    "CHALLENGE",
    "SERIOUS"
]
selected = select(choices)

# Handle the player's choice
if selected == 0:  # SARCASM
    game_state["GraysonAnger"] += 1
    print(speak["graham_speak"])
    delay_print2("“Oh lovely.")
    time.sleep(0.4)
    delay_print2(" Do I get to carry your cigarettes too, ")
    time.sleep(0.2)
    delay_print2("or is that above my clearance level?”")
    time.sleep(1)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2(italic_text("(sharply)\n"))
    delay_print2("“Careful, rookie.")
    time.sleep(0.4)
    delay_print2(" Keep talking like that and I’ll start thinking you enjoy this little dynamic we have.”")
    time.sleep(1.5)
    print("\n")

    delay_print2("He leans back with a smug look, ")
    time.sleep(0.3)
    delay_print2("but there’s a flash of something tighter in his jaw—-")
    time.sleep(0.4)
    delay_print2("he didn’t love the tone.")
    time.sleep(0.7)
    delay_print2(" (You want to roll your eyes at that.)")
    time.sleep(0.4)
    delay_print2(" Still, he recovers quick.")
    time.sleep(1)
    print("\n")

    delay_print2('“Besides, if you’re going to carry something, make it your weight.”')
    time.sleep(3)

elif selected == 1:  # CHALLENGE HIM
    game_state["GraysonAnger"] += 2
    game_state["GrahamAnger"] += 1

    delay_print2("Really, ")
    time.sleep(0.2)
    delay_print2(italic_text("this"))
    time.sleep(0.1)
    delay_print2(" is out of your pay grade. ")
    time.sleep(0.5)
    delay_print2("Maybe you’re just there to babysit? ")
    time.sleep(0.5)
    delay_print2("You’re inclined to entertain that thought with a snicker.")
    time.sleep(0.7)

    delay_print2('\n“If you’re so good at this, ')
    time.sleep(0.2)
    delay_print2('how come they stuck you with "someone" ')
    time.sleep(0.1)
    delay_print2('like me? ')
    time.sleep(0.4)
    delay_print2('Doesn’t sound like a vote of confidence.”')
    time.sleep(1)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2(italic_text("(pauses, jaw tensing)\n"))
    delay_print2('“They didn’t stick me with you, rookie.')
    time.sleep(0.4)
    delay_print2(italic_text("\n(leans in)"))
    delay_print2('\nThey stuck you with me. ')
    time.sleep(0.3)
    delay_print2('There’s a difference. ')
    time.sleep(0.3)
    delay_print2('And the only vote of confidence you need is whether I let you keep slowing me down.”')
    time.sleep(1.5)
    print("\n")

    print(speak["graham_speak"])
    delay_print2("...")
    time.sleep(0.5)
    delay_print2("\nPrick.")
    time.sleep(3)

elif selected == 2:  # GET SERIOUS
    print(speak["graham_speak"])
    delay_print2("“Reanimated?!")
    time.sleep(0.3)
    delay_print2(" Seriously, what does that even mean?!")
    time.sleep(0.5)
    delay_print2(" If this is real, ")
    time.sleep(0.3)
    delay_print2("we're going to need a lot more than just two people and a folder of redacted crap.”")
    time.sleep(1)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2("“Welcome to the party.")
    time.sleep(0.4)
    delay_print2(" That’s what I’ve been saying——")
    time.sleep(0.5)
    delay_print2("no backup, ")
    time.sleep(0.2)
    delay_print2("no prep, ")
    time.sleep(0.2)
    delay_print2("just us and whatever this is.”\n")
    time.sleep(0.4)
    delay_print2(italic_text("(leans forward, voice low)\n"))
    delay_print2("“So unless you’ve got a plan hidden in that clipboard,")
    time.sleep(0.4)
    delay_print2(" get your head on straight.")
    time.sleep(0.4)
    delay_print2(" We move in four hours.”")
    time.sleep(3)

delay_print2("The room falls quiet again.")
time.sleep(0.5)
delay_print2(" Outside, the clouds darken.")
time.sleep(0.5)
delay_print2(" The day feels heavier than it should.")
time.sleep(2)

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()




# -----------------------------------------------------------------------------



# Scene 3A: The Departure
# [POV SWITCH - Grayson’s POV]

print(povs["grayson_pov"])
delay_print1(italic_text("Exterior——Ministry of Interior, Prague, May 12, 1997"))
time.sleep(1.2)
print("\n")

delay_print2("The air’s thick with anticipation as you stand outside the Ministry’s front doors, ")
time.sleep(0.1)
delay_print2("waiting for Graham.")
time.sleep(1)
delay_print2("\nYour watch reads 3:50pm——")
time.sleep(0.2)
delay_print2("ten minutes before you’re supposed to be on the move.")
time.sleep(0.9)
delay_print2(" You’d rather be anywhere else, ")
time.sleep(0.2)
delay_print2("but duty calls.")
time.sleep(1.3)
print("\n")

delay_print2("You glance at your watch again, ")
time.sleep(0.3)
delay_print2("and sure enough, ")
time.sleep(0.2)
delay_print2("Graham rounds the corner——")
time.sleep(0.4)
delay_print2("he walks like his limbs aren’t sure what order to move in.")
time.sleep(0.7)
delay_print2(" Bag slung too low, ")
time.sleep(0.2)
delay_print2(" hair trying and failing to lie flat.")
time.sleep(0.6)
delay_print2("\nStill, ")
time.sleep(0.2)
delay_print2("he cleaned up.")
time.sleep(0.6)
delay_print2(" No bloodshot eyes, ")
time.sleep(0.2)
delay_print2("no wrinkled shirt.")
time.sleep(0.6)
delay_print2(" Improvement.")
time.sleep(1.2)
print("\n")

delay_print2("At least Graham seems to have gotten the hint.")
time.sleep(0.5)
delay_print2(" His appearance isn’t a ")
time.sleep(0.05)
delay_print2("total ")
time.sleep(0.1)
delay_print2("disaster.")
time.sleep(0.4)
delay_print2(" Well, ")
time.sleep(0.1)
delay_print2("for a rookie.")
time.sleep(0.7)
delay_print2(" His posture’s still stiff, his expression still annoyed,")
time.sleep(0.5)
delay_print2(" but there’s something that feels… right about his silence.")
time.sleep(0.7)
delay_print2(" Maybe he’s finally realized this is real.")
time.sleep(1.2)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(mockingly)\n"))
delay_print2("“About time, rookie. ")
time.sleep(0.2)
delay_print2("I was starting to think I’d have to go without you.”")
time.sleep(1.3)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(grimaces, walking up to you)\n"))
delay_print2("“Didn’t realise we were in such a hurry. ")
time.sleep(0.2)
delay_print2("I was busy packing.”")
time.sleep(1)
print("\n")

delay_print2("You tilt your head slightly, narrowing your eyes.")
time.sleep(0.5)
print("\n")

print(speak["grayson_speak"])
delay_print2("“Packing? ")
time.sleep(0.2)
delay_print2("For what, ")
time.sleep(0.1)
delay_print2("a vacation?”")
time.sleep(0.5)
delay_print2(italic_text(" (You wave a hand dismissively)\n"))
delay_print2("“Forget it. ")
time.sleep(0.2)
delay_print2("Let’s get this over with.”")
time.sleep(1.5)
print("\n")

delay_print2("Graham hesitates, probably caught between wanting to argue")
time.sleep(0.2)
delay_print2(" and realizing it's useless.")
time.sleep(0.6)
delay_print2(" Good.")
time.sleep(0.5)
delay_print2(" You’ve been in the business long enough to know that hesitation gets people killed.")
time.sleep(1.5)
print("\n")

delay_print2("You start walking,")
time.sleep(0.3)
delay_print2(" and after a moment, ")
time.sleep(0.2)
delay_print2("he falls in line behind you.")
time.sleep(1)
print("\n")

delay_print2("As you make your way to the vehicle, the weight of the file you’d been handed earlier presses on your mind.")
time.sleep(0.8)
delay_print2("\nReanimated.")
time.sleep(0.8)
delay_print2(" Could be some sort of freak case.")
time.sleep(0.5)
delay_print2("\nBut with the way things are escalating,")
time.sleep(0.4)
delay_print2(" you’ve learned better than to take things at face value.")
time.sleep(1.8)
print("\n")

delay_print2("You’re surprised when Graham speaks up, voice low, almost reluctant.")
time.sleep(1)
print("\n")

print(speak["graham_speak"])
delay_print2("“Do you really think it’s… real?")
time.sleep(0.3)
delay_print2("What’s in that report?”")
time.sleep(1.3)
print("\n")

delay_print2("You don’t look back at him,")
time.sleep(0.6)
delay_print2(" but you can feel his eyes boring into your back.")
time.sleep(3)
print("\n") 

# Player Choice - How do you respond?
choices = [
    "DISMISSIVE",
    "TRUTH",
    "SARCASM"
]
selected = select(choices)

if selected == 0:  # DISMISSIVE
    print(speak["grayson_speak"])
    delay_print2("“Doesn’t matter what I think.")
    time.sleep(0.8)
    delay_print2(" Orders are orders.")
    time.sleep(0.7)
    delay_print2(" You can burn energy on ‘what ifs’ all you want,")
    time.sleep(0.8)
    delay_print2(" but we’ve got a van full of gear, an address, and a deadline.”")
    time.sleep(1.5)
    print("\n")

    delay_print2("Your tone is flat, dry——like you’ve had this conversation a hundred times before")
    time.sleep(0.4)
    delay_print2(" with people who didn’t make it to the next one.")
    print("\n")
    time.sleep(1.3)

    print(speak["grayson_speak"])
    delay_print2("“Start asking the wrong questions,")
    time.sleep(0.5)
    delay_print2(" and you’ll miss what’s right in front of you.")
    time.sleep(0.7)
    delay_print2(" And out there?”\n")
    delay_print2(italic_text(" (You jerk your chin forwards, towards the edges of the city where everything turns to forest and fog)\n"))
    delay_print2("“That kind of distraction gets people killed.”")
    time.sleep(1.6)
    print("\n")

    delay_print2("Graham doesn’t respond.")
    time.sleep(0.6)
    delay_print2(" Not out loud.")
    time.sleep(0.6)
    delay_print2(" But the silence that follows is heavier now.")
    time.sleep(1.2)
    print("\n")

elif selected == 1:  # HARSH TRUTH
    print(speak["grayson_speak"])
    delay_print2("“Do I think it’s real?")
    time.sleep(0.7)
    delay_print2(" What, like you want me to answer in comforting lies?")
    time.sleep(0.8)
    delay_print2(" Or should I hit you with the cold, hard truth?”")
    print("\n")
    time.sleep(1.5)

    delay_print2("Graham doesn’t respond immediately,")
    time.sleep(0.6)
    delay_print2(" and you can hear him swallowing back whatever he was going to say.")
    time.sleep(0.9)
    delay_print2(" He’s thinking too much.")
    time.sleep(0.6)
    delay_print2(" That’s his problem.")
    time.sleep(1.2)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2(italic_text("(still moving towards the car)\n"))
    delay_print2("“I’ll tell you what you need to know.")
    time.sleep(0.7)
    delay_print2(" Focus on surviving.")
    time.sleep(0.6)
    delay_print2("\nWhatever this is, we’re walking straight into it——")
    time.sleep(0.6)
    delay_print2("whether it’s a bad batch of food or something worse.")
    time.sleep(0.7)
    delay_print2("\nI’m not here to give you a happy ending.”")
    print("\n")
    time.sleep(1.7)

elif selected == 2:  # SARCASM
    print(speak["grayson_speak"])
    delay_print2(italic_text("(chuckles dryly)\n"))
    delay_print2("“Real enough that they’re sending us instead of the usual clean-up crew.")
    time.sleep(0.9)
    delay_print2("\nSo either it’s a freak accident with a body count, or….”")
    print("\n")
    time.sleep(1.1)

    delay_print2(italic_text("(You gesture vaguely toward the horizon)\n"))
    delay_print2("“…we’re walking into something they don’t want to name out loud.")
    time.sleep(0.9)
    delay_print2(" Which frankly, is my favourite kind of problem.”")
    time.sleep(1.4)
    print("\n")

    delay_print2("You glance at Graham, smirking.")
    print("\n")
    time.sleep(1)

    print(speak["grayson_speak"])
    delay_print2("“Cheer up.")
    time.sleep(0.6)
    delay_print2("\nWorst case, we die horribly,")
    time.sleep(0.7)
    delay_print2(" and someone else has to do our paperwork.”")
    print("\n")
    time.sleep(1.5)

# Continue Scene
delay_print2("You reach the car——the doors are unlocked, and you climb in without another word.")
print("\n")
time.sleep(1.3)

delay_print2("Graham follows you, his hesitation lingering for a second before he slides into the passenger seat...")
time.sleep(0.9)
delay_print2(" clearly uncomfortable with the tension that settles between you.")
print("\n")
time.sleep(1.5)

delay_print2("The engine hums to life, and you glance over at him.")
time.sleep(0.7)
delay_print2(" He’s pale, his grip tight on the seatbelt as he stares out the window...")
time.sleep(0.9)
delay_print2(" a thousand thoughts whirling behind his eyes.")
print("\n")
time.sleep(1.5)

print(speak["grayson_speak"])
delay_print2(italic_text("(muttering to yourself)\n"))
delay_print2("“You’ve got the luxury of second-guessing everything, rookie.")
time.sleep(0.9)
delay_print2(" Not everyone’s so lucky.”")
print("\n")
time.sleep(1.6)

delay_print2("There’s a long pause before Graham speaks again...")
time.sleep(1.1)
delay_print2(" quieter this time.")
print("\n")
time.sleep(1)

print(speak["graham_speak"])
delay_print2("“Are you ever going to tell me what this is all about?”")
print("\n")
time.sleep(1.2)

delay_print2("You don’t look at him...")
time.sleep(0.6)
delay_print2(" but you smirk to yourself.")
print("\n")
time.sleep(1.3)

print(speak["grayson_speak"])
delay_print2("“Maybe you’ll find out.")
time.sleep(0.7)
delay_print2(" But for now, focus on the task at hand.”")
print("\n")
time.sleep(1.5)

delay_print2("The car speeds towards the edge of the city, ")
time.sleep(0.3)
delay_print2(" where the unknown waits.")
print("\n")
time.sleep(2)

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()



# -----------------------------------------------------------------------------

# Scene 3B: En Route
# [POV SWITCH - Graham’s POV]

print(povs["graham_pov"])
delay_print1(italic_text("Interior——Agency Vehicle, En Route to Site 14, May 12, 1997"))
time.sleep(1)
print("\n")

delay_print2("The roads blur past like an old film reel——")
time.sleep(0.3)
delay_print2("washed-out greys, ")
time.sleep(0.3)
delay_print2("rusting fences, ")
time.sleep(0.3)
delay_print2("wilted countryside. \n")
time.sleep(0.5)
delay_print2("You’re quiet, ")
time.sleep(0.3)
delay_print2("watching buildings shrink behind you in the mirror, ")
time.sleep(0.3)
delay_print2("the city exhaling its last breath.\n ")
time.sleep(0.5)
delay_print2("At about this time, ")
time.sleep(0.3)
delay_print2("the convenience store clerk you see the most would be clocking out. ")
time.sleep(0.5)
delay_print2("Good for him.")
time.sleep(1)
print("\n")

delay_print2("Grayson sits across from you, ")
time.sleep(0.3)
delay_print2("thumbing through another folder. ")
time.sleep(0.5)
delay_print2("His legs are crossed like he’s in a lounge, ")
time.sleep(0.3)
delay_print2("not a state vehicle headed toward something deeply classified, ")
time.sleep(0.3)
delay_print2("and possibly horrifying. ")
time.sleep(0.5)
delay_print2("The man’s made of nerves, ")
time.sleep(0.3)
delay_print2("and nicotine.")
time.sleep(1)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(reading aloud, vaguely bored)\n"))
delay_print2("“Subject One: Male, mid-thirties. ")
time.sleep(0.3)
delay_print2("Presented with fever, ")
time.sleep(0.3)
delay_print2("incoherence, ")
time.sleep(0.3)
delay_print2("and——oh, this is a nice touch——")
time.sleep(0.3)
delay_print2("extreme biting compulsion.”\n")
time.sleep(0.5)
delay_print2(italic_text("(he raises a brow)\n"))
delay_print2("“Sounds like half the people I’ve dated.”")
time.sleep(1.5)
print("\n")

delay_print2("You don’t laugh. ")
time.sleep(0.3)
delay_print2("You don’t speak. ")
time.sleep(0.5)
delay_print2("You’re thinking about your other neighbour who got bit by a raccoon once. ")
time.sleep(0.5)
delay_print2("He was pretty much okay, ")
time.sleep(0.3)
delay_print2("but then again, ")
time.sleep(0.3)
delay_print2("he was 300 pounds of muscle, ")
time.sleep(0.3)
delay_print2("and you’d be dealing with biting people, ")
time.sleep(0.1)
delay_print2("so maybe it’s different.")
time.sleep(1.5)
print("\n")

delay_print2("You keep staring at the countryside as it decays into industrial gloom. ")
time.sleep(0.5)
delay_print2("The silence stretches.")
time.sleep(3)
print("\n")

# Player Choice - What do you do?
choices = [
    "WHY YOU WERE CHOSEN",
    "QUESTION INTEL",
    "STAY SILENT"
]
selected = select(choices)

if selected == 0:  # ASK WHY YOU WERE CHOSEN
    print(speak["graham_speak"])
    delay_print2("“You never answered earlier. ")
    time.sleep(0.3)
    delay_print2("Why me?”")
    time.sleep(1)
    print("\n")

    delay_print2("Grayson doesn’t look up at first. ")
    time.sleep(0.3)
    delay_print2("When he does, ")
    time.sleep(0.3)
    delay_print2("there’s something like annoyance on his face——")
    time.sleep(0.3)
    delay_print2("but buried deep, ")
    time.sleep(0.3)
    delay_print2("buried under layers of something harder to name.")
    time.sleep(1.5)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2("“Because someone up there thinks you’re smarter than you look.”\n")
    time.sleep(0.5)
    delay_print2(italic_text("(pauses)\n"))
    delay_print2("“Or expendable. ")
    time.sleep(0.3)
    delay_print2("Maybe both.”")
    time.sleep(1.5)
    print("\n")

    print(speak["graham_speak"])
    delay_print2("“Huh…. ")
    time.sleep(0.3)
    delay_print2("Reassuring.”")
    time.sleep(1)
    print("\n")

    delay_print2("Somehow this seems to be the dichotomy you’ve been stuck with your whole life.")
    time.sleep(1)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2(italic_text("(shrugs)\n"))
    delay_print2("“You wanted honesty.”")
    time.sleep(3)
    print("\n")

elif selected == 1:  # QUESTION THE INTEL
    print(speak["graham_speak"])
    delay_print2("“This file’s a mess. ")
    time.sleep(0.3)
    delay_print2("No video, ")
    time.sleep(0.3)
    delay_print2("no timestamps, ")
    time.sleep(0.3)
    delay_print2("just second-hand quotes. ")
    time.sleep(0.3)
    delay_print2("This is a joke.”")
    time.sleep(1)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2("“Then laugh.”")
    time.sleep(1)
    print("\n")

    print(speak["graham_speak"])
    delay_print2("“I'm serious. ")
    time.sleep(0.3)
    delay_print2("There's nothing verifiable. ")
    time.sleep(0.3)
    delay_print2("We’re going in blind.”")
    time.sleep(1.5)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2("“You think I don’t know that? ")
    time.sleep(0.3)
    delay_print2("You think I’d be here if this was anything else?”")
    time.sleep(1.5)
    print("\n")

    delay_print2("He shuts the folder, ")
    time.sleep(0.3)
    delay_print2("more forceful than necessary. ")
    time.sleep(0.5)
    delay_print2("It sits between you like an unexploded grenade.")
    time.sleep(3)
    print("\n")

    game_state["GraysonAnger"] += 1

elif selected == 2:  # STAY SILENT
    delay_print2("The folder stays open, ")
    time.sleep(0.3)
    delay_print2("but neither of you read it anymore. ")
    time.sleep(0.5)
    delay_print2("The silence grows heavy, ")
    time.sleep(0.3)
    delay_print2("oppressive.")
    time.sleep(1.5)
    print("\n")

    delay_print2("The engine hums, ")
    time.sleep(0.3)
    delay_print2("and the smell of leather, ")
    time.sleep(0.3)
    delay_print2("old smoke, ")
    time.sleep(0.3)
    delay_print2("and sterile polish fills your lungs.")
    time.sleep(1.5)
    print("\n")

    delay_print2("Grayson finally breaks it.")
    time.sleep(1)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2("“Whatever’s at Site 14, ")
    time.sleep(0.3)
    delay_print2("it’s not just paperwork. ")
    time.sleep(0.5)
    delay_print2("So get your head on, ")
    time.sleep(0.3)
    delay_print2("Svoboda.”")
    time.sleep(1.5)
    print("\n")

    delay_print2("Your name sounds foreign in his mouth. ")
    time.sleep(0.5)
    delay_print2("You don’t respond. ")
    time.sleep(0.3)
    delay_print2("Hah. ")
    time.sleep(0.3)
    delay_print2("You really are petty.")
    time.sleep(3.5)
    print("\n")

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()

# -----------------------------------------------------------------------------

# SCENE 4: Site 14
# [POV SWITCH - Grayson’s POV]
clear()
time.sleep(1)
print(povs["grayson_pov"])
delay_print1(italic_text("Site 14, Edge of the Forest, Southern Bohemia, May 12, 1997"))
time.sleep(2)   
print("\n")

delay_print2("The vehicle stops just off a gravel path."), time.sleep(0.4)
delay_print2(" Woods stretch around the compound like a noose."), time.sleep(0.4)
delay_print2(" Barbed fences twist between trees."), time.sleep(0.6)
delay_print2(" You’ve seen plenty of bleak crap in your time——but this place?"), time.sleep(0.6)
delay_print2(" This place feels off.")
time.sleep(2)
print("\n")

delay_print2("No birds."), time.sleep(0.4)
delay_print2(" No insects."), time.sleep(0.4)
delay_print2(" Just the wind and the creak of an unguarded gate.")
time.sleep(1)
print("\n")

print(speak["graham_speak"])
delay_print2("“Doesn’t look very…contained.”")
print("\n")
time.sleep(1.5)

delay_print2("You flick your lighter open and closed, once, twice."), time.sleep(0.4)
delay_print2(" Not because you need it——")
delay_print2("but because it’s the only sound you trust right now.")
print("\n")
time.sleep(2)

delay_print2("Your sidearm weighs heavy at your hip."), time.sleep(0.4)
delay_print2(" You check it without looking——just a brief palm press to make sure it’s still there, chambered and ready."), time.sleep(0.8)
delay_print2(" Graham noticed."), time.sleep(0.4)
delay_print2(" His hand flinches toward his own holster, uncertain.")
time.sleep(1.5)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(low voice)\n"))
delay_print2("“Stay close."), time.sleep(0.4)
delay_print2(" And if you see anything moving——don’t freeze."), time.sleep(0.4)
delay_print2(" Don't ask questions."), time.sleep(0.4)
delay_print2(" Just put it down.”")
time.sleep(2)
print("\n")

delay_print2("He tenses slightly at that,"), time.sleep(0.4)
delay_print2(" You can tell."), time.sleep(0.4)
delay_print2(" He’s not used to guns——not used to you.")
time.sleep(2)
print("\n")

delay_print2("That makes two of you.")
time.sleep(2)
print("\n")

delay_print2("The trees part to reveal the edge of a courtyard."), time.sleep(0.4)
delay_print2(" Dried blood stains the concrete."), time.sleep(0.4)
delay_print2(" The silence presses against your skin like a too-tight suit.")
time.sleep(2)
print("\n")

delay_print2("You look back once at Graham."), time.sleep(0.4)
delay_print2(" He’s trying to mask it, but you see it——his pulse ticking fast,"), time.sleep(0.4)
delay_print2(" his hand flexing at his side like it’s grasping for something that isn’t there.")
time.sleep(2)
print("\n")

print(speak["grayson_speak"])
delay_print2("“Too late to run now, isn’t it?”")
time.sleep(4)
print("\n")
clear()
time.sleep(3)

clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()


# -----------------------------------------------------------------------------

# SCENE 5A:
# [POV SWITCH - Graham’s POV]
print(povs["graham_pov"])
delay_print2("There’s a heavy turning in your stomach,"), time.sleep(0.4)
delay_print2(" it’s a feeling more than faithless dread."), time.sleep(0.4)
delay_print2(" It's a wild beast–its claws digging into your guts and prodding."), time.sleep(0.4)
delay_print2(" It’s the dog barking and scratching at the door before an earthquake.")
time.sleep(2)
print("\n")

delay_print2("The animal of your brain has processed something before you,"), time.sleep(0.4)
delay_print2(" the civilized master, could even understand.")
time.sleep(1.5)
print("\n")

delay_print2("You must not be doing a very good job at masking your emotions.")
time.sleep(2)
print("\n")

print(speak["grayson_speak"])
delay_print2("“Great job, rookie."), time.sleep(0.4)
delay_print2(" You’re really selling the ‘cool under pressure’ act."), time.sleep(0.4)
delay_print2(" Keep it up, and they’ll make a statue out of you.”")
time.sleep(2)
print("\n")

delay_print2("You try to reign yourself in again,"), time.sleep(0.4)
delay_print2(" only to discover your dog brain has undone centuries of evolutions."), time.sleep(0.4)
delay_print2(" From its stable whining, it's now biting at you and screaming——it's a beast undone."), time.sleep(0.4)
delay_print2(" You’re going to go crazy if you don’t do something about that.")
time.sleep(2)
print("\n")

# [PLAYER CHOICE - What do you do?]
choices = [
    "MUZZLE THE DOG",
    "LET IT SPEAK"
]
selected = select(choices)

# Handle the player's choice
if selected == 0:  # MUZZLE THE DOG
    game_state["Composure"] += 1
    game_state["Instinct"] -= 1
    delay_print2("You’re not reasoning your way out of this one,"), time.sleep(0.4)
    delay_print2(" so you speak a language its primal brain understands.\n"), time.sleep(2)
    delay_print2("You grit your teeth,"), time.sleep(0.4)
    delay_print2(" and you bite your tongue so hard you feel like it might come clean off.\n"), time.sleep(0.4)
    delay_print2("The beast whimpers and shies,"), time.sleep(0.4)
    delay_print2(" and you’re fine.\n"), time.sleep(2)
    delay_print2("You. Are. Fine."), time.sleep(0.4)
    delay_print2(" You are not losing your marbles today.")
    time.sleep(2)
    print("\n")

    print(speak["graham_speak"])
    delay_print2("So you keep your feet moving, even if you do feel like hurling.\n")
    time.sleep(1.5)
    delay_print2("“I’d prefer to be a painting.”")
    time.sleep(2)
    print("\n")

    delay_print2("Your tone is dry and even and it does NOT crack."), time.sleep(0.4)
    delay_print2(" You're sure if someone was spectating they’d clap at you for your insurmountable feat of will."), time.sleep(0.4)
    delay_print2(" There’s some breath of levity at that.")
    time.sleep(3)
    print("\n")

elif selected == 1:  # LET IT SPEAK
    game_state["Composure"] -= 1
    game_state["Instinct"] += 1
    game_state["Dogbrained"] = True
    delay_print2("You stop walking."), time.sleep(0.4)
    delay_print2(" Your eyes dart around."), time.sleep(0.4)
    delay_print2(" Your nose twitches."), time.sleep(0.4)
    delay_print2(" The hair on the back of your neck stands on edge and you listen."), time.sleep(2)
    delay_print2(" Somewhere between the metallic sting of blood and the echo of silence,"), time.sleep(0.4)
    delay_print2(" you feel it.")
    time.sleep(2)
    print("\n")

    delay_print2("The air stirs around something,"), time.sleep(0.4)
    delay_print2(" about forty six centimetres in width and two meters in height."), time.sleep(0.4)
    delay_print2(" It lumbers and drags itself,"), time.sleep(0.4)
    delay_print2(" stumbling over vines and debris alike."), time.sleep(0.4)
    delay_print2(" It smells putrid.")
    time.sleep(2)
    print("\n")

    delay_print2("You’re really off your rockers now.")
    time.sleep(2)
    print("\n")

    print(speak["graham_speak"])
    delay_print2("“There’s– There’s something here with us”")
    print("\n")
    time.sleep(2)

    print(speak["grayson_speak"])
    delay_print2("He shoots you a concerned look.\n")
    time.sleep(1.5)
    delay_print2("“If something wants us dead,"), time.sleep(0.4)
    delay_print2(" it would’ve made a move already."), time.sleep(0.4)
    delay_print2(" You’re not that interesting.”")
    time.sleep(2)
    print("\n")
    delay_print(". . .")
    time.sleep(1.5)
    print("\n")
    delay_print2("You’re not sure he actually says the last part,"), time.sleep(0.4)
    delay_print2(" your heart is pounding too loud in your ears to hear him,"), time.sleep(0.4)
    delay_print2(" or anything for that matter.")
    time.sleep(3)
    print("\n")

# [BACK TO THE GENERAL PATH]


delay_print2("The more you walk, the more your head pounds,")  
time.sleep(0.8)  
delay_print2(" it’s like every step just adds another pulse under your head.")  
time.sleep(1.3)  

delay_print2("The world keeps darting in and out.\n")  
time.sleep(1.1)  
delay_print2("For a moment, it’s overwhelming,")  
time.sleep(0.7)  
delay_print2(" the clothes grating against your skin like lemon juice on raw nerve endings.\n")  
time.sleep(1.6)  

delay_print2("Then, the pendulum swings to the other side.")  
time.sleep(1.1)  
delay_print2(" You’re enveloped in the never-ending nothingness.")  
time.sleep(2.2)  
print("\n")

delay_print2("You watch someone with unkempt hair trailing through a splash of green.\n")  
time.sleep(1.3)  
delay_print2(" It looks like you.")  
time.sleep(1.1)  
delay_print2(" Even so, it stirs no familiarity.\n")  
time.sleep(1.5)  

delay_print2("You are detached,")  
time.sleep(0.7)  
delay_print2(" and formless for a moment,")  
time.sleep(0.9)  
delay_print2(" and then you’re pulled right back into the world,")  
time.sleep(1.2)  
delay_print2(" screaming and tearing at your flesh with its sensory phenomena.\n")  
time.sleep(1.8)  

delay_print2("Your existence swings back and forth like that for what feels like millennia.")  
time.sleep(1.4)  
delay_print2(" You don’t even realize it’s stopped at first.")  
print("\n")
time.sleep(2)  

delay_print2("Digging at the flesh of your arm,")  
time.sleep(0.9)  
delay_print2(" it’s only a few more minutes of trekking before you see the first signs of civilization:\n\n")  
time.sleep(2.2)  

delay_print2("A grey chain link fence.")  
time.sleep(1.1)  
delay_print2(" It's tilted way off its axis,")  
time.sleep(1.0)  
delay_print2(" and large segments of it are completely missing.\n")  
time.sleep(1.3)  
delay_print2(" It acts as a pitiful attempt of a border between the creeping undergrowth and the overgrown industrial cement.\n")  
time.sleep(1.6)  

delay_print2("Maybe at some point,")  
time.sleep(0.4)  
delay_print2(" it did a worthy job at its purpose,")  
time.sleep(1.0)  
delay_print2(" but now it’s just sad.")  
print("\n")
time.sleep(2)  

delay_print2("Grayson stops just in front of a hole in the fence,")  
time.sleep(0.9)  
delay_print2(" big enough to be easily ducked through.\n")  
time.sleep(1.2)  
delay_print2(" You can practically see the neurons firing in his brain.")  
time.sleep(1.4)  
delay_print2(" He’s going to do something stupid.")  
print("\n")
time.sleep(2)  

print(speak["grayson_speak"])  
delay_print2("“Ladies first.”")  
time.sleep(2)  
print("\n")

delay_print2("He exaggerates a chivalrous bow.")  
time.sleep(1.1)  
delay_print2(" You want to laugh,\n")  
time.sleep(0.8)  
delay_print2(" but your desire is wiped the moment you remind yourself he’s a bit of a prick.")  
time.sleep(1.6)  
delay_print2(" And anyhow,")  
time.sleep(0.7)  
delay_print2(" you can do over-the-top roleplay better than that.")  
time.sleep(4)  
# -----------------------------------------------------------------------------
# [PLAYER CHOICE - What do you do?]
choices = [
    "PLAY ALONG",
    "IGNORE"
]
selected = select(choices)

# Handle the player's choice
if selected == 0:  # GO ALONG WITH IT
    delay_print2("You raise your voice two octaves higher.")  
    time.sleep(1.2)  
    delay_print2(" “Wow! Thank you kind sir!”")  
    time.sleep(1.6)  
    delay_print2(" You consider batting your lashes,")  
    time.sleep(1.0)  
    delay_print2(" but that might be doing too much.")  
    time.sleep(2)  
    print("\n")

    delay_print2("You step through the hole in the fence,")  
    time.sleep(0.6)  
    delay_print2(" and imagine he’s stupefied.")  
    time.sleep(1)  
    delay_print2(" Maybe he’s not,")  
    time.sleep(0.6)  
    delay_print2(" but it’s fun to think about.")  
    time.sleep(2)  

elif selected == 1:  # IGNORE HIM
    delay_print2("You don't even acknowledge his attempt at humor.")  
    time.sleep(0.7)  
    delay_print2(" You’re too far gone for games like that.")  
    time.sleep(1.2)  
    print("\n")

    delay_print2("Grayson’s voice fades behind you as you move through the hole in the fence without a word,")  
    time.sleep(.6)  
    delay_print2(" the quiet grind of metal on concrete ringing in your ears as you duck through.")  
    time.sleep(3)
    clear()
    time.sleep(1)
    delay_print("...")
    time.sleep(1)
    clear()

# -----------------------------------------------------------------------------

# SCENE 5B:
# [POV SWITCH - Grayson’s POV]
print(povs["grayson_pov"])
delay_print2("The chain-link fence rattles behind you as you swing over it, ")
time.sleep(0.4)
delay_print2("landing with a muted thud on the pavement, ")
time.sleep(0.4)
delay_print2("where tufts of grass have started to seep throigh the cracks——")
time.sleep(0.7)
delay_print2("nature reclaiming what bureaucracy forgot.\n")
time.sleep(1.5)
delay_print2("You straighten out your coat, ")
time.sleep(0.4)
delay_print2("brushing off the flakes of rust that clung to the hem like dead insects.")
print("\n")
time.sleep(1.5)

delay_print2("The compound towers ahead——")
time.sleep(0.4)
delay_print2("unadorned concrete walls,")
time.sleep(0.4)
delay_print2(" stained with time and smoke.")
time.sleep(1.2)
delay_print2("Brutalit and blank, ")
time.sleep(0.4)
delay_print2(" like a structure meant to outlive people")
time.sleep(1.2)
delay_print2("No signage.")
time.sleep(0.4)
delay_print2(" No welcome mat.")
time.sleep(0.6)
delay_print2(" Just that feeling—there’s something wrong in the geometry of it.")
time.sleep(0.7)
delay_print2(" Wrong in the silence.")
print("\n")
time.sleep(1.5)

delay_print2("You light another cigarette.")
time.sleep(0.4)
delay_print2(" You’ve been chain-smoking since Prague.")
time.sleep(0.6)
delay_print2(" You tell yourself it’s the nerves.")
time.sleep(0.4)
delay_print2(" But you know it’s not.")
time.sleep(1.5)
print("\n")

delay_print2("Graham’s already halfway to the courtyard, scanning, twitchy.")
time.sleep(0.6)
delay_print2(" His shoulders tense like he’s wearing someone else’s skin.")
print("\n")
time.sleep(2)
# -----------------------------------------------------------------------------
# [PLAYER CHOICE - What do you do?]
choices = [
    "JOKE",
    "STAY SILENT"
]
selected = select(choices)

# Handle the player's choice
if selected == 0:  # BREAK THE SILENCE
    print(speak["grayson_speak"])
    delay_print2("“If something jumps out and eats you, ")
    time.sleep(0.3)
    delay_print2("I’m not filing the paperwork.”")
    time.sleep(1.5)
    print("\n")

    print(speak["graham_speak"])
    delay_print2(italic_text("(glancing back, muttering)\n"))
    delay_print2("“Wasn’t expecting you to. ")
    time.sleep(0.5)
    delay_print2("Probably forge my death certificate and go get lunch.”")
    time.sleep(1.5)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2(italic_text("(chuckles)\n"))
    delay_print2("“Lunch and a raise. ")
    time.sleep(0.3)
    delay_print2(" Don’t tempt me.”")
    time.sleep(1.5)
    print("\n")

    delay_print2("He doesn’t respond, ")
    time.sleep(.4)
    delay_print2("but his pace slows——")
    time.sleep(.4)
    delay_print2("either from nerves or just the weight of your voice pulling at his spine.")
    time.sleep(2)
    print("\n")

elif selected == 1:  # STAY SILENT
    time.sleep(1.5)
# -----------------------------------------------------------------------------

delay_print2("He hovers near the shadow of the main building, where the gray concrete swallows light.")
time.sleep(1.5)
print("\n")

delay_print2("You follow.")
time.sleep(1.5)
print("\n")

delay_print2("Every step echoes wrong——")
time.sleep(0.4)
delay_print2("too loud, ")
time.sleep(0.3)
delay_print2("too sharp.")
time.sleep(0.6)
delay_print2(" Somewhere, a bird starts to chirp.")
time.sleep(0.4)
delay_print2(" Then stops mid-note.")
time.sleep(1.5)
print("\n")

delay_print2("There’s a streak of something on the compound wall ahead——dark and old.")
time.sleep(0.6)
delay_print2(" Could be blood.")
time.sleep(0.4)
delay_print2(" Could be paint.")
time.sleep(0.4)
delay_print2(" Could even just be a bad joke.")
time.sleep(1.5)
print("\n")

delay_print2("You don’t laugh.")
time.sleep(1.5)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(muttering to yourself)\n"))
delay_print2("“Looks like hell built a bunker.”")
time.sleep(1.5)
print("\n")

delay_print2("Graham pauses near the main door, ")
time.sleep(0.4)
delay_print2("one hand hovering by his belt, ")
time.sleep(0.3)
delay_print2("uncertain if he should draw or knock.")
time.sleep(1.5)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(eyebrow raised)\n"))
delay_print2("“Well? ")
time.sleep(0.2)
delay_print2("You first. ")
time.sleep(0.3)
delay_print2("You were so eager to get inside.”")
time.sleep(1.5)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(frowning)\n"))
delay_print2("“I wasn’t. ")
time.sleep(0.3)
delay_print2("You just walk like a crypt keeper.”")
time.sleep(1.5)
print("\n")

print(speak["grayson_speak"])
delay_print2("“Cute. ")
time.sleep(0.3)
delay_print2("Let’s see if your sense of humour survives inside the compound.”")
time.sleep(1.5)
print("\n")



# Scene: Exploring the Building
delay_print2("Graham leads the way, opening the door and stepping through.")
time.sleep(0.6)
delay_print2("\nThe space beyond swallows light, ")
time.sleep(0.4)
delay_print2("as if it doesn’t want to be seen.")
time.sleep(0.6)
delay_print2("\nYour boots scrape across the concrete floor, ")
time.sleep(0.4)
delay_print2("and the staleness of the air hits you first——")
time.sleep(0.4)
delay_print2("a heavy, ")
time.sleep(0.4)
delay_print2("oppressive weight, ")
time.sleep(0.6)
delay_print2("like the whole place has been holding its breath for years.")
time.sleep(1.2)
delay_print2("\nThe faint smell of mold and something else—something metallic, ")
time.sleep(0.3)
delay_print2("like the air itself has turned rusty.")
time.sleep(2)

print("\n")
delay_print2("Graham freezes, ")
time.sleep(0.4)
delay_print2("scanning the empty hallway.")
time.sleep(0.6)
delay_print2(" His hand stays near his belt.")
time.sleep(0.6)
delay_print2("\nHe’s still acting twitchy.")
time.sleep(0.6)
delay_print2("\nYou don’t blame him.")
time.sleep(0.4)
delay_print2(" The silence here is different.")
time.sleep(0.6)
delay_print2("\nIt’s suffocating, ")
time.sleep(0.6)
delay_print2("like the world beyond the door is a distant memory, ")
time.sleep(0.4)
delay_print2("and everything inside is just… .")
time.sleep(0.6)
delay_print2("waiting.")
time.sleep(2)

print("\n")
print(speak["grayson_speak"])
delay_print2("“Now you’re starting to look like a guy who doesn’t want to be here.”")
time.sleep(1.5)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(eyes darting, hesitant)\n"))
delay_print2("“I never said I did. ")
time.sleep(0.4)
delay_print2("This place feels… ")
time.sleep(0.3)
delay_print2(italic_text('wrong."'))
time.sleep(1.5)
print("\n")

print(speak["grayson_speak"])
delay_print2("“You’re paranoid. ")
time.sleep(0.6)
delay_print2("But hey, ")
time.sleep(0.4)
delay_print2("I’m with you.")
time.sleep(0.6)
delay_print2(" This looks like the kind of place where bad decisions get made.”")
time.sleep(1.5)
print("\n")

delay_print2("You both move deeper into the building.")
time.sleep(0.6)
delay_print2("\nThe dim light filtering through cracked windows doesn’t do much to ease the feeling of claustrophobia building in your chest.")
time.sleep(0.8)
delay_print2("\nThe walls here are streaked—worn down by time and neglect.")
time.sleep(0.6)
delay_print2("\nSome rooms are half-gutted—furniture upended, ")
time.sleep(0.4)
delay_print2("rusted machines, ")
time.sleep(0.4)
delay_print2("old papers scattered like someone just… ")
time.sleep(0.6)
delay_print2("vanished in the middle of their work.")
time.sleep(1.2)
delay_print2("\nNothing seems to have been touched for years.")
time.sleep(0.6)
delay_print2(" It’s like everything was frozen in time.")
print("\n")
time.sleep(2)

delay_print2("You pass by a metal door with a thick window that’s been shattered, shards of glass still hanging from the frame like a twisted ornament.")
time.sleep(0.8)
delay_print2(" Beneath the door, the floor is stained—brown and sticky.")
time.sleep(0.6)
delay_print2(" You step over it, trying not to breathe too deeply.")
time.sleep(0.6)
delay_print2(" Something about the bloodstains doesn’t sit right with you.")
print("\n")
time.sleep(2)

print(speak["graham_speak"])
delay_print2(italic_text("(tense)\n"))
delay_print2("“Something happened here. Doesn’t take a genius to see that.”")
print("\n")
time.sleep(1.5)

print(speak["grayson_speak"])
delay_print2(italic_text("(smirking)\n"))
delay_print2("“Could’ve been a fire drill gone wrong.")
time.sleep(0.4)
delay_print2(" Or a bad lunch order.”")
print("\n")
time.sleep(1.5)

delay_print2("You turn a corner and find yourself facing a long hallway lined with dark doors.")
time.sleep(0.6)
delay_print2(" The place feels like a maze, like it’s designed to confuse or trap.")
time.sleep(0.6)
delay_print2(" You can’t help but feel… watched.")
time.sleep(0.6)
delay_print2(" There’s an eerie hum in the air, like the building itself is alive, trying to tell you something.\n\n")
time.sleep(2)

print(speak["grayson_speak"])
delay_print2(italic_text("(under your breath)\n"))
delay_print2("“I swear, this place is more unsettling than your personality.”")
print("\n")
time.sleep(1.5)

print(speak["graham_speak"])
delay_print2("Graham’s eyes flick to you, then back to the hallway ahead.")
time.sleep(0.6)
delay_print2(" He doesn’t smile.")
time.sleep(0.4)
delay_print2(" He doesn’t laugh.")
print("\n")
time.sleep(1.5)

print(speak["graham_speak"])
delay_print2("“I’m not unsettling.")
time.sleep(0.4)
delay_print2(" Now shut up and keep moving.”")
print("\n")
time.sleep(1.5)

delay_print2("You both keep going.")
time.sleep(0.6)
delay_print2(" You can feel the tension building.")
time.sleep(0.6)
delay_print2(" The hall seems endless, and every creak, every shift in the air makes your skin crawl.")
time.sleep(0.8)
delay_print2(" But you don’t stop.")
time.sleep(0.4)
delay_print2(" You won’t.")
time.sleep(0.4)
delay_print2(" Not yet.")
time.sleep(3)
clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()

# Reset anger counts
game_state["GrahamAnger"] = 0
game_state["GraysonAnger"] = 0



# -----------------------------------------------------------------------------





# SCENE 5C
# PO
delay_print2(povs["grayson_pov"])
delay_print2("The hallway stretches ahead like some twisted game of cat and mouse. ")
time.sleep(.4)
delay_print2("The dim light flickers overhead, casting strange shadows that dance and jitter with every step\n")
time.sleep(.8)
delay_print2("The air is thick with dust, ")
time.sleep(.3)
delay_print2("and  you feel like you're moving through a tomb. ")
time.sleep(.8)
delay_print2("There's no noise")
time.sleep(.4)
delay_print2("——except for the odd creaks and groans of the building settling around you.\n")
time.sleep(1.3)
delay_print2("The silence here is deafening.\n\n")

time.sleep(1.5)
delay_print2("Graham starts walking faster than before, ")
time.sleep(.4)
delay_print2("his steps a little sharper, more anxious. ")
time.sleep(.8)
delay_print2("You're not sure if it's the silence or the sense that something is about to go wrong\n\n")
time.sleep(1.3)

print(speak["graham_speak"])
delay_print2(italic_text(("(urgently, halting suddenly)\n")))
time.sleep(.8)
delay_print2('"Wait——')
time.sleep(.2)
delay_print2('did you hear that?!"')
print("\n")

time.sleep(1.5)
delay_print2("Your hand instinctively falls to your firearm, ")
time.sleep(.4)
delay_print2("immediately aleart. ")
time.sleep(.8)
delay_print2("There's no sound.\n")
time.slee(.8)
delay_print2("No movement.\n")
time.sleep(.8)
delay_print2("Just the oppresive silence of the compound.")
time.sleep(.4)
delay_print2(" For a moment, it felt like the world itself was holding its breath. ")
time.sleep(.8)
delay_print2('\n\n')
print(speak["grayson_speak"])
delay_print2(italic_text(("(relieved, annoyed)\n")))
delay_print2('"Seriously,')
time.sleep(.2)
delay_print2(" quit that.")
time.sleep(.4)
delay_print2("What do you hear?")
time.sleep(.4)
delay_print2(" A rat sneezing?")
time.sleep(.4)
delay_print2(' You\'re going nuts."')
print("\n")

# -----------------------------------------------------------------------------

print(speak["graham_speak"])
delay_print2(italic_text("(snapping)\n"))
delay_print2("“I'm serious, Grayson. Something’s out there.”\n\n")
time.sleep(2.5)

# Player Choice - How does Grayson respond?
choices = [
    "DISMISSIVE",
    "REASSURE",
    "JOKE"
]
selected = select(choices)

if selected == 0:  # DISMISSIVE
    game_state["GrahamAnger"] += 2
    delay_print2("He needs to calm down. You’ve seen it, he’s been walking around, eyes darting like everything’s out to get him.")
    print ("\n")
    time.sleep(0.8)
    delay_print2(" Everything, including you.\n")
    time.sleep(1)
    delay_print2("“Uh huh... It's probably just the wind playing tricks on your ears as usual.”\n\n")
    time.sleep(1.5)

    print(speak["graham_speak"])
    delay_print2(italic_text("(eyebrows furrowed)\n"))
    delay_print2("“We’re in an abandoned building, investigating a report of something reanimated, whatever that even means, and you want to just be lax about it?”\n\n")
    time.sleep(1.5)

elif selected == 1:  # REASSURING
    game_state["GrahamAnger"] -= 1
    delay_print2("You get it, he's nervous, but if he keeps twitching like this at every creak, he’s seriously going to get us into some trouble.\n")
    time.sleep(1)
    delay_print2("“Relax rookie, if something jumps out, I’ll just shoot it.”\n\n")
    time.sleep(1.5)

    print(speak["graham_speak"])
    delay_print2(italic_text("(sighs)\n"))
    delay_print2("“I’m not very soothed with how lightly you’re taking this.”\n\n")
    time.sleep(1.5)

elif selected == 2:  # JOKE IT OFF
    game_state["GrahamAnger"] += 1
    delay_print2("He’s wound up way too tight. Someone needs to lighten the atmosphere and it doesn’t look like it’s going to be him anytime soon.\n")
    time.sleep(1)
    delay_print2("“Place holder!!!!”\n\n")
    time.sleep(1.5)

    print(speak["graham_speak"])
    delay_print2(italic_text("(raising voice)\n"))
    delay_print2("“I’m being serious.”\n\n")
    time.sleep(1.5)


# -----------------------------------------------------------------------------


# Switch to Graham's POV
print(povs["graham_pov"])
time.sleep(2)

# Player Choice - How does Graham respond?
choices = [
    "DEFENSIVE",
    "CONFRONT",
    "DROP IT"
]
selected = select(choices)

if selected == 0:  # DEFENSIVE
   
    delay_print2("You can see it in his eyes because you’ve seen it so often. He thinks you are crazy and paranoid.\n\n")
    time.sleep(2)
    game_state["GraysonAnger"] += 1
    print(speak["graham_speak"])
    delay_print2("“Can you just stop dismissing everything I say?”\n\n")
    time.sleep(2.5)

elif selected == 1:  # CONFRONT
    game_state["GraysonAnger"] += 2
    print(speak["graham_speak"])
    delay_print2("If he wants to risk his life, so be it, but you’re not letting some self-important man risk yours too.\n")
    time.sleep(0.8)
    delay_print2("“If you keep taking things this lightly, you’re going to get us killed.”\n\n")
    time.sleep(1.5)

elif selected == 2:  # DROP IT
    game_state["GraysonAnger"] -= 1
    print(speak["graham_speak"])
    delay_print2("Whatever. If he wants to keep risking things, that's his business.\n")
    time.sleep(0.8)
    delay_print2("You narrow your eyes.\n")
    time.sleep(0.5)
    delay_print2("“You better hope that you’re right.”\n\n")
    time.sleep(1.5)

# -----------------------------------------------------------------------------

# Switch to Grayson's POV
print(povs["grayson_pov"])

# Grayson's POV - How does Grayson respond?
choices = [
    "BLUNT",
    "DISMISSIVE",
    "DROP IT"
]
selected = select(choices)

if selected == 0:  # BLUNT
    game_state["GrahamAnger"] += 2
    print(speak["grayson_speak"])
    delay_print2("He’s been doing nothing but slow you down this whole time, and you’ve been miraculously tolerant.\n")
    time.sleep(0.8)
    delay_print2("Yet he thinks he can look down on and lecture you?\n")
    time.sleep(0.5)
    delay_print2("“Maybe if you weren’t so paranoid all the time, we’d be fine.”\n\n")
    time.sleep(1.5)

elif selected == 1:  # DISMISSIVE
    game_state["GrahamAnger"] += 1
    print(speak["grayson_speak"])
    delay_print2("He’s incompetent, paranoid, and whiny. The only thing you want most right now is for him to stop talking.\n")
    time.sleep(0.8)
    delay_print2("“Yeah, yeah, whatever you say, damn rookie.”\n\n")
    time.sleep(1.5)

elif selected == 2:  # DROP IT
    game_state["GrahamAnger"] -= 1
    print(speak["grayson_speak"])
    delay_print2("This is getting you nowhere. Every response you grant him is valuable energy you waste.\n")
    time.sleep(0.8)
    delay_print2("Plus, he’s starting to give you a headache.\n")
    time.sleep(0.5)
    delay_print2("“Forget about it rookie, we need to focus on our investigation.”\n\n")
    time.sleep(1.5)


# -----------------------------------------------------------------------------


# Graham's POV - How does Graham respond?
print(povs["graham_pov"])
choices = [
    "CONFRONT",
    "MUTTER OUT LOUD",
    "MUTTER TO YOURSELF"
]
selected = select(choices)

if selected == 0:  # CONFRONT
    game_state["GraysonAnger"] += 2
    print(speak["graham_speak"])
    delay_print2("You don’t know if he has even listened to you once this whole time.\n")
    time.sleep(0.8)
    delay_print2("“Why can’t you just think beyond yourself for once?”\n\n")
    time.sleep(1.5)

elif selected == 1:  # MUTTER OUT LOUD
    game_state["GraysonAnger"] += 1
    print(speak["graham_speak"])
    delay_print2("He just won’t listen to you. He hasn’t, ever. You try to stop it but—\n")
    time.sleep(0.8)
    delay_print2("“Pretentious prick.”\n")
    time.sleep(0.5)
    delay_print2("Yup. That was loud.\n\n")
    time.sleep(1.5)

elif selected == 2:  # MUTTER TO YOURSELF
    game_state["GraysonAnger"] -= 1
    print(speak["graham_speak"])
    delay_print2("Nothing you say will be productive. Still, you’re petty enough to want to say something, even if it is inaudible.\n")
    time.sleep(0.8)
    delay_print2("“...Prick.”\n\n")
    time.sleep(1.5)


# -----------------------------------------------------------------------------

# Grayson responds
print(speak["grayson_speak"])
delay_print2("“Huh? Wanna repeat that again for me rookie?”\n\n")
time.sleep(1.5)

print(speak["graham_speak"])
delay_print2("“You never listen to anyone. It’s always your way or nothing!”\n\n")
time.sleep(1.5)

print(speak["grayson_speak"])
delay_print2("“Because hesitation gets people killed.”\n\n")
time.sleep(1.5)

print(speak["graham_speak"])
delay_print2("“Sometimes, thinking things through saves lives.”\n\n")
time.sleep(1.5)

print(speak["grayson_speak"])
delay_print2("“And sometimes—“")
print("\n")
time.sleep(1.5)

# Sudden interruption
delay_print2("Suddenly, from the shadows, a grotesque figure lunges forward with a guttural snarl.\n")
time.sleep(0.8)
delay_print2("Its pale, mottled skin stretches over a skeletal frame, and its glassy eyes lock onto its target.\n\n")
time.sleep(2)

# -----------------------------------------------------------------------------
# Determining Who is Grabbed

if game_state["GrahamAnger"] > game_state["GraysonAnger"]:
    grabbed = "GRAHAM"
elif game_state["GraysonAnger"] > game_state["GrahamAnger"]:
    grabbed = "GRAYSON"
else:
    grabbed = random.choice(["GRAHAM", "GRAYSON"])

# -----------------------------------------------------------------------------

# HANDLE OUTCOME BASED ON WHO IS GRABBED
if grabbed == "GRAHAM":
    # GRAHAM IS GRABBED
    print(povs["grayson_pov"])
    delay_print2("Graham is caught off guard as the creature lunges at him, wrapping its claws around his arms, pulling him towards its gaping maw.\n\n")
    time.sleep(1.5)

    if game_state["GraysonAnger"] >= 3:
        # GRAYSON HESITATES
        delay_print2("You hesitate.")
        print("\n")
        time.sleep(1.5)

        print(speak["graham_speak"])
        delay_print2("“Don’t just stand there, help me!”")
        print("\n")
        time.sleep(1.5)

        delay_print2("You quickly snap out of it, and pull Graham to safety. However, Graham is scratched in the process.\n\n")
        time.sleep(1.5)
        game_state["GrahamTrustInGrayson"] -= 3  # Adjust trust in Grayson's POV

    else:
        # GRAYSON ACTS IMMEDIATELY
        delay_print2("Without thinking, you grab Graham by the arm and pull him back.\n")
        time.sleep(0.8)
        delay_print2("The creature’s claws scrape the air where Graham was standing a second ago, its breath rancid, filling your nose with the stench of decay.\n\n")
        time.sleep(1.5)
        game_state["GrahamTrustInGrayson"] += 3  # Adjust trust in Grayson's POV

# -----------------------------------------------------------------------------

elif grabbed == "GRAYSON":
    # GRAYSON IS GRABBED
    print(povs["graham_pov"])
    delay_print2("Grayson is caught off guard as the creature lunges at him, wrapping its claws around his arms, pulling him towards its gaping maw.\n\n")
    time.sleep(1.5)

    if game_state["GrahamAnger"] >= 3:
        # GRAHAM HESITATES
        delay_print2("You hesitate.\n\n")
        time.sleep(1.5)

        print(speak["grayson_speak"])
        delay_print2("“Well shit! Don’t just stand there, help me!”\n\n")
        time.sleep(1.5)

        delay_print2("You quickly snap out of it, and pull Grayson to safety. However, Grayson is scratched in the process.\n\n")
        time.sleep(1.5)
        game_state["GraysonTrustInGraham"] -= 3  # Adjust trust in Graham's POV

    else:
        # GRAHAM ACTS IMMEDIATELY
        delay_print2("Without thinking, you grab Grayson by the arm and pull him back.\n")
        time.sleep(0.8)
        delay_print2("The creature’s claws scrape the air where Grayson was standing a second ago, ")
        time.sleep(.5)
        delay_print2("its breath rancid, ")
        time.sleep(.5) 
        delay_print2("filling your nose with the stench of decay.")
        print("\n")
        time.sleep(1.5)
        game_state["GraysonTrustInGraham"] += 3  # Adjust trust in Graham's POV

# -----------------------------------------------------------------------------

# RETEAT
delay_print2("You shove him backwards, the two of you stumbling as you retreat down the hallway.\n")
time.sleep(0.8)
delay_print2("The creature snarls again, ")
time.sleep(.3)
delay_print2("its growl growing louder, ")
time.sleep(.6)
delay_print2("angrier.")
time.sleep(1.5)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(while running)"))
delay_print2("\n“What the hell was that?!”")
time.sleep(1.5)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(while running)"))
delay_print2("\n“Hell do I know, ")
time.sleep(.3)
delay_print2("just focus on getting out of here first!”")
time.sleep(1.5)
print("\n")

delay_print2("The hallway blurs past in streaks of concrete and rust, ")
time.sleep(.4)
delay_print2("your shoes pounding over chipped tile.")
time.sleep(1.5)
delay_print2("\nYou hear it before you see it. ")
time.sleep(.3)
delay_print2("That gurgling, ")
time.sleep(.3)
delay_print2("that wet rasp dragging through the halls.")
time.sleep(2)
print("\n")

delay_print2("You and Graham round a corner.")
time.sleep(1.5)
print("\n")

delay_print2("Behind you,")
time.sleep(0.7)
delay_print2("\nFootsteps stop.")
time.sleep(2)
print("\n")

delay_print2("You whip around.")
time.sleep(2)
print("\n")

print(speak["grayson_speak"])
delay_print2("“…Svoboda!”")
time.sleep(3)
print("\n")

delay_print2("He’s frozen, halfway down the corridor. Gun drawn. Both hands on it, like he actually knows what he’s doing.")
time.sleep(2)
print("\n")

delay_print2("The thing stumbles into view in front of him.")
time.sleep(1)
print("\n")

delay_print2("Your blood goes cold.")
time.sleep(2)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(shouting)"))
delay_print2("\n“Idiot!")
time.sleep(.3)
delay_print2(" Do you even know how to use that?!”")
time.sleep(1.5)
print("\n")

delay_print2("Then——")
time.sleep(0.9)
print(italic_text("\nClick."))
time.sleep(2.5)
print("\n")

delay_print2("Nothing.")
time.sleep(2)
print("\n")

delay_print2("Goddammit.")
time.sleep(1.5)
delay_print2("\nHis gun jammed.")
time.sleep(4)
print("\n")

# [PLAYER CHOICE - What do you do?]
choices = [
    "SHOOT THE WALKER",
    "GRAB GRAHAM AND FLEE"
]
selected = select(choices)

if selected == 0:  # SHOOT THE WALKER
    delay_print2("There's no time to think. ")
    time.sleep(1)
    delay_print2("You draw your pistol and fire—")
    time.sleep(1)
    delay_print2("\nBang.")
    time.sleep(2)
    print("\n")

    delay_print2("The creature jerks back with a guttural screech. ")
    time.sleep(1)
    delay_print2("It stumbles——")
    time.sleep(.7)
    delay_print2("but doesn’t fall.")
    time.sleep(2)
    print("\n")

    print(speak["graham_speak"])
    delay_print2("“Did you get it?!”")
    time.sleep(1.5)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2(italic_text("(gritted teeth)"))
    delay_print2("\n“Not enough. ")
    time.sleep(.5)
    delay_print2("Move, Svoboda!”")
    time.sleep(1.5)
    print("\n")

    delay_print2("It lunges again. ")
    time.sleep(1)
    delay_print2("You fire twice more. ")
    time.sleep(1.5)
    delay_print2("It crashes to the floor, twitching. ")
    time.sleep(2)
    print("\n")

    print(speak["graham_speak"])
    delay_print2("“Holy crap, Grayson—”")
    print("\n")

    print(speak["grayson_speak"])
    delay_print2("“Save the talk for later, ")
    time.sleep(.3) 
    delay_print2("we need to get out of here first!”")
    time.sleep(1.5)
    print("\n")

elif selected == 1:  # GRAB GRAHAM AND FLEE
    delay_print2("You don’t think. ")
    time.sleep(.8)
    delay_print2("You lunge forward, ")
    time.sleep(.5)
    delay_print2("grab him by the collar, ")
    time.sleep(.3)
    delay_print2("and pull.")
    time.sleep(1.5)
    print("\n")

    print(speak["grayson_speak"])
    delay_print2("“Forget it——run!”")
    time.sleep(1.5)
    print("\n")

    delay_print2("The thing screeches. ")
    time.sleep(1)
    delay_print2("You run harder.")
    time.sleep(1.5)
    print("\n")

    delay_print2("Graham’s frantic limbs cross over themselves and he nearly falls face first.")
    time.sleep(1.5)
    delay_print2("\nYou throw your arm around him and drag him up to keep him running.")
    time.sleep(2)
    print("\n")

    delay_print2("Behind you, ")
    time.sleep(.3)
    delay_print2("the abomination screams and bangs clumsily against walls, ")
    time.sleep(.5)
    delay_print2("causing a constant strobe of sharp clangs like the beating of a drum.")
    time.sleep(2)
    print("\n")

# Aftermath
delay_print2("The two of you burst through a half-collapsed doorway, ")
time.sleep(.3)
delay_print2("slamming it shut behind you.")
time.sleep(1.5)
delay_print2("\nYou can still hear your heartbeat, ")
time.sleep(1)
delay_print2("like it's trying to punch its way out of your chest.")
time.sleep(2)
print("\n")

delay_print2("Graham slumps to the floor, shaking.")
time.sleep(1.5)
delay_print2("\nYou can’t even look at him right away.")
time.sleep(1)
delay_print2 (" our hands are still shaking.")
time.sleep(1.5)
delay_print2("\nHe could’ve died.")
time.sleep(1)
delay_print2(" You could’ve died.")
time.sleep(1.5)
delay_print2("\nAnd worst of all——")
time.sleep(0.8)
delay_print2("\nYou're not sure that next time, ") 
time.sleep(.3)
delay_print2("either of you will be as lucky.")
time.sleep(2)
print("\n")

# after the escape
print(speak["graham_speak"])
delay_print2(italic_text("(whispers)"))
time.sleep(0.5)
delay_print2("\n“It wasn’t human…”")
time.sleep(2)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(pale, eyes unfocused)"))
time.sleep(.5)
delay_print2("\n“No. ")
time.sleep(.3)
delay_print2("It wasn’t.”")
time.sleep(3)
print("\n")

delay_print2("A long pause. ")
time.sleep(1.5)
delay_print2("The silence roars.")
time.sleep(3)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(staring blankly)"))
time.sleep(.5)
delay_print2("\n“It looked dead. ")
time.sleep(1)
delay_print2("But it moved. ")
time.sleep(1.5)
delay_print2("It watched me.”")
time.sleep(2)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(not denying it)"))
(.5)
delay_print2("\n“It shouldn’t be possible.”")
time.sleep(3)
print("\n")

print(speak["graham_speak"])
delay_print2(italic_text("(voice cracking)"))
time.sleep(.5)
delay_print1("\n“It misfired.”")
time.sleep(2.5)
print("\n")

print(speak["grayson_speak"])
delay_print2(italic_text("(quietly)"))
time.sleep(1)
delay_print1("\n“I know.”")
time.sleep(4)
print("\n")

# EPILOGUE/ENDING SET UP
delay_print2("Among the filthy piles of refuse and the putrid smell of decay,")
time.sleep(.5)
delay_print2("two men sat, ")
time.sleep(.3)
delay_print2("as discarded and isolated as the rotting building around them.")

time.sleep(1)
delay_print2("\nEach one knew it then, ")
time.sleep(.5)
delay_print2("through some illogical stirring in their gut, ")
time.sleep(.3)
delay_print2("a shared thought prevailed.")
print("\n")
time.sleep(1)
delay_print2("The reprieve of silence protected their last peace, ")
time.sleep(.3)
delay_print2("and the moment it ended,")
time.sleep(.3)
delay_print2("the final breath of the life they once knew would fracture irrevocably.")
time.sleep(1)
delay_print2("\nSo for fear of abandoning the comfortable and known, ")
time.sleep(.5)
delay_print2("neither one spoke.")

time.sleep(1)
delay_print2("\nBut the silence could not last forever, ")
time.sleep(.3)
delay_print2("and eventually, ")
time.sleep(.3)
delay_print2("the truth of the situation would need to be confronted.")
time.sleep(1.5)
print("\n")

delay_print2('"But not now, ')
time.sleep(0.3)
delay_print2('not for a few more minutes,"')
delay_print2("\nthey both thought.")
time.sleep(8)
clear()
time.sleep(1)
delay_print("...")
time.sleep(1)
clear()
delay_print1(bold_text("TO BE CONTINUED..."))