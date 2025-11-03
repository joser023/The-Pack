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
"In order to understand the inner workings of a machine, it is said one must become one with the machine. What does it mean to become one?"
"How does that apply in the case of living in a forest teeming with critters, magical entities, and humans who all come with separate goals."
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

"Choose the Raccoon?"
    menu: 
        "Yes":
            jump Begin_Raccoon
        "No":
            jump start

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

"Choose the Bear?"
    menu:
        "Yes":
            jump Begin_Bear
        "No":
            jump start



#---------------------------
#--Begin Bear Tile 1
#--------------------------

label Begin_Bear:

" The forest lay dormant. The sun rests a few hours before reaching its peak. It's quiet."
" The wind rattles the leaves on trees and brushes the fur of the animals who are awake. One resident however, feels there is too much wind and not enough clouds in sight."

    b "I can't tell if there is going to be a storm approaching or if there is a separate force that is manipulating the wind? It does not matter. I need to keep following this weaving trail of string that I see."

    if RunCount <= 1:
        b "The string carries a soft blue hue, if I wack it with my paw it simply turns to air and then comes back. I don't see anything it is tied to either."
        b "My body wants to follow it by instinct, so I let it do so."

    b "No other strings have appeared since I started following this blue string."

    b " I'm not even sure if other animals see it as well."

" N: The bear follows the blue string further into the forest. Will there be a reward, or misery at the end?"

return
#---------------------------
#--End Bear Tile 1
#--------------------------



#------------------------------------------
#-End Bear Branch
#------------------------------------------


#------------------------------------------
#-Start Dragonfly Branch
#------------------------------------------
label Choose_Dragonfly:

"The Dragonfly, the aerial assassin of the insect kingdom"
"The Dragonfly sees many things, its eyes can detect the motions of the unknown. Many call it {i} Future sight{/i}. "

 "Choose the Dragonfly?"
    menu: 
        "Yes":
            jump Begin_Dragonfly
        "No":
            jump start

label Begin_Dragonfly:
#------------------------------------------
#- End Dragonfly Branch
#------------------------------------------


# Using return ends the game but I forgot how change it so it ends depending on a route
    return
