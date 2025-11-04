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

    #These if statements are using the variable Branch variables to confirm whether the player has completed this branch or not.
    #If they have, the game will not allow them to pick that route again.
    #That way there is no risk of the player repeating the same route over and over again. 

        "Follow the Raccoon" if RacoonBranch is False:
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
label Choose_Raccoon

    "The Raccoon, a funny little fella who has a funny face"
    "Do not be fooled however, the Raccoon is agile and acrobatic. Furthermore it carries the innate trait of{i} magic pocket{/i}"

    menu: 
        "Choose the Raccoon"

        "Yes?":
            jump Begin_Raccoon
        "No?":
            jump start

label Begin_Raccoon:
    "Still in progress... :P Blame the Raccoon, they were sleeping in again."
    $ RacoonBranch = True
    jump start
#------------------------------------------
#-End Raccoon Branch
#------------------------------------------


#------------------------------------------
#-Start Bear Branch
#------------------------------------------
label Choose_Bear:
    "The Bear, a stoic grumpy creature."
    "It's strength dominates the forest and its intuition gives its innate{i} path sensing{/i} abilities. "

    menu: 
        "Choose the Bear"

        "Yes?":
            jump Begin_Bear
        "No?":
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

    if RunCount >= 2:
        b "I gotta keep moving, this string is the key to finding them. Once I find them we need to find that lake and end this once and for all."


    " N: The bear follows the blue string further into the forest. Will there be a reward, or misery at the end?"
    jump Bear_Tile_2


#---------------------------
#--End Bear Tile 1
#--------------------------


#---------------------------
#--Begin Bear Tile 2
#--------------------------

label Bear_Tile_2:
    "The sun was now past the midway point. The Bear roamed through the forest, rather annoyed as to how long the string goes."
    "It endlessly reaches through the forest, weaving through the trees, the bushes, and the horizon at times."

    b " This part of the forest is different. Bigger trees, mushrooms, and it smells more humid. The trees are blocking more of the sun around here. This area is going to be dangerous at night."
    
    b "The darkness will appear here faster. I need to move out of here quickly before nightfall."

    "Bear picked up the pace through this part of the forest. But something felt off. The Bear rounded around the rock wall once more, only to find themselves facing it again in front of them."

    b " What is going on here?"

    " The Bear pauses, scans their surroundings and runs in a different direction. They round trees and bushes only to find themselves next to the giant rock again."

    p " Hehehehe..."

    b " Who's there? Show yourself!"

    p " Hahaha!"

    " Out of thin air, balls of light manifest brightly before the Bear's eyes. These glowing lights are the local pixies of the forest. They love to play tricks on the local wildlife and this time they found something extraordinary."
    
    p " It. Yes. Yes. Yes. Yes. This one is special. Special. Special. Special. "

    b " Who are you calling special? "

    b " The Bear lunges at the flying pixies who gracefully flutter out of harm's way."

    p " Oh. Oh. Oh. Oh... Mean creature. Yes, mean creature. Punishment needed. Yes, punishment needed! Fight! Fight! Fight! Fight!"

    " The Bear got a bad feeling from this. Rightfully so as a spark bolt hit them in the body"

    b"OW! HEY STOP THAT! CRAP!"

    " The Bear realized quickly it is not the predator here. It is prey being hunted by a pack of psychotic predators who can fly and use all forms of magic. Bolts of magic, levitation, minor teleport."
    " The Bear suffered constantly trying to find an exit out of this trap."

    menu:
        "Look around":
            jump escape_plan

label escape_plan:
    " As the bear surveyed the area for anything useful they spotted something peculiar. They ran again, taking a magical beating. They were once again teleported back by the pixies, and there it was in front of the Bear: A fairy circle clear as day." 
    " The toadstools made the perfect circle that pixies would come out of."
    " The Bear sprinted immediately for the toadstools in order to destroy the fairy circle."

    p " No! No! NO! Do not interrupt the circle! Yes! Yes!"

    " The pixies frantically all casted their magic at once. A unison of chaos. The teleport spell acted immediately shifting the bear out of the way." 
    " Unfortunately one pixie did not anticipate they would miss and hit a toadstool."

    p " AHH! No! No! Bad! Bad! Not good!"

    b "Perfect... I need to... swipe at those... mushrooms... Thought the Bear to themself."

    " The Bear's energy was sapped from the barrage of attacks and constant running. They needed one chance. The pixies all in desperation used teleport wildly. Moving the Bear everywhere in their domain."
    " The Bear was getting nauseous, but they could tell that they were still in the general area of the fairy circle. How would they know if they were in front of the circle? It happened for a quick second." 
    " They saw the{i} blue thread{/i} followed by a quick flash of the toadstools."

    b " That's it! They thought."

    "The Bear concentrated their focus on waiting for that one moment. One good swipe would destroy most of the fairy circle"

    b "Please... Please..."

    "The nausea was getting to the Bear's head. They needed to stay focused. They had one chance at this."
    "Right on time, the{i} blue thread {/i}appeared."
    
    menu:
        "Paw Swipe":
            jump Destroy_fairyCircle


label Destroy_fairyCircle:
   
    " The Bear swiped mid teleport and as anticipated, their claws landed on the fairy circle. Shredding the toadstools into tiny pieces."

    p "NO! NO! NO! NO! RUN! RUN! RUN!"

    " The pixies without their fairy circle are nothing. The glow the pixies created dissipated faintly into the forest."
    " The sunlight became more apparent to the Bear who was now laying on the floor throwing up from the nausea induced teleporting spree."

    " Fatigue took over the Bear's body. The pain and exhaustion of being attacked with magic left clear scars and burns across the bear's fur."
    "These were not scars of honor. No, these were the scars of a fool who did not think twice before acting."
    "With the battle over the Bear passed out in the Fairy forest. Hoping nothing would approach it in its defenseless state"
    
    " {i} To be continued{/i}"
    return



#---------------------------
#--End Bear Tile 2
#--------------------------


#------------------------------------------
#-End Bear Branch
#------------------------------------------


#------------------------------------------
#-Start Dragonfly Branch
#------------------------------------------
label Choose_Dragonfly

    "The Dragonfly, the aerial assassin of the insect kingdom"
    "The Dragonfly sees many things, its eyes can detect the motions of the unknown. Many call it{i} Future sight{/i}. "

    menu: 
        "Choose the Dragonfly"

        "Yes?":
            jump Begin_Dragonfly
        "No?":
            jump start

label Begin_Dragonfly:
    "Still in progress... :P Dragonfly got distracted staring at dandelion seeds."
    $ DragonflyBranch = True
    jump start
#------------------------------------------
#- End Dragonfly Branch
#------------------------------------------


# Using return ends the game but I forgot how change it so it ends depending on a route
    return
