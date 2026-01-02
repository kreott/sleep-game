# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("???")


# The game starts here.

label start:

    scene bgroom with fade

    play sound "alarm.wav" fadein 2

    p "Ugh..."

    "You get up from your bed to stop the alarm"

    return
