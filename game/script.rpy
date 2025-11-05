# The script of the game goes in this file.

# Declare Character variables here so it is easier to call them when making the dialogue
# The color part changes the text color of that characters specifically so change it to what you like
define n = Character("Narrator")
define t = Character("Tree")
define b = Character("Bear", color="#e0c7ff") # Light purple
define r = Character("Racoon", color="#6e7b8b") # Gray
define tl = Character("Turtle", color="#6dc066") # Green
define hb = Character("Hummingbird")
define c = Character("Coyote")
define df = Character("Dragonfly")

# Declare permanent or constantly used variables for the game

default RunCount = 0  #Tally how many branches the player has done or started

 # Use this to track which branches the players have completed or have not
default RacoonBranch = False 
default BearBranch = False
default DragonflyBranch = False



#-----------------------
#-Scene and character commands
#-----------------------
#Scene command: Insert the backgrounds into the images folder in your files and then you can call them with the 
# bg followed by the file name 

#Show command: Same as the Scene, insert into the images tab and it can be freely called in the code so long as everyone
# has the images uploaded

#WARNING: Files are case sensitive so they should each be given unique names. Reason being that if one word is similar
# it will overwrite any other onscreen asset with similar words in it
#

#---------------------------
# -The game starts here.
#--------------------------

label start:
    "…"
    "\“Who are you?\”"
    "A question that rings throughout your fleeting thoughts."
    "You were here. You were just here. And now…"
    "…"
    "You were doing something. What were you doing? Now you…"
    "Can't…remember…"
    "You…what kind of……beast…"
    "…the Lake…get to…"
    "…all that's…left…"
    "…your Pack…"
    jump starting_choice

label starting_choice:
    menu:
        "Follow the Raccoon":
            jump Choose_Raccoon
        "Follow the Bear":
            jump Choose_Bear
        "Follow the Dragonfly":
            jump Choose_Dragonfly


#---------------------------------------------------
#--Branching narrative starts here and the player chooses which route
#---------------------------------------------------


#------------------------------------------
#-Start Raccoon Branch
#------------------------------------------
label Choose_Raccoon:

    "The Raccoon, a funny little fella who has a funny face"
    "Do not be fooled however, the Raccoon is agile and acrobatic. Furthermore it carries the innate trait of {i} magic pocket{/i}"

    menu: 
        "Choose the Raccoon"

        "Yes":
            jump Begin_Raccoon
<<<<<<< Updated upstream
        "No":
=======
        "No?":
>>>>>>> Stashed changes
            jump starting_choice

label Begin_Raccoon:
#------------------------------------------
#-End Raccoon Branch
#------------------------------------------


#------------------------------------------
#-Start Bear Branch
#------------------------------------------
label Choose_Bear:
    "The Bear, a stoic grumpy creature."
    "It's strength dominates the forest and its intuition gives its innate {i} path sensing{/i} abilities. "

    menu: 
        "Choose the Bear"

        "Yes":
            jump Begin_Bear
<<<<<<< Updated upstream
        "No":
=======
        "No?":
>>>>>>> Stashed changes
            jump starting_choice

label Begin_Bear:

#------------------------------------------
#-End Bear Branch
#------------------------------------------


#------------------------------------------
#-Start Dragonfly Branch
#------------------------------------------
label Choose_Dragonfly:

    "{i} Dragonfly, ever full of hope, mostly relies on their [[Foresight] to glimpse the future. If that fails, their [[Compound Eyes] can take in additional information from their present surroundings.{i}"

    menu: 
        "Choose the Dragonfly"

        "Yes":
            jump Begin_Dragonfly
<<<<<<< Updated upstream
        "No":
=======
        "No?":
>>>>>>> Stashed changes
            jump starting_choice

label Begin_Dragonfly:
    "{i} A small Dragonfly emerges from the brush, flitting about lazily through the air. {i}"

    df "What a lovely afternoon…the breeze feels just right today."

    df "This is what I love about the forest. Everything seems so warm and inviting on a day like this."

    df "But this is no time to be still. I suppose I should start making my way towards this lake."

    df "Although, it appears I've forgotten where it is. All I know is that it seems…important."

    df "Well, no matter. If it's important, then I'm sure I will come across it sooner or later."

    df "All in good time."

    df "Hmm…now which direction should I go..?"

#------------------------------------------
#- End Dragonfly Branch
#------------------------------------------


# Using return ends the game but I forgot how change it so it ends depending on a route
    return
