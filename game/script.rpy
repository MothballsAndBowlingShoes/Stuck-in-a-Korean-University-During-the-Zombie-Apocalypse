# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bm = Character("Byun Min")
define jh = Character("Jee Hwan")
define m = Character("???")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bustop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.
    "I sigh, as i hate Biology."
    "Right now, i'm majoring in mechanical engineering."
    "I have always loved mechanics as I had been working in a car shop my family owned since a young age"
    "Biology is something I have only ever taken for requirements sake, and that's what this is."
    "The stranger next to me agrees." 
    
    show bm
    with fade
    
    m "I also hate biology, it's just not really my thing"
    jh "Me neither its always been a mess to deal with"
    "i look away."
    "i've never been great at making eye contact"
    m "So what year are you in?"
    "She smiles at me."
    jh "Second year. I’m only 19 though"
    m "Cool! I'm also in my second year"
    "She laughs"
    bm "What's your name? Mine is Byun Min"
    jh "Jee Hwan"





    # This ends the game.

    return
