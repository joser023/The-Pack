# The script of the game goes in this file.


# Declare Character variables here so it is easier to call them when making the dialogue
#You can use capital or lowerscase letters and numbers. No spaces though.
# The color part changes the text color of that characters specifically so change it to what you like

#Minor Characters
define n = Character("Narrator")
define t = Character("Tree")
define p = Character("Pixies")


#The Main cast of characters
define b = Character("Bear", color="#e0c7ff") # Light purple
define r = Character("Racoon", color="#6e7b8b") # Gray
define tl = Character("Turtle", color="#6dc066") # Green
define hb = Character("Hummingbird")
define c = Character("Coyote")
define df = Character("Dragonfly")


# Declare permanent or constantly used variables for the game

# List of how many times a character has appeared in the story

# Checks to see how many time Bear appears
default Bsighting = 0

# Checks to see how many time Raccoon appears
default Rsighting = 0

# Checks to see how many time Turtle appears
default TLsighting = 0

# Checks to see how many time Hummingbird appears
default HBsighting = 0

# Checks to see how many time Coyote appears
default Csighting = 0

# Checks to see how many time Dragonfly appears
default DFsighting = 0


default RunCount = 0  #Tally how many branches the player has done or started

default MapNumber = 1 #keeping track of your position on the map...mostly

 # Use this to track which branches the players have completed or have not
default RaccoonBranch = True
default BearBranch = True
default DragonflyBranch = True


#i’m taking the filenames based directly on what is in our google drive art folder! I’ll leave comments breaking up the art by category


#animal ingame assets . the larger drawings, not the headshots.


image bear = "images/FullBody/Bear.png"
image coyote = "images/FullBody/Coyote.PNG"
image dragonfly = "images/FullBody/Dragonfly.png"
image hummingbird = "images/FullBody/Hummingbird.PNG"
image raccoon = "images/FullBody/Raccoon.PNG"
image turtle = "images/FullBody/Turtle.PNG"
image FishFairy = "images/FullBody/KoiFish.png"


#animal headshots. To abbreviate and differentiate between the ingame PNGS, I’m adding a “HS” before the name of each animal. Capital, so it reads more clearly between the name of the animal.


image HSbear = "images/HS/HS-Bear.png"
image HScoyote = "images/HS/His-Coyote.PNG"
image HSdragonfly = "images/HS/HS-Dragonfly.png"
image HShummingbird = "images/HS/HS-Hummingbird.png"
image HSraccoon = "images/HS/HS-Raccoon.PNG"
image HSturtle = "images/HS/HS-Turtle.PNG"
image HSfishfairy = "images/HS/HS-Koi.png"


# map. The way I structured the naming was with two digits primarily (example, 0.0) the first being the column, the second being the row. So if you wanted the second tile down from column three, it would be 3.2. Think of the numbers like (C.R) , with c/r being column and row respectively.


image map1 = "images/Tiles/map1.png"
image map2_1 = "images/Tiles/map2.1.png"
image map2_2 = "images/Tiles/map2.2.png"
image map3_1 = "images/Tiles/map3.1.png"
image map3_2 = "images/Tiles/map3.2.png"
image map3_3 = "images/Tiles/map3.3.png"
image map4_1 = "images/Tiles/map4.1.png"
image map4_2 = "images/Tiles/map4.2.png"
image map4_3 = "images/Tiles/map4.3.png"
image map4_4 = "images/Tiles/map4.4.png"
image map5_1 = "images/Tiles/map5.1.png"
image map5_2 = "images/Tiles/map5.2.png"
image map5_3 = "images/Tiles/map5.3.png"
image map5_4 = "images/Tiles/map5.4.png"
image map6_1 = "images/Tiles/map6.1.png"
image map6_2 = "images/Tiles/map6.2.png"
image map6_3 = "images/Tiles/map6.3.png"
image map7_1 = "images/Tiles/map7.1.png"
image map7_2 = "images/Tiles/map7.2.png"
image map8 = "images/Tiles/map8.png"
image mapBlank = "images/Tiles/mapBlank" 


# backgrounds. I noticed the file names were quite long, so I condensed by removing the “BG” from each name when you call the file, and simplifying the longer names. I also removed any spaces. The first initial of each word is capital to help readability.


image Base = "images/Background/BG-base.png"
image BriarElement = "images/Background/BG-Briar Elemental Variant.png"
image Campfire = "images/Background/BG-Campfire.PNG"
image DeforestedStumps = "images/Background/BG-Deforested Stumps Variant.png"
image ElkCarcass = "images/Background/BG-ElkCarcass.png"
image FairySwarm = "images/Background/BG-FairySwarm.png"
image FlowerField = "images/Background/BG-FlowerField.png"
image HollowTree = "images/Background/BG-HollowTree.png"
image MudPatch = "images/Background/BG-MudPatch.png"
image MushroomPatch = "images/Background/BG-MushroomPatch.png"
image RagingRiver = "images/Background/BG-Raging River Variant.png"
image RainDroplets = "images/Background/BG-RainDroplets.png"
image SmallLake = "images/Background/BG-SmallLake.png"
image StrongWind = "images/Background/BG-StrongWind.png"
image Lake = "images/Background/BG-Lake.png"

define config.layeredimage_offer_screen = True




define config.layers = ["master", "Foreground", "transient", "Headshot", "screens", "overlay" ]








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
    #These if statements are using the variable Branch variables to confirm whether the player has completed this branch or not.
    #If they have, the game will not allow them to pick that route again.
    #That way there is no risk of the player repeating the same route over and over again.    
    "..."
    "\"Who are you?\""
    "A question that rings throughout your fleeting thoughts."
    "You were here. You were just here. And now..."
    "..."
    "You were doing something. What were you doing? Now you..."
    "Can't...remember..."
    "You...what kind of.....beast..."
    "...the Lake...get to..."
    "...all that's...left..."
    "...your Pack..."
    jump starting_choice

label starting_choice:
    #These if statements are using the variable Branch variables to confirm whether the player has completed this branch or not.
    #If they have, the game will not allow them to pick that route again.
    #That way there is no risk of the player repeating the same route over and over again. 
    menu:
        "Follow the Raccoon"  if RaccoonBranch:
            jump Choose_Raccoon
        "Follow the Bear" if BearBranch:
            jump Choose_Bear
        "Follow the Dragonfly" if DragonflyBranch:
            jump Choose_Dragonfly


#---------------------------------------------------
#--Branching narrative starts here and the player chooses which route
#---------------------------------------------------




#------------------------------------------
#-Start Raccoon Branch
#------------------------------------------
label Choose_Raccoon:


   "The Raccoon, a funny little fella who has a funny face"
   "Do not be fooled however, the Raccoon has great [[Agility]. Furthermore it carries the innate trait of {i} [[magic pocket]{/i}"


   "Choose the Raccoon?"
   menu:
       "Yes":
           jump Begin_Raccoon
       "No":
           jump starting_choice


label Begin_Raccoon:


    # Mark that the player has started the Raccoon branch
 
    


    # Tile 1


    "The forest hums softly in its slow awakening. Shafts of gold cut through the canopy, painting the moss in dancing patches of light."
    "The smell of wet bark and clover lingers in the air. Somewhere, a stream murmurs like a forgotten song."


    r "Mmm... another perfect day for heroics and snacks."


    "Raccoon stretches and yawns, then rolls onto their back, watching sunlight flicker between branches."


    r "...Had the weirdest dream last night... there was a lake. Big, shiny, like a mirror that swallowed the sky."
    "They pause, squinting at the treetops."
    r "I think something was waiting for me there."


    "They brush leaves from their fur and grin."


    r "Or maybe it was just me admiring my reflection again. Hard to tell sometimes."


    "They hop upright and take a few steps toward the clearing, humming tunelessly."


    r "Anyway, dream or not, sounds like destiny's calling! And if destiny's shiny, then even better."


    "They look around, tail flicking eagerly."


    r "Now... which way was that lake again?"
    scene map1 onlayer master
    menu:
        "Take upper route":
            $ MapNumber = 2.1
            jump rc_tile_2

        "Take lower route":
            $ MapNumber = 2.2
            jump rc_tile_2



    # Tile 2

label rc_tile_2:

    "[MapNumber]"

    "Further down, the ground softens to mud. A glint of silver flashes beneath the surface, half-buried like treasure waiting to be found."


    r "Oh-ho-ho! Jackpot! The forest rewards those with impeccable taste."


    "They crouch, eyes bright."


    r "Careful... slow... stealth mode."


    "They leap forward."


    "WHOOSH!"


    r "Wha-AHHH! No! This is NOT treasure! It's-ugh-it's... sticky! Gross!"


    "They thrash as thick resin threads stretch between their paws."


    r "Why do all my good ideas turn bad so quickly?"


    "They struggle, half-amused, half-frustrated."


    r "Okay, Raccoon. Think. Time to deploy your legendary training. Which you... definitely have."


    menu:
        "Use [[Agility] to twist free":
            "Raccoon twists, somersaults, and pops free with a dramatic spin."
            r "Ha! Elegant as always!"
        "Use [[Magic Pocket] to escape":
            "They dig into a small satchel tied to their fur, pulling out a spoon, a feather, and finally a shiny pebble."
            r "Aha! The magic pebble of... goo-dissolving? Let's find out!"
            "They tap the sap with the pebble; it melts away like sugar in tea."
            r "Magic!"


    "They stand, covered in flecks of mud and resin."


    r "I'm either the cleverest animal in the forest... or the dumbest."


    "They glance back at the sticky patch, where sunlight still glints off the sap."


    r "Still... that shine looked just like the one from my dream."


    "Their grin fades a little."


    r "Maybe not everything shiny wants to be found."
    if MapNumber == 2.1:
        scene map2_1 onlayer master 
    elif MapNumber == 2.2:
        scene map2_2 onlayer master
    menu:
        "Take upper route":
            if MapNumber == 2.1:
                $ MapNumber = 3.1
            else:
                $ MapNumber = 3.2
            jump rc_tile_3
        "Take lower route":
            if MapNumber == 2.1:
                $ MapNumber = 3.2
            else:
                $ MapNumber = 3.3
            jump rc_tile_3


    # Tile 3

label rc_tile_3:

    "The air smells sweeter as the forest opens again. Light plays on the leaves; each rustle feels like a whisper from something watching kindly, or curiously."


    r "Note to self: shiny equals sticky. Got it. I totally learned my lesson. Probably."


    "They act like a solider, marching proudly forward."


    r "Bet Bear would've told me to 'use my head before my tail.'"


    "They lower their voice, mimicking Bear."


    r "\"Raccoon, you can't solve everything with jokes.\""


    r "Counterpoint: jokes make everything better."


    "They chuckle, then sigh."


    r "But... maybe they're right. At least sometimes. I keep diving into things headfirst. One day that's gonna hurt someone else, not just me."


    if RunCount > 1:
        r "At least I'm starting to think before acting. That's progress, right? Baby steps. Stylish baby steps."

    if MapNumber == 3.1:
        scene map3_1 onlayer master
    elif MapNumber == 3.2:
        scene map3_2 onlayer master
    else:
        scene map3_3 onlayer master

    menu:
        "Take upper route":
            if MapNumber == 3.1:
                $ MapNumber = 4.1
            elif MapNumber == 3.2:
                $ MapNumber = 4.2
            else:
                $ MapNumber = 4.3
            jump rc_tile_4

        "Take lower route":
            if MapNumber == 3.1:
                $ MapNumber = 4.2
            elif MapNumber == 3.2:
                $ MapNumber = 4.3
            else:
                $ MapNumber = 4.4
            jump rc_tile_4



    # Tile 4 - choose companion pair
label rc_tile_4:
    "They stop, hearing a rustle in the underbrush."


    r "Hmm? Sounds like company."


    "They perk up, ears twitching with excitement."


    r "Finally! Maybe someone who appreciates my charm."

    "Shapes move in the greenery ahead. Familiar silhouettes step into the light."


    menu:
        "Travel with Turtle and Coyote":
            jump Raccoon_RouteA
        "Travel with Bear and Hummingbird":
            jump Raccoon_RouteB




# -----------------------------------------
# Route A - Turtle & Coyote
# -----------------------------------------
label Raccoon_RouteA:


    # Tile 4A


    "A mossy shell glints in the light; beside it, a blur of tan fur bounds through the bushes."


    c "Woah! Didn't expect to see you here, short stuff!"


    r "Short? Excuse you, this is called compact excellence."


    tl "You two arguing already? We just found each other."


    c "Not arguing! Just bonding aggressively."


    r "Exactly. That's how real friendships start."


    "Turtle sighs, stepping over a root with careful precision."


    tl "If you two keep making noise, every predator in the forest will know where we are."


    c "Good! Then they can come hang out too."


    r "See? Team spirit!"


    tl "Team idiocy..."


    r "Tomato, tomahto."


    "They share a laugh, except Turtle, who shakes their head fondly."


    r "So. You two on your way to the lake too?"


    tl "We're always on our way somewhere. Just hopefully not to our deaths."


    c "Don't say that! The forest is full of cool stuff! Maybe treasure! Maybe ghosts!"


    tl "That's not helping."


    r "Perfect. I like this dynamic already. Let's find out what shiny mistake waits for us next."

    if MapNumber == 4.1:
        scene map4_1 onlayer master
    elif MapNumber == 4.2:
        scene map4_2 onlayer master
    elif MapNumber == 4.3:
        scene map4_3 onlayer master
    elif MapNumber == 4.4:
        scene map4_4 onlayer master
    menu:
        "Take upper route":
            if MapNumber == 4.1:
                $ MapNumber = 5.1
            elif MapNumber == 4.2:
                $ MapNumber = 5.2
            elif MapNumber == 4.3:
                $ MapNumber = 5.3
            elif MapNumber == 4.4:
                $ MapNumber = 5.4
            jump rc_tile_5A

        "Take lower route" if MapNumber < 4.4:
            if MapNumber == 4.1:
                $ MapNumber = 5.2
            elif MapNumber == 4.2:
                $ MapNumber = 5.3
            elif MapNumber == 4.3:
                $ MapNumber = 5.4
            jump rc_tile_5A

    # Tile 5A

label rc_tile_5A:

    "The trio stops near a massive hollow tree whose center hums when they speak."


    c "Whoa, check this out!"


    r "Echo! Echo! Echooo!"


    "Their voice bounces back, slightly distorted."


    r "See? The forest loves my voice."


    tl "That... doesn't sound like just an echo."


    c "Maybe it's forest ghosts! Hi ghosts!"


    r "You're welcome for the jokes, by the way!"


    "The echo replies faintly, barely more than a breath."


    "\"Welcome...\""


    tl "Okay, that's not funny."


    r "Maybe it's just memory. Forests remember laughter too."


    c "Creepy but poetic."


    tl "Let's move before the memories start answering back."


    r "You're no fun."


    "They move on, laughter fading into the hollow's hum."

    if MapNumber == 5.1:
        scene map5_1 onlayer master
    elif MapNumber == 5.2:
        scene map5_2 onlayer master
    elif MapNumber == 5.3:
        scene map5_3 onlayer master
    elif MapNumber == 5.4:
        scene map5_4 onlayer master
    menu:
        "Take upper route" if MapNumber > 5.1:
            if MapNumber == 5.2:
                $ MapNumber = 6.1
            elif MapNumber == 5.3:
                $ MapNumber = 6.2
            elif MapNumber == 5.4:
                $ MapNumber = 6.3
            jump rc_tile_6A
        "Take lower route" if MapNumber < 5.4:
            if MapNumber == 5.1:
                $ MapNumber = 6.1
            elif MapNumber == 5.2:
                $ MapNumber = 6.2
            elif MapNumber == 5.3:
                $ MapNumber = 6.3
            jump rc_tile_6A
    # Tile 6A

label rc_tile_6A:

    "A roaring river cuts through the forest, water sparkling violently in moonlight."


    r "Finally! A natural water slide!"


    tl "Absolutely not, Raccoon."


    c "It does look fun..."


    tl "I take that back. Absolutely not, for both of you."


    menu:
        "Raccoon leads, using [[Agility] across the rocks":
            "Raccoon leaps from rock to rock, paws slipping on the spray but somehow keeping their balance."
        "Turtle leads, using [[Swimming] to steady the current":
            "Turtle slips into the water, steady as stone, letting the others use their shell as a moving bridge."
        "Coyote leads, using [[Scent] to find a calmer crossing":
            "Coyote lifts their nose, tracing the air until they find a narrower, calmer stretch of river to cross."


    "Midway, a wave almost knocks Raccoon off; Turtle shouts instructions while Coyote barks encouragement."


    r "Remind me to never underestimate physics again!"


    tl "Remind me to travel alone next time."


    c "But then who would bring the snacks?"


    "They all laugh as they reach the opposite shore, dripping but alive."

    if MapNumber == 6.1:
        scene map6_1 onlayer master
    elif MapNumber == 6.2:
        scene map6_2 onlayer master
    elif MapNumber == 6.3:
        scene map6_3 onlayer master
    menu:
        "Take upper route" if MapNumber > 6.1:
            if MapNumber == 6.2:
                $ MapNumber = 7.1
            elif MapNumber == 6.3:
                $ MapNumber = 7.2
            jump rc_tile_7A
        "Take lower route" if MapNumber < 6.3:
            if MapNumber == 6.1:
                $ MapNumber = 7.1
            elif MapNumber == 6.2:
                $ MapNumber = 7.2
            jump rc_tile_7A

    # Tile 7A

label rc_tile_7A:

    "Later, the Pack settles by a quiet stream. Fireflies drift like embers from another world."


    r "Finally, the perfect atmosphere for reflection... or snacks. Probably both."


    c "You always think with your stomach."


    tl "And yet we're alive, somehow."


    "Raccoon grins, piling twigs onto a bonfire."


    r "Alright, no moping tonight. We survived the sticky, the scary, and the soggy. We deserve a party."


    "They light the fire, sparks rising into the starlight. Someone laughs. Someone groans. But tonight, they are all together."


    r "Look around, folks. For once, the forest doesn't feel like it's judging us."


    tl "Probably won't last long. Give it time."


    r "Nah. Tonight it listens."


    "Raccoon starts humming, spinning clumsily around the fire. The others eventually join-awkwardly, reluctantly, sincerely."


    "The laughter feels alive. Even Turtle relaxes a little."


    r "You know... I think laughter's like light. Doesn't matter how dark the forest gets-it still finds a way through."

    if MapNumber == 7.1:
        scene map7_1 onlayer master
    elif MapNumber == 7.2:
        scene map7_2 onlayer master
    menu:
        "Take upper route" if MapNumber == 7.2:
            $ MapNumber = 8
            jump rc_tile_8A
        "Take lower route" if MapNumber == 7.1:
            $ MapNumber = 8
            jump rc_tile_8A

       # Tile 8A - Ending

label rc_tile_8A:
    "The Pack is able to navigate through the forest, following the faint pull of Turtle's [[Tide Memory] as it tugs them down the trail."
    "Before long, they emerge from the trees, and stand in front of a giant lake."


    r "So this is it."
    tl "I remember this place. There should be a lake somewhere up ahead."
    r "Feeling lucky enough to dive?"
    tl "No. This one's different."
    c "Different how? Looks like a standard lake to me."


    "They move closer to the water's edge, the air around them growing heavy and still."
    tl "Put me down at the shore, please."
    r "Yeah, give me a second."


    "Raccoon does as they're told and sets Turtle down near the waterline. Gentle waves lap at Turtle's shell as they close their eyes."
    tl "If I can just... remember the tides here..."


    "The water begins to ripple and change. Little waves form, then grow taller, crashing harder against the shore."
    r "That's not good!"
    c "Uh, guys? I don't think the lake likes us!"


    "A sudden wave surges forward, slamming into them and dragging all three off their feet."
    "Cold water closes over their heads as they're yanked out into the lake."


    "They kick and struggle, but the pull only grows stronger, like the whole lake is pouring downward beneath them."
    "The surface roils, swallowing their silhouettes until nothing is left but circling ripples on the dark water."

    $ Rsighting += 1
    $ Csighting += 1
    $ TLsighting += 1
    $ RunCount += 1
    $ RaccoonBranch = False
    scene black with fade


    jump ending






# -----------------------------------------
# Route B - Bear & Hummingbird
# -----------------------------------------
label Raccoon_RouteB:


    # Tile 4B


    "A deep rumble echoes from the trees, followed by a high-pitched complaint."


    hb "I swear, Bear, if we walk ten more steps without finding food, I'm going to combust."


    b "You say that every ten steps."


    r "Hey! Speaking of combusting-look who it is!"


    hb "Oh great. The forest comedian."


    r "You wound me, birdie. I bring joy and chaos in equal measure."


    b "Mostly chaos."


    r "And yet, you're smiling inside. I can tell."


    b "You can't."


    r "I can."


    "They walk together, the forest darkening toward dusk."


    hb "We're wasting daylight on jokes. Typical."


    r "Correction: we're using daylight creatively."


    b "You mean wasting."


    r "Semantics!"


    "Bear grumbles. Hummingbird mutters under their breath. Raccoon just laughs."


    r "Alright, grumpy squad, I'll lead. Someone's gotta bring personality to this trio."


    hb "We're doomed."


    if MapNumber == 4.1:
        scene map4_1 onlayer master
    elif MapNumber == 4.2:
        scene map4_2 onlayer master
    elif MapNumber == 4.3:
        scene map4_3 onlayer master
    elif MapNumber == 4.4:
        scene map4_4 onlayer master
    menu:
        "Take upper route":
            if MapNumber == 4.1:
                $ MapNumber = 5.1
            elif MapNumber == 4.2:
                $ MapNumber = 5.2
            elif MapNumber == 4.3:
                $ MapNumber = 5.3
            elif MapNumber == 4.4:
                $ MapNumber = 5.4
            jump rc_tile_5B

        "Take lower route" if MapNumber < 4.4:
            if MapNumber == 4.1:
                $ MapNumber = 5.2
            elif MapNumber == 4.2:
                $ MapNumber = 5.3
            elif MapNumber == 4.3:
                $ MapNumber = 5.4
            jump rc_tile_5B
    # Tile 5B

label rc_tile_5B:
    "Night falls. The forest glows faintly blue from clusters of mushrooms lighting the path."


    hb "Fantastic. Bioluminescent death traps. My favorite."


    b "They're just mushrooms."


    hb "You say that until they sprout teeth."


    r "If they do, at least we'll see them coming!"


    "The light reflects in Raccoon's eyes; they look almost dreamlike."


    r "You know, it's kinda pretty. Like the ground decided to have its own stars."


    b "Pretty doesn't mean safe."


    r "Safe doesn't mean interesting."


    hb "You're both exhausting."


    "They continue walking, light flickering underfoot. For a moment, all three are quiet. Then Raccoon hums a tune, breaking the tension."


    r "If I die glowing, make sure I look fabulous."


    hb "You already look ridiculous."


    r "Close enough."

    if MapNumber == 5.1:
        scene map5_1 onlayer master
    elif MapNumber == 5.2:
        scene map5_2 onlayer master
    elif MapNumber == 5.3:
        scene map5_3 onlayer master
    elif MapNumber == 5.4:
        scene map5_4 onlayer master
    menu:
        "Take upper route" if MapNumber > 5.1:
            if MapNumber == 5.2:
                $ MapNumber = 6.1
            elif MapNumber == 5.3:
                $ MapNumber = 6.2
            elif MapNumber == 5.4:
                $ MapNumber = 6.3
            jump rc_tile_6B
        "Take lower route" if MapNumber < 5.4:
            if MapNumber == 5.1:
                $ MapNumber = 6.1
            elif MapNumber == 5.2:
                $ MapNumber = 6.2
            elif MapNumber == 5.3:
                $ MapNumber = 6.3
            jump rc_tile_6B
    # Tile 6B

label rc_tile_6B:
    "A meadow of luminous flowers sways under a faint mist."


    hb "Pretty. Probably lethal."


    b "Stay back. The smell's off."


    r "Oh come on, they're just flowers. Friendly ones. Right?"


    b "No."


    hb "Definitely not."


    "Raccoon pulls a scrap of cloth from their magic pocket and ties it around their face."


    r "Mask time! Safety first, fashion second."


    hb "You're ridiculous."


    r "Ridiculously prepared."


    b "Hummingbird, clear the air with your wind."


    "Wind surges through the meadow; the pollen scatters and the air clears [[Wind Gale]."


    r "See? Teamwork! We're unstoppable."


    hb "Until the next stupid decision."


    b "At least they're learning."


    r "Was that a compliment?"


    b "Don't push it."

    if MapNumber == 6.1:
        scene map6_1 onlayer master
    elif MapNumber == 6.2:
        scene map6_2 onlayer master
    elif MapNumber == 6.3:
        scene map6_3 onlayer master
    menu:
        "Take upper route" if MapNumber > 6.1:
            if MapNumber == 6.2:
                $ MapNumber = 7.1
            elif MapNumber == 6.3:
                $ MapNumber = 7.2
            jump rc_tile_7B
        "Take lower route" if MapNumber < 6.3:
            if MapNumber == 6.1:
                $ MapNumber = 7.1
            elif MapNumber == 6.2:
                $ MapNumber = 7.2
            jump rc_tile_7B
    # Tile 7B

label rc_tile_7B:
    "Later, the Pack settles by a quiet stream. Fireflies drift like embers from another world."


    r "Finally, the perfect atmosphere for reflection... or snacks. Probably both."


    hb "Barely survived getting here."


    b "Could be worse."


    "Raccoon grins, piling twigs onto a bonfire."


    r "Alright, no moping tonight. We survived the sticky, the scary, and the soggy. We deserve a party."


    "They light the fire, sparks rising into the starlight. Someone laughs. Someone groans. But tonight, they're all together."


    r "Look around, folks. For once, the forest doesn't feel like it's judging us."


    b "Maybe it's just sizing us up."


    r "Nah. Tonight it listens."


    "Raccoon starts humming, spinning clumsily around the fire. The others eventually join-awkwardly, reluctantly, sincerely."


    "The laughter feels alive. Even Hummingbird smiles faintly. Even Bear relaxes."


    r "You know... I think laughter's like light. Doesn't matter how dark the forest gets-it still finds a way through."

    if MapNumber == 7.1:
        scene map7_1 onlayer master
    elif MapNumber == 7.2:
        scene map7_2 onlayer master
    menu:
        "Take upper route" if MapNumber == 7.2:
            $ MapNumber = 8
            jump rc_tile_8B
        "Take lower route" if MapNumber == 7.1:
            $ MapNumber = 8
            jump rc_tile_8B

           # Tile 8B - Ending

label rc_tile_8B:
    "The Pack is able to navigate through the forest using Bear's [[Pathsense] string."
    "The thread guides them through the last stretch of trees until the forest opens up around a wide, shimmering lake."


    r "We actually made it."
    hb "Yeah. And it feels wrong."
    b "Stay close. We don't know what will happen here."


    "They all move closer to the water's edge, stopping where damp earth gives way to sand."
    hb "Whatever comes next, I'd at least like to not drown."
    r "I'll do my best to keep us all fabulously afloat."


    "Bear wades in first, testing the depth. Raccoon follows, splashing nervously, while Hummingbird hovers just above the surface."
    "For a moment, the water around them is strangely calm."


    "Then they feel it. The water underneath them slowly, surely being pulled downward."
    hb "Do you feel that?"
    r "I'm trying, but I'm being pulled in! Bear, I think we're-"


    "The pull becomes a sudden, violent drag. The lake's surface warps, funneling everything toward its dark center."
    b "Get out of the water!"


    "They fight to swim back, but every stroke only drags them deeper into the invisible current."
    "One by one, they're swallowed by the lake, their shapes vanishing beneath the churning water."

    $ Rsighting += 1
    $ Bsighting += 1
    $ HBsighting += 1
    $ RunCount += 1
    $ RaccoonBranch = False

    scene black with fade


    jump ending


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

    b "I can't tell if there is going to be a storm approaching or if there is a separate force that is manipulating the wind? It does not matter."
    b "I need to keep following this weaving trail of string that I see."

    if RunCount <= 1:
        b "The string carries a soft blue hue, if I wack it with my paw it simply turns to air and then comes back. I don't see anything it is tied to either."
        b "My body wants to follow it by instinct, so I let it do so."
        b "No other strings have appeared since I started following this blue string."
        b " I'm not even sure if other animals see it as well."

    if RunCount >= 2:
        b "I gotta keep moving, this string is the key to finding them. Once I find them we need to find that lake and end this once and for all."


    " N: The bear follows the blue string further into the forest. Will there be a reward, or misery at the end?"
    $ Bsighting += 1
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

    b "OW! HEY STOP THAT! CRAP!"

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
    
    jump Bear_Tile_3
   

#---------------------------
#--End Bear Tile 2
#--------------------------


#---------------------------
#--Begin Bear Tile 3
#--------------------------
label Bear_Tile_3:
    "The day flew by instantly as the Bear lay dormant on the forest floor. Nothing disturbed them. Nothing appeared around them. Only the trees watched. The trees said nothing but their eyes and judgement lay on the Bear."
    "Within the confines of the Bear's mind they played the encounter with the pixies multiple times. Trying to decipher what could have been done. What could be done better? Am I equipped to fight magical creatures?"
    "What if they fly? These questions passed through the Bear's mind."
    
    b " Fear is my greatest enemy. If I cannot control the fear that takes over in those moments then my judgement is not sound. I have never encountered or experienced being attacked by pixies before."

    if RunCount is 0:
        b "Why did the string lead me through such a dangerous area? Then it helped me in my state of panic. What does this string know that I do not?"

        "The Bear felt unsettled by the idea that this magic string they trust with their life may have a mind of its own."

    if RunCount is 1:
        b " If I took my time like last time, maybe I would have realized that the dark forest was not a safe choice. "

        " No, then I would lose the string. I needed to follow the string."

    if RunCount is 2:
        b "The string knows best. I just need to trust it, but if it's going to put me through a gauntlet like that, I may as well deviate off course to not deal with it."
        b "The string always reappears to me later on so it would simply be an issue of losing time."

    b "This place is changing in mysterious ways. The magical entities who control this forest are reacting to something, and they are definitely not happy. I need to find the source. I need answers to why I see this string."

    b "I need to find a clue. Something that will even give me a slight hint as to what is going on with me and this forest."

    b "What am I doing right now? Am I still alive? I'm not sure... I feel alive. I feel weightless, empty even. Am I still in the pixie patch or has some other foul beast decided to prey on me."

# Happens for the first and second appearance.
    if RunCount <= 1:
        b "This space is not normal. There were no animals. No sense of life. It felt cursed even. No, not cursed, protected."

        b "Those pixies seemed rather adamant about not letting me leave this place, but they said I was special. What makes me so special that I deserve to be treated so horribly?"

        b "Could they see the string? Was that why they called me special? No, they didn't even bring it up. I want answers, but who will have them?"

#-----------
#3rd Run interaction happens here
#------------
    if RunCount is 2:
        t " Lost in thought is the phrase you are looking for stranger."

        b " Who's there?"

        t " Do not worry, I am communicating with you telepathically."

        b " That did not answer my question. Who are you?"

        t " Still stubborn I see."

        b " The one who is stubborn is you."

        t " Stubborn? Maybe. I like rooted better."

        b " Pardon? Rooted? Are you a plant? So even the plants are magical here?"

        t " Well, in this area of the forest, yes. The pixies tend to these woods. The same pixies you scared off."

        b " You here to cast divine judgement?"

        t " I do not intend to be hostile with you. You seemed very deep in thought so I wished to converse about the dilemma you are facing."

        b " You've been reading my mind?"

        t "  Yes."

        b " Great, a plant that can read and talk to me through my mind."

        t " Time is ticking, I do not have all night. You wish for a clue to the mystery correct?"

        b " Yes."

        t " You hold one of the answers to that very mystery. The string you speak of is simply a manifestation of your power. Your connection to magic is not coincidental. It is a gift granted to you by them."

        b " Who is them?"

        t " The spirit of the forest. They are the one who brought you here. They are the one who you should have listened to from the start..."

        b "What do you mean listened to? I haven't heard a thing from this spirit of the forest you speak of. Hey! Plant! Answer me!"

    "The bear lay there in their mind contemplating what they could do now. Silence permeated the space. The night was quiet in the shaded forest. As it always was."
    jump Bear_Tile4

#---------------------------
#--End Bear Tile 3
#--------------------------

#---------------------------
#--Begin Bear Tile 4
#--------------------------
label Bear_Tile4:
    " The Bear finally awoke from their slumber. Time was a blur."

    b "How many days has it been since I passed out?"

    b " The bear could feel cold patches on its body from being attacked by the pixies. Now was not the time to dwell on the discomfort."
    b " The Bear still has a goal in front of them, follow the string and figure out where it ends."

    " So did the Bear keep following the mysterious blue string out of the shaded forest."

    " The tree line slowly cleared up and color slowly returned to the Bear's eyes as it made it out of the shaded forest. The Bear was happy to have made it out in some form."
    " The string was acting strange, it was cutting itself and reforming, almost as if it was not sure what to do."

    if RunCount is 0:
        " The bear stood there perplexed. It had never seen the yarn do this before"

        b " What the heck are you doing now?"

        " The bear swatted at the ethereal yarn. Nothing happened, the paw simply flies through it. The Bear stood there for a second, and thought to itself."

        b "I think I might as well take a short break. I have no idea what this thing is doing and I'm curious if it will do something after a while."

    "The Bear lay there for some time watching the yearn destroy and meld itself together. It was mesmerizing and very hypnotizing to watch."
    "So much so that the Bear did not realize there were voices getting closer and closer"

#------------------
#Player will Choose their duo of animals.
#-------------------
    menu: 
        "Meet Hummingbird and Dragonfly?":
            jump BHD_Tile4
        "Meet Turtle and Raccoon?":
            jump BTR_Tile4


#---------------------
#- Hummingbird/Dragonfly route Tile4
#-------------------
label BHD_Tile4:
    hb " You don't know anything Fly. You mean to tell me we are gonna meet the Bear at some point. HAH! In your dreams."
    
    df " We aren't dreaming, Bird; my future sight doesn't lie. I can feel it! We have to be nearing that point in the future I saw!"
   
    b " Huh? What the? Oh no. No, no, no. Ughhhh. Is that annoying bird with me again? The Dragonfly is tolerable, but that damn Hummingbird makes me want to tear my ears off. The Bear thought to themself."
    " The bear got up and wandered toward the voices of the doubtful Hummingbird and confident Dragonfly. The Dragonfly quickly sensed the presence of something approaching the duo and focused on it."
   
    df " See!? I told you."
    
    hb " ... Crap."
    
    "The flying duo flew towards the Bear. "
    
    b " So I'm stuck with you two this time? Not a word out of your depressed beak, bird. Dragonfly, pleasure seeing you again."
    
    df " Likewise. Do you have an idea of where we are going?"
    
    b " Unfortunately, no. "
    
    df " Hmm. Then let us wander forward. I shall... Oh dear, are you okay?"
    
    b " Don't worry about it; I had a run-in with some hostile magic creatures a while back."
    
    df " Those marks are bad! You could get an infection from them."
    
    hb " If they did, they would already be dead from blood loss. Might be-"
    
    "The Bear shoots a glance at the Bird. The bird mumbled the rest under its beak."
    
    b " Mind leading the way, Dragon?"
   
    df " Certainly! Follow me."
    
    "So the pack was united. What mysteries would the trio encounter next?"
    #Intentionally delaying it till the end of the tile in case the player decides to back out from the decision
    $ HBighting += 1
    $ DFsighting += 1
    
    jump BHD_Tile5


#---------------------
#- Turtle/Raccoon route Tile4
#-------------------
label BTR_Tile4:
    tl "Please let me go! This is absurdly dangerous!"
   
    r "Oh, c'mon, we've done this countless times already, and nothing has happened."
    
    tl "You have literally dropped me over 5 times because you tried to run on 2 feet! You can't do that!"
   
    r "Says who? All you gotta do is stay tucked in your shell, and you'll be fine. Oof!"
    
    " As if on cue, the Raccoon not paying attention, ran straight into the Bear, startling them and dropping Turtle."
   
    b " HEY!"
   
    tl " AAAAAAAGHHH! I TOLD YOU NOT TO DO IT! WE'RE GONNA DIE NOW!"
    
    r " Humph. Owww... Why does everyone gotta be so loud?"
    
    " The Bear got into an attack stance on instinct. They stared down at the rather gullible Raccoon and absolutely terrified Turtle that was flipped over."
    
    b " Oh. It's you two."
    
    " The Bear proceeded to flip the turtle over and push the Raccoon on its back."
    
    r " Hey! Not cool, man."
    
    tl " Huh? Oh, Bear! I am so glad to see you. Please keep me away from this troublemaker who puts me in danger constantly."
    
    b " I think it's funny if you ask me."

    tl " What do you mean it's funny? My life is at stake here."

    r " You make no sense, Bear. So what have you been up to? Ah... Fighting, I see."
   
    b " It's a long story, but I'm alive."
    
    r " You look like you walked into 5 separate traps, got stuck in all 5, and somehow got out of each one."
   
    b  " You could say that."
    
    tl " Yes, nice chatter and all, but can you please put me on your back? I prefer not being in the clutches of that gremlin."
    
    b " Raccoon, you mind hoisting the Turtle onto my back?"
   
    r " Sure, and that's rude after how far I've carried you?"
   
    tl " I think it is justified. You are a living hazard to my existence."
    
    " With the trio united, they would begin to chatter and almost act in a family manner."
    " They would soon begin traveling once more after settling on a direction to roam in."
    $ TLsighting += 1
    $ Rsighting += 1
    jump BTR_Tile5

#---------------------------
#--End Bear Tile 4
#--------------------------

#---------------------------
#--Begin Bear Tile 5
#--------------------------

#---------------------
#- Hummingbird/Dragonfly route Tile5
#-------------------
label BHD_Tile5:
    " The Pack wandered aimlessly for some time; Bear's magic string would appear from time to time only to disintegrate after a couple of minutes."
   
    df "You seem rather disgruntled? What is on your mind?"
   
    b " My ability is not working. I can't get a clear idea of where this string wants me to go."
    
    df " That is annoying."
    " The Dragonfly lands on the Bear's head, and its eyes shine under the light."
    b "Got any new neat tricks you can pull off?"
    df "Nope, I can still only see into the future. It's not always clear, but it is useful. Currently one of the futures seems especially odd."
    b "That is pretty useful."
    " The Hummingbird returned to the pack after foraging for some nectar and landed on a nearby tree facing the duo."
    b "Speak, bird. What did you see on your trip for food?"
    hb "I'm not a peon, you overgrown death machine. Nothing strange. I found a rabbit if you are feeling hungry. Doubt you'll find it though; it probably ran off when it heard me."
    
    " Fly up ahead and scout. See if you can find anything else."
    " The Hummingbird stared down at the Bear with a level of contempt and disrespect. They did not want to listen to the Bear's command, but they obliged as they had nothing better to do. It was better this way."
    " Neither enjoyed each other's company. The Hummingbird left the branch quietly and zoomed far off ahead."
    df " You know I can be a mediator for you two?"
    b " That bird has issues we may never understand. You only bring out the worst in them, Dragon."
    df " I doubt it."
    "Some time passes as the Bear and Dragonfly catch up to Hummingbird"
    b "Hey Bird, where have... You... Been..."
    df "Oh my goodness."
    hb "..."


# Change scene to stump forest
    "The Pack gazed over the destitute field of tall grass, tree stumps, and dead trees. It was dead."
    " Nothing has entered this area since I found it. It appalls me."
    df "Surely some rats or small rodents who live in tall grass are in there? If that were the case, why is the grass still growing?"
    b "Grass grows where it pleases; if not kept in check, it will consume everything in a sea of green. Dragon, mind gazing into the future?"
    " The dragonfly used [[future sight]."
    df "This is the odd future I spoke of. It was all green. It all makes sense now."
    hb "You saw this, and you didn't say a word? You have arguably the strongest ability we know of, and you can't decipher Jack?"
    b "Silence."

    menu:
        "Enter the stump forest?":
            jump Stump_forest
        "Avoid the stump forest?":
            jump Detour1

#------
#-Enter Stump forest
#-----
label Stump_forest:
    b " There should be nothing in there, correct?"
    hb " Oh hell no. I am NOT going through there. If there are no flowers in sight, I am dead. Go through there, and you ain't seeing me until you get out."
    b " Up for something to keep us on edge, Dragon?"
    df " I can't say I am. Especially not this." 
    b " If we intend to follow this direction, the fastest way is to cut through."
    hb " I'm out; if you want to walk through the dead zone, that's all you. I'll probably remember you if you die."
    df "I think I am also going to sit this one out. I don't like the feel of that area. Also, I don't think there are many things to eat there either."
    b "Very well. Stay safe and wait for me. I'll be over there hopefully by nightfall."
    df "Don't die. That place is a living tomb."
    " The Pack split up. Hummingbird and Dragonfly flew across the perimeter of the stump forest while the Bear crossed through."
    "It was an interesting walk for the Bear. The grass was almost as tall as them."
    b "For the grass to grow to this height means the deer and other herbivores fear this place still. Loggers, I believe, are what the beavers call them. Humans who cut a great amount of trees with creatures of metal."
    b "Do they truly realize the effects they have on this forest by doing this? Do they know it never recovered?"
    "The Bear could feel an eerie energy emanating from the stumps. It wasn't directly aimed at them, but it felt malicious towards the ones who cut them."
    " The night drew on, and finally the Bear crossed the stump forest."
    hb "Oh, you're still alive?"
    b "Miss me that much, Bird? I thought all you knew was pain and sorrow."
    hb "Haha. Don't get much of it after waiting a long time to see you cross that cursed place. Enjoy your little walk through that cemetery?"
    b "Partially. Helped clear my mind from how quiet it was, but it also made me worry."
    hb "Yeah, that's nice. Hey Fly!"
    df "Huh? Wha?"
    hb "Bear's back, let's go set up camp."
    df "Oh, sure."
    "The Pack would now set up camp for the night after reuniting with Bear. The stump forest would lie etched into their mind that night."
    jump BHD_Tile6

#----------------
#Avoid stump forest
#----------------
label Detour1:
    b " Let's walk around. I agree; this place gives me the creeps."
    df " Who? Who would do this?"
    b " Humans, I believe. They aren't something you reason with. They take what they want and slaughter us if we fight back."
    hb " Easy for you to say, big guy. You can actually fight them. Us little folk only run for our lives."

    " The pack began walking around. It took much longer than expected to get around the stump forest. The pack set up camp some distance away from the stumps." 
    hb " You think the ghosts of the dead animals still roam that place?"
    b "Shut it."
    hb "It's a valid question. We got all sorts of crazy monsters and creatures here. Why not go see some dead animals?"
    b "I'll send you to greet them if you don't shut up."
    hb "Might be a better choice than dealing with the cutthroat vibes that place gives. We aren't even near it, and I feel like something is watching us."
    b "You never shut up, do you? How about you go look for these ghosts? You seem so scared, yet so excited to talk about them when safe."
    hb "Nah, I'm feeling a bit sleepy. It felt like a good story to keep us alert."
    b "You're a coward."

    "The Pack slept through the night, yet they never shook the feeling something was watching them. Bear was on guard duty for part of the night, followed by Dragonfly and then Hummingbird."
    "They survived another night and began moving around the stumps once more."

    jump BHD_Tile6
#---------------------
#- Turtle/Raccoon route Tile5
#-------------------
label BTR_Tile5:
    " The Pack slept through the night, yet they never shook the feeling something was watching them. Bear was on guard duty for part of the night." 
    " The Pack wandered aimlessly for some time; Bear's [[path sensing] would appear from time to time only to dissipate after a couple of minutes."
    b " Hmm. This is annoying."
    r " What is on your mind ya big oaf?"
    b " My ability is not cooperating. I can see this string, and it leads me to different places, but it hasn't been consistent lately."
    r " That's pretty unfortunate. Turtle, can't you do something like that?"
    tl " No. I can't do anything like that."
    r " Really? I thought it was similar?"
    tl " You really need to listen to Raccoon. I explained it 3 times, and every time you ended up reaching into that magic pocket of yours for a snack."
    r " OOO! Great idea. Let's have a snack break."
    tl " I regret having this conversation. Bear, would you like a refresher on what my ability is?"
    b "Yes, go on. Raccoon, keep up now; it isn't time for eating."
    tl "It's a bit complicated, but I can recall past events that have happened in different locations."
    "So let's say right now, I can use my skill to see what has happened here, and I may possibly see what animals have passed by here."
    tl "Another ability is I can grow my shell to create a giant wall."
    r "Hey, do you want some berries? Said the Raccoon with its mouth full."
    b "No."
    tl "What kind?"
    r "Red."
    tl "Gimme."
    "While the Raccoon mounted the Bear's back to feed the Turtle, the Bear stopped. The Bear was gazing upon a lake."
    "The water looked serene on the surface, but as the Bear looked into the depths, it became increasingly dark very quickly."
    " At the bottom in the darkness, the Bear could see some sort of flickering light. It seemed to be moving rather quickly. Is it a fish?" 
    b "Hey, you two, take a look at this lake."
    r "What's up? Woah, it's dark, dark, and it's still daytime."
    tl "A magic lake, most likely?"
    b "Most definitely."
    r "Turtle, isn't this your domain? How about you use your ability and see what's up with the lake?"
    tl "I don't think it's worth spending the time on something like this. Especially considering only I can go that deep underwater and can see."

    menu:
        "Convince Turtle?":
            jump Convince_Turtle
        "Stand with Turtle?":
            jump Defend_Turtle

#--------------
#-Convince Turtle route
#--------------
label Convince_Turtle:
    b "You're getting ahead of yourself, Turtle. Raccoon is wrong to send you in, but I think it would be a good idea to at least scan why it is this way."
    tl "Oh... You're right, you're right. Okay, let me get off then and bathe in the water; that will help me deepen the connection for my ability to work better."
    
    "After unmounting from Bear, the Turtle was placed in the water and floated there in place. The Turtle closed its eyes, and the water began to vibrate around them."
    "A [[tidal memory] was forming; it was a rather beautiful sight, except for the fact that Raccoon was washing their hands while doing this, which became a memory that Turtle saw."
    "After about a minute, the vibration stopped and the turtle swam out of the water."
   
    tl "You have to be a wild animal."
    r "I mean, I am."
    tl "Why did you think it was a great idea to clean your hands while I was doing that?"
    r "Cause they're dirty? Why else?"
    tl "Jeez. You are something else, Raccoon. Anyways, this lake is definitely of magical origin."
    b "How so?"
    tl "There seemed to be a battle between two elemental spirits in this area; their battle was so intense it left a crater that would later catch water with time. This lake is that very crater."
    tl "What exists at the bottom of this crater are not fish, but wild spirits who grow in the darkness. They are currently harmless in this state, but I wouldn't trust going in regardless."
    tl "The water has a sort of heaviness from the concentration of magic energy being released by the spirits. It's making me dizzy."
    b "Very well."
    r "So what would happen if I drank the wat-"
    "NO! Said both Turtle and Bear."
    jump BTR_Tile6




#------------
#-Defend Turtle Route
#--------------
label Defend_Turtle:

    b " You are being a pushy Raccoon."
    r " I mean, not really? They are an aquatic creature, so I feel like they have a better shot at doing something here than anyone else."
    tl " I'm not diving into a pitch-black lake that has twinkling lights at the bottom."
    r " But what if it's buried treasure?"
    tl " We don't need treasure."
    r " I can store it with my magic pocket; it's fine."
    " The Bear understood quickly how Raccoon was deciding for the uncomfortable Turtle, so they decided to intervene more."
    " It's not a matter of yes or no, Raccoon. We can't see what is down there. What if it isn't a treasure? Then what do we do?"
    r "Uh... I don't know..."
    b "Exactly, we can't because we can't swim enough or even see that well in dark water."
    tl "Personally I am not feeling like diving into the spooky lake. So, I'll pass on that."
    r "I thought it was a good idea..."
    " The Raccoon felt sad that their idea was turned down. The Bear was not worried too much by the Raccoon's reaction, but they did notice the slouch in their walk was more droopy."
    b " Make a more stable plan next time. That will get the vote of Turtle."
    r " Huh? Oh, sure."
    " The Pack made their way around the lake and ventured forward once again into the forest."
    jump BTR_Tile6

#---------------------------
#--End Bear Tile 5
#--------------------------


#---------------------------
#--Begin Bear Tile 6
#--------------------------


#----
# BHD Tile 6 route
#----
label BHD_Tile6:
    df " Oh dear. This is not good."
    
    b " What's wrong?"
    
    df " My [[foresight] detects a storm coming. And this one is not going to be nice to anyone or anything."
    b " Does your foresight give you an estimate of the time it will take to reach us?"
    df " No, it doesn't. It's all just a premonition with an unknown time frame."
    hb " Even if we did have time, it's not like we are anywhere near some sort of shelter to speak of. Plus, having a time frame for the Fly's abilities would be hell."
    b " You see time as a constant hell bird. I see it as convenient information to have. Change your perspective, and it will be much easier to digest."
    b " Enough chit-chat; both of you start scouting the area. We need to find shelter now!"
    df " Roger that!"
    hb " If you don't find me, presume I'm hiding in a tree."
    " The Pack split up quickly in search of some form of shelter. The dark clouds quickly rolled into the forest and brought with them a wicked storm."
    " Lightning began striking the forest, wind speeds began rising high, and the rain was more typhoon-like."
    df " AHHHHHH!"
    hb " WE'RE GONNA DIE!"
    b " Hold onto me! I think I see a cliff face up ahead."
    hb " Please, if there is a higher power, make me something other than a Hummingbird; please let me be a bit bigger. I will take a sparrow."
    hb " I just don't want to be suffering from acute starvation every few hours. It's a simple ask, really."
    b " Enough with the prayers! If you can see, look for something that looks like a cave or shelter."
    df " Left! Left! I see an opening!"
    " The Bear lunged towards the hole in the cliff. Fortunately, it was big enough to fit all of them."
    "{i}BOOM!{/i} the lighting responded. The storm kept raging relentlessly. Everything in its path was suffering greatly."
    b " Are you two alright?"
    df " I think so?"
    hb " I felt like my body almost got torn off of my legs by the wind."
    b " We will stay here till the storm settles."
    " The storm did not pass by so easily. Hours passed, and to no avail, it had yet to pass. This storm would last a full day."
    b " Bird. Are you sure you can survive a full day without flowers?"
    hb " Yeah... So long as I ain't flying, I probably won't die."
    df " I think he is dying of starvation."
    b "{i}sigh{/i} I'll be back."
    " The Pack rested in the cave for a full night. Only after sunrise did the storm settle down. The forest was in shambles. "
    " Fallen trees, overflowing rivers, mudslides, and landslides littered the area."
    b " This storm really did a number on the forest. "
    hb " Hey! I can get a decent view now thanks to the fallen trees! I can see things, kind of."
    b " Do you see any way for me around these giant trees?"
    hb " Just break them. You ain't making it around."
    b " I'll just climb them instead at the cleaner spots."
    " The fallen trees had posed a greater problem to the Bear who was on the ground, compared to their flying allies."
    df " I'm back. It seems like there are tons of trees that were knocked down by the storm. Do you think you have the energy to move around or climb some trees?"
    b " Lead me; I think I will manage for the time being."
    " The Pack would enter a rather interesting performative act; the two flying animals would relay very conflicting messages while the Bear would attempt to climb, walk around, or crawl under different types of debris."
    " The process did not take very long, but it did test the patience of all 3 members."
    jump BHD_Tile7

#----
# BTR Tile 6 route
#----
label BTR_Tile6:
    r "You ever wonder if other animals have these weird powers we have?"
    "Yes, Turtle and Bear replied."
    r "It feels like every ability is tied to us as animals. Turtles got that weird shell thing with the memory thing. Then you got a magic string."
    r "I think I am not right about the power thing."
    tl "It may just be related to us as individuals?"
    r "Like every other raccoon has a separate ability from mine?"
    tl "Yes."
    r "That would be pretty cool actually. Imagine an army of Raccoons each with their own unique ability."
    tl "At that point it's just power in numbers for who has more powers."
    "The wind picked up from behind the Pack. Bear stopped momentarily. They felt the whiff of something odd. Something out of place."
    "{i}BOOM!{/i} A nearby tree snapped from the impact of the bullet piercing it."
    menu:
        "Run":
            jump ChaseTile6

label ChaseTile6:
    b "MOVE! NOW!"
    "{i}BOOM!{/i} Another bullet fired, landing near the Raccoons legs."
    r "OH MY GOD! That almost hit me!"
    b " Don't speak! RUN!"
    tl "Oh god! Oh god! Oh god! This can't be happening. This can't be happening."
    b "Turtle, grab on; you're slipping!"
    "The turtle in a panic used [[tidal memory] to scan the memories of this area of the forest"

    tl "Crap, we made a mistake; my ability tells me we stumbled on human hunting ground!"
    r "That's a thing?!"
    b "Always has been! I've seen them before! Those giant sticks shoot fire! Do not get hit by them!"
    "Right on cue, another {i}BOOM!{/i} followed by a whistling sound seared the side of Bear's face."
    b "URGHH!"
    tl "Ah Crap, crap, crap. Not good Bear got hit. What do we do? Do I bring up my shell?"
    r "Friend, that magic is piercing into the trees. Imagine what it will do to your shell."
    tl "Right! Right. AHH! What do we do here?!"
    b "Hide and run! AHHH, damn it!"
    tl "Did they get your eye?"
    b "No, I can see, but I can taste blood in my mouth. Turtle, what direction leads us out of the hunting ground?"
    tl "Uh, uh, uh. It doesn't matter at this point. Just run straight!"
    "The group advanced at quick speeds as far from the hunter as possible."
    b " I think we lost them."

    "The Turtle activated [[Tidal memory] on the land"
    tl "Hmmm... Yes. Oh, thank goodness. I can see the footprints; they stopped following us some time ago."
    r "Here, I might have something for the bleeding." 
    "Raccoon scavenged through the magic pocket for some leaves." 
    r "Here, these flowers and leaves should help."
    b "What are they for?"
    r "It's my special mix of herbs and spices."
    "Raccoon began to dab the assortment of flowers and leaves against Bear's face." 
    b "Ow! That stings."
    r "Oh good! It's working then."
    b "No. Not good, that stuff hurts. Keep it away."
    r "Believe in the herbs and spices, Bear; they will cure all your problems." 
    b "I refuse if they are going to hurt me."
    tl "Going to sour the mood here, but I am detecting sudden movement of the hunter moving once again. We need to move."
    r "You are saved from the herbs and spices this time, but you will not be once we get out of this."
    b "Screw your damn herbs and spices!"
    "The Pack finished their discourse and began running once more away from the hunter's sight."
    jump BTR_Tile7

#---------------------------
#--End Bear Tile 6
#--------------------------

#---------------------------
#--Begin Bear Tile 7
#--------------------------

#------------
#- BHD Tile 7 route
#-------
label BHD_Tile7:
    "The night was dark, emptier than a drained ocean. In the midst of this darkness lay an orb of light. A beacon for all who cared to see."
    b "Bird, what can you do?"
    hb "I can fly, I can eat from flowers, and I can channel a gust of wind to blow a leaf."
    df " They can do better than blow a gust of wind. They just tend... to not be able to do much more than that. What, it's true!"
    "The Hummingbird gave the Dragonfly an annoyed stare to drill holes into them."
    b "That will do. Use your skill to blow some more air on the fire. I'll go find some branches to add to it."
    hb "You don't know when to shut your mouth, do you?"
    df "Neither of us do."
    hb "Oh no. {b}Don't{/b} lump me with you."
    df "I think this is the time we both admit that we are wrong."
    hb "Wrong? I have been realistic, honest, and truthful."
    df "You have said little to nothing since we met the Bear. You're lying to yourself."
    " The Hummingbird had never seen this shift in Dragonfly before; it made them uncomfortable. It felt like staring at a pool of water, and the reflection was talking back to them."
    " The Hummingbird stood there motionless in shock."
    df " Hahaha. Guess my impression of Bear was that good. In all seriousness though, we really need to figure out what-"
    " The Hummingbird darted at the Dragonfly and attempted to peck at the bug."
    df " Hey! Quit it!"
    hb " Is this a game to you? Putting me in the hot seat while toying with me? Why can you find joy even in a screwed up moment like this?"
    df "We live, we eat, we die! Can I not try to enjoy myself? My lifespan is shorter than yours, and even I can admire the fleeting moments."
    df "You whine and moan that nothing was set perfectly for you. You are spoiled."
    hb "Can I not be? Can I not have wants?"
    b "You carry a wound that cannot be contained in that small body of yours."
    "The Bear reappeared from the darkness carrying a bundle of sticks in its mouth. They dropped them and smacked them one by one closer to the fire."
    b "When we saw the stumps, I noticed you were more vulnerable than I had seen before. You've suffered something on that level."
    b "Something so terrifying it needs you to be a monster to survive it."
    b "Give up."
    hb "Excuse me?"
    b "If you had my body, my strength, my experience. Would it be enough?"
    hb "...Yes."
    df "You're lying again."
    hb "Can you not butt in anymore? You've been a thorn in my side, a zit I couldn't pop, a sickness that never dies."
    b "Then leave. The Dragon has been your voice of reason since you've met them. They are the small voice you've kept-"
    hb "Shut up."
    b "locked away."
    hb "SHUT UP!"
    b "-The voice you wish you could let speak out but won't admit is right."
    "The Hummingbird's heart raced intensely. A rage boiled within the small body but was only a defense mechanism. The Hummingbird did not want to admit they were read so easily."
    hb "You will never understand... What I saw. We.... lost everything. I was hopeless. Desperate for survival. Death has been hunting me for too long. Not a single moment do I go without feeling its gaze upon me."
    b  "You carry a will to live that some wish they had. To be able to keep moving forward is to live. You are the only one holding yourself back."
    "The Pack fell silent. The fire crackled and hummed. No one said a word."
    "The Hummingbird shined and began to generate a [[gust of wind] and pushed it to the fire. The Hummingbird kindled the fire; the fire must live so everyone can stay warm."
    "What is my purpose? They all thought."
    jump BHD_Tile8


#-------
#- BTR Tile 7 Route
#------
label BTR_Tile7:
    "The day quickly vanished. The fear, adrenaline, and unrest settled as the sun set."
    b "I think we can rest here."
    tl "How are you doing? Are you sure that wound won't be a problem later?"
    r "It will definitely be. I knew a raccoon who got caught in a human trap once. Buddy was dead a week later from some weird mucus growing on their leg."
    r "Sit down now and let me use my herbs and spices on ya."
    "The Bear did not want to, but it seems the Raccoon is more knowledgeable in this aspect than they thought."
    tl "Hey Raccoon, do you mind doing that thing you usually do when the sun goes down?"
    r "Yeah mean starting the fire? Yeah, I should. Won't be able to tend to the wound without being able to see. Good call."
    " The Turtle nodded. Guilt consumed the Turtle as they were unable to do anything to help their friends in an extremely dire scenario."
    " The Raccoon reached into their [[magic pocket] and pulled out a piece of flint and a rock."
    r "Hey Bear, you mind clawing at the ground for me? I need a clean patch to set up this fire. Imma grab some sticks real quick."
    r "Gotta keep this fire up and running long enough to tend to your wounds."
    b "Mind getting the Turtle off my back?"
    r "Yeah, no problem."
    "This constant dynamic between the Raccoon and Bear is something the Turtle wishes it could do. Land really is not a turtle's domain."
    r "Alright, you two can hang here; I'll go grab the sticks and stuff. Be back in a jiffy!"
    " The Raccoon scampered off into the brush. The Bear began to stab and pick at the soil to create the patch the Raccoon wanted."
    "The Turtle walked around and stared at the digging process."
    b "What's on your mind? I can tell you're still shaken up from the human incident."
    tl "Ah, well, Yeah... I felt like I really couldn't do much per se. All I did was bite down on your back and hope for the best. There really haven't been any moments I look back on and say, \"I did good there.\""
    "The Turtle hoped for a response from the Bear, but they did not respond. Turtle wanted some form of criticism, but nothing was returned."
    b "That's it?"
    tl "What?"
    b "That's what worries you? Heh"
    tl "Wha-Wha- What's funny? Did I sound like a fool?"
    b "No. You dwell too much on the small things, Turtle. You did well, and you don't realize it."
    tl "When?"
    b "Who realized the human was still chasing us after we thought we lost them? Who was immediately voluntold to explore the lake because they are the best diver?"
    b "Who has the ability to protect and tell the stories of the past?"
    tl "Me. Huh."
    b "I think you just get so frightened and panicked that you don't realize that you do contribute in your own ways."
    "The Bear completed their small hole for the fire. The Bear felt proud of making a hole."
    "The Turtle realized that maybe they are better at some things than they realized; it's just a matter of perspective that blinded them."
    " The Raccoon returned running with some sticks in its mouth and presumably more in its magic bag."
    " Alright, Turtles and Bears let us begin."
    " The Raccoon pulled out more sticks from its [[magic pocket] and began throwing them into the small hole."
    "After that they pulled out some dried grass and made a ball. Next they grabbed the piece of flint and a rock and began smashing them together. Sparks began to fly."
    "The Bear and Turtle looked baffled in amazement at the sorcery the Raccoon was doing before their very eyes. Soon enough, the grass caught fire."
    r "Okay! Hot! Hot! Hot!"
    "The Raccoon grabbed the ball and tossed it into the pile of sticks. Then the Bear grabbed sticks and put them on top of the small fire."
    r "Blow on the fire please!"
    b "Oh, sure!"
    "With the help of Bear blowing on the fire, it almost went out, but Raccoon's guidance helped keep it alight, and finally, the bigger sticks caught fire."
    r "It lives! Yes! Thank you, spirits of the forest."
    "The Bear and Turtle looked in amazement at the fire. This destructive force, right in front of them, wasn't spreading."
    "It stayed there, but it felt terrifying in its own way, yet it also felt pleasing and warm to be next to."
    b "How did you do this?"
    r " Well, I'm not really sure where I learned it from. I just kind of knew how to do it. Pretty neat, right?"
    "The Bear couldn't help but be amazed. The silly Raccoon had many tricks up its sleeve. What else did they know?"
    r "Alright, lend me your face."
    "The Raccoon gestured with its little paws for the Bear's face with bundles of herbs and spices ready. The Bear was extremely reluctant."
    " It hurt a lot last time, and they weren't sure about this."
    "The Raccoon was not taking no for an answer and got closer. The Bear dropped to the floor accepting defeat."
    r " Put this in your mouth. Next to the inside of the wound."
    b "It tastes bitter. Ouw! If Horphs!"
    r "Oh good. That means it's working."
    b "I domph like dis."
    r "Did not say you would. Just know that means it's working, I think?  Had another animal I tried it on. Hehe. They want me dead buut, they are still alive."
    b "Yeah. ME!"
    r "Hey! No moving and whining; I need you to stay still. I'm cleaning the wound."
    "The Turtle watched this all happen with a smile on their face. This team was good. They will make it. The Turtle was sure of it. The only issue is. What would they do when they reached it?"
    jump BTR_Tile8

#---------------------------
#--End Bear Tile 7
#--------------------------


#---------------------------
#--Begin Bear Tile 8
#--------------------------

#-------
#-BHD Tile 8 route
#-------
label BHD_Tile8:
    "The Pack was able to navigate through the forest using the Bear's [[path sensing] string, which had returned to them the night before."
    hb "Does this string of yours ever end?"
    b "If it did, I would have said so."
    df "Seems like it. My [[foresight] is getting a bit hazy, but I see us stopping somewhere."
    b "Good."
    "After a few more hours of traveling, they reached the foreseen stopping point. A giant lake stood in their path."
    df "This is exactly what I saw."
    hb "A lake?"
    b "Strange, the string ends here at the water's edge."
    df "You know any magic words? Might be a riddle!"
    hb "It looks like an ordinary lake..."
    "The Hummingbird felt it for a split second. The chill they felt that night. It all came rushing back in an instant, only to be snapped away. The Hummingbird slowly flew to the water."
    b "Bird? Bird!"
    "The hummingbird flew into the water and, like a drop of water, was gone in an instant. Consumed by the lake's existence."
    b "Dragon! Can you see anything?"
    "The Dragonfly was gone as well. Only the Bear remained in the middle of the lake."
    b "When did I get so far into the lake? Where is everyone?"
    "All valid questions, but no one answered them. The Bear saw something below them shining. They weren't sure what it was, but they were attracted to it. As they descended, the water began beating."
    "It got darker and darker. The beating kept going. Then it went quiet."
    $ BearBranch = True
    return

#-------
#-BTR Tile 8 route
#-------
label BTR_Tile8:
    "The Pack was able to navigate through the forest using the Bear's [[path sensing] string, which had returned to them the night before."
    r "How's your cheek feeling?"
    b "It stings a lot."
    r "I think that's, good?"
    tl "I feel strange."
    r "How so?"
    tl "I remember this path. There should be a lake somewhere up ahead."
    r "Feeling lucky and wanting to dive?"
    tl "No. This one's different."
    b "Let's move faster."
    "The Pack advanced quickly down the path following the Turtle's guidance. In a short span of time they were in front of a giant lake."
    tl "Get me down, please?"
    r "Yeah, give me a second."
    b "You gonna use your magic?"
    tl "Yes. Put me at the water's edge, please."
    " The Raccoon did as it was told and plopped the Turtle in the sandbar. The turtle walked to the water and began to float. The Turtle began the ritual of the [[tidal memory]."
    " The water began to ripple and change. Waves formed, and the water got violent. The Bear and Raccoon looked at each other and rushed into the water. Something was going wrong with the ritual."
    " As the two approached the Turtle. The waves got more violent and began pushing them away. Suddenly a big wave appeared."
    r " That's not good!"
    b " Get out of the water!"
    r "I'm trying, but I'm being pulled in! Bear I think we're-"
    "The wave crashed with a hard thud. Consuming all three animals. Each getting pulled into the dark depths of the lake."
    $ BearBranch = True
    return


#---------------------------
#--End Bear Tile 8
#--------------------------

#------------------------------------------
#-End Bear Branch
#------------------------------------------




#------------------------------------------
#-Start Dragonfly Branch
#------------------------------------------
label Choose_Dragonfly:

    "{i} Dragonfly, ever full of hope, mostly relies on their [[Foresight] to glimpse the future. If that fails, their [[Compound Eyes] can take in additional information from their present surroundings.{i}"

    "Choose the Dragonfly"
    menu: 
        "Yes":
            jump Begin_Dragonfly
        "No":
            jump starting_choice


label Begin_Dragonfly:
    "{i} A small Dragonfly emerges from the brush, flitting about lazily through the air. {i}"

    df "What a lovely afternoon...the breeze feels just right today."

    df "This is what I love about the forest. Everything seems so warm and inviting on a day like this."

    df "But this is no time to be still. I suppose I should start making my way towards this lake."

    df "Although, it appears I've forgotten where it is. All I know is that it seems...important."

    df "Well, no matter. If it's important, then I'm sure I will come across it sooner or later."

    df "All in good time."

    df "Hmm...now which direction should I go..?"

label dragon_transition_one:
    scene map1 onlayer master
    menu:
        "Take upper route":
            $ MapNumber = 2.1
            jump dragon_tile_two
        
        "Take lower route":
            $ MapNumber = 2.2
            jump dragon_tile_two

label dragon_tile_two:
    "{i}The winds start to pick up throughout the forest. What was once a gentle breeze has now been whipped into a gale. The small Dragonfly struggles to fly straight in this weather.{i}"

    df "Oh dear! These are certainly less-than-ideal flying conditions."

    df "I'm not sure how much longer I can stay in the air!"
    menu:
        "Take shelter until the winds cease.":
            jump dragon_hide

        "Fly on, darting between cover from the wind. [[Compound Eyes]":
            jump dragon_fly
    label dragon_hide:
        "{i} Dragonfly flies down into an old hollow tree stump, where they wait for several hours until the wind has gone back to normal. {i}"
        jump dragon_transition_two

    label dragon_fly:
        "{i} Dragonfly flies onward, moving from tree to tree to gain maximum protection from the oncoming flurry. Moving through tree hollows and tiny openings in bushes, they use their [[Compound Eyes] to spot which pieces of cover up ahead will provide the best defense from their adversary; the air itself.{i}"
        jump dragon_transition_two

label dragon_transition_two:
    if MapNumber == 2.1:
        scene map2_1 onlayer master 
    elif MapNumber == 2.2:
        scene map2_2 onlayer master
    menu:
        "Take upper route":
            if MapNumber == 2.1:
                $ MapNumber = 3.1
            else:
                $ MapNumber = 3.2
            jump dragon_tile_three
        
        "Take lower route":
            if MapNumber == 2.1:
                $ MapNumber = 3.2
            else:
                $ MapNumber = 3.3
            jump dragon_tile_three

label dragon_tile_three:
    "{i}Slightly ruffled from the previous gale, Dragonfly travels onward through the forest.{i}"

    df "Mmm...it's good to be able to fly without issue again. Hopefully this weather holds up."

    df "I wonder why I didn't feel that it would be that windy..."
    
    df "I guess it just wasn't important enough for me to see it through [[Foresight]."

    df "After all, I got through those winds alright. So it all worked out in the end."

    if DFsighting < 1:
        df "I'm sure if there's something really bad to worry about, the universe would let me know somehow."
    else:
        df "Although, perhaps I should be a little more cautious in the future."

        df "Winds like those make me wish that Hummingbird was around. Even if they always seem so upset."

    df "At any rate, a little insect like me could surely use some company on this lone journey."

    df "Well, I'm sure I'll run into someone eventually. All in good time."

    jump dragon_transition_three

label dragon_transition_three:
    if MapNumber == 3.1:
        scene map3_1 onlayer master
    elif MapNumber == 3.2:
        scene map3_2 onlayer master
    else:
        scene map3_3 onlayer master
    menu:
        "Take upper route":
            if MapNumber == 3.1:
                $ MapNumber = 4.1
            elif MapNumber == 3.2:
                $ MapNumber = 4.2
            else:
                $ MapNumber = 4.3
            jump dragon_tile_four
        
        "Take lower route":
            if MapNumber == 3.1:
                $ MapNumber = 4.2
            elif MapNumber == 3.2:
                $ MapNumber = 4.3
            else:
                $ MapNumber = 4.4
            jump dragon_tile_four

label dragon_tile_four:
    "{i}Dragonfly moves through the trees, admiring the colors of the leaves as they fly.{i}"

    df "Ahh... You know, I feel like something is waiting for me just up ahead [[Foresight]."

    "{i}A rustling noise grows louder from a group of nearby bushes.{i}"

    df "Right on time! I wonder who I will meet today."
    jump dragon_select

label dragon_select:
    menu:
        "Raccoon and Bear":
            jump rb_select

        "Hummingbird and Coyote":
            jump ch_select

    label rb_select:
        "{i}Curious as ever, Raccoon uses their [[Agility] to get out of sticky situations, and can pull a myriad of objects from their [[Magic Pocket]."
        
        "{i}Headstrong Bear on the other hand likes to use their raw [[Strength] ability to push forward, aided by their magical [[Pathsense] to sniff out the best route.{i}"

        menu:
            "{i} Choose Raccoon and Bear?{i}"

            "Yes":
                jump raccoon_bear

            "No":
                jump dragon_select

    label raccoon_bear:
        "{i}The rustling noise turns to the sound of talking. Not just talking, arguing. As energetic Raccoon and serious Bear emerge from the brush, they appear to be deep in the middle of an argument.{i}"

        r "Listen, I just thought it could be helpful, that's all! It wasn't even that bad of an idea!"

        b "{i}sighs{i} Except that I had to pull you outa the muck in that lake."

        r "Well, they're called CATtails, so I just thought that I would be able to find the cat that the tail went to, and then they could travel with us."

        b "You can't even swim well. You had no right to just jump into the water like that."

        "{i}Bear looks to Dragonfly, nodding to them as the pair approaches.{i}"

        b "At least we found you. Hopefully you've been holding up better than we have."

        r "Hey, I don't know what they're talking about. We've been holding up perfectly fine- hey, do we look fine to you?"

        "{i}Dragonfly looks over the wet Raccoon, and the grumpy looking Bear.{i}"
        menu:
            "\"You look less than fine.\"":
                jump less_fine

            "\"You look fine.\"":
                jump look_fine

        label less_fine:
            df "Well, you are all sopping wet. But luckily the remaining sun should be able to dry you off."

            b "Lucky? We're lucky that I got you out of that lake at all."

            if Rsighting >= 1:
                r "Well...I guess I could've asked you first before jumping in...sorry about that..."
            else:
                r "Bah! I knew exactly what I was doing."
            jump bear_raccoon

        label look_fine:
            df "You both look perfectly fine to me!"

            r "Thank you! See what I was saying Bear about being a little more positive?"
            jump bear_raccoon

        label bear_raccoon:
            b "All right, whatever. We lost a lot of light thanks to your stunt earlier, so we should keep moving."

            df "As you wish. I'm just so glad I came across you two. I think this will be a wonderful journey together."
            jump dragon_transition_fourB

    label ch_select:
        "{i}A bundle of energy, Coyote makes great use of their nose with their [[Scent] ability, and their [[Poison Immunity] lets them identify and consume food that would be deadly to others.{i}"

        "{i}Meanwhile Hummingbird, ever the cynical realist, remains one of the strongest fliers available with [[Flight], aided by their use of their [[Wind Gale] magic.{i}"
        menu:
            "{i}Pick Coyote and Hummingbird?{i}"
            
            "Yes":
                jump coyote_hummingbird

            "No":
                jump dragon_select

        label coyote_hummingbird:
            "{i}Almost tumbling through the bushes, small but energetic Coyote bursts through, followed by sour-looking Hummingbird. The two look towards Dragonfly with completely different expressions.{i}"

            c "Oh boy, another one?! I can't wait to travel together, friend!"

            "{i}Coyote beams warmly. In contrast, Hummingbird looks at Dragonfly with a downcast expression.{i}"

            hb "Another one of us? Two was already enough, but traveling with three is just going to make things far too complicated."

            df "Well, we are together now. So let us just be happy that we found one another, yes?"

            if HBsighting < 1:
                hb "{i}shrugs{i} Not entirely sure what there is to be happy about, but you're right. We're stuck together, whether I like it or not."
            else:
                hb "{i}shrugs{i} The more the merrier, I suppose. Thats what they say, at least."

            c "Then it's settled! We travel!"
            jump dragon_transition_fourA

label dragon_transition_fourA:
    if MapNumber == 4.1:
        scene map4_1 onlayer master
    elif MapNumber == 4.2:
        scene map4_2 onlayer master
    elif MapNumber == 4.3:
        scene map4_3 onlayer master
    elif MapNumber == 4.4:
        scene map4_4 onlayer master
        
    menu:
        "Take upper route":
            if MapNumber == 4.1:
                $ MapNumber = 5.1
            elif MapNumber == 4.2:
                $ MapNumber = 5.2
            elif MapNumber == 4.3:
                $ MapNumber = 5.3
            elif MapNumber == 4.4:
                $ MapNumber = 5.4
            jump dragon_tile_fiveA
        
        "Take lower route" if MapNumber < 4.4:
            if MapNumber == 4.1:
                $ MapNumber = 5.2
            elif MapNumber == 4.2:
                $ MapNumber = 5.3
            elif MapNumber == 4.3:
                $ MapNumber = 5.4
            jump dragon_tile_fiveA

label dragon_transition_fourB:
    if MapNumber == 4.1:
        scene map4_1 onlayer master
    elif MapNumber == 4.2:
        scene map4_2 onlayer master
    elif MapNumber == 4.3:
        scene map4_3 onlayer master
    elif MapNumber == 4.4:
        scene map4_4 onlayer master
        
    menu:
        "Take upper route":
            if MapNumber == 4.1:
                $ MapNumber = 5.1
            elif MapNumber == 4.2:
                $ MapNumber = 5.2
            elif MapNumber == 4.3:
                $ MapNumber = 5.3
            elif MapNumber == 4.4:
                $ MapNumber = 5.4
            jump dragon_tile_fiveB
        
        "Take lower route" if MapNumber < 4.4:
            if MapNumber == 4.1:
                $ MapNumber = 5.2
            elif MapNumber == 4.2:
                $ MapNumber = 5.3
            elif MapNumber == 4.3:
                $ MapNumber = 5.4
            jump dragon_tile_fiveB

label dragon_tile_fiveA:
    "{i}Coyote trots along happily through the brush, as Dragonfly and Hummingbird follow close behind the best they can.{i}"

    hb "Slow down dog! Are you trying to lose us?"

    c "Oops! Sorry! I'm just so excited to be traveling with new friends again!"

    df "Do not worry Hummingbird. If Coyote goes far, their powerful nose will surely lead them back to us."

    c "Yeah! I got a real good nose."

    "{i}Coyote sniffs the air, taking in all the sensory information around them through their nose [[Scent].{i}"

    c "Smells like, {i} sniff sniff {i} Rain."

    "{i}As if on cue, a droplet hits Coyote right on the snout. They rear back slightly, licking their nose.{i}"

    hb "What?! You mean it's going to rain? Now?"

    "{i}Without saying another word, Hummingbird flies directly up into the air [[Flight]. They fly high up into the sky, looking at the horizon, where they can see dark clouds rolling in towards them. They quickly fly back down.{i}"

    hb "They're right. It seems like a massive rainstorm is coming our way. This is bad, this is really bad."

    "{i}Hummingbird starts flying around in circles nervously.{i}"

    df "Woah, woah. Everything will be alright, don't worry."

    hb "Don't worry?! When that rain gets here, it will be too heavy for either of us to fly. That means we'll have to cling to a branch and hang on for dear life so we don't get swept away! Does that sound 'alright' to you?"

    "{i}The rain starts to fall heavier, further exacerbating Hummingbird.{i}"

    df "Hey, I've made it through tougher things before, and I'm sure you have too. We'll just find a safe, dry spot to take shelter."

    "{i}Dragonfly looks around and spots a dry looking tree stump [[Compound Eyes].{i}"

    df "Over here."

    "{i}Dragonfly directs Hummingbird and Coyote over to the tree stump. The two small fliers duck down inside, while Coyote sticks their snout in, letting the rain wash off their back.{i}"

    hb "Great. Being in this stuffy stump is totally miles better than being out there. I can hardly breathe in here."

    c "Oh, sorry!"

    "{i}Coyote moves their face out of the hole at the top of the tree stump, letting both fresh air and a few rain drops in.{i}"

    hb "No, wait! Come back! Come back!"

    "{i}Confused Coyote pokes their head back over, looking down into the stump where the other two animals are.{i}"

    df "Just be still, Hummingbird. The rain will pass, and then we can continue traveling again. All in good time."

    hb "All in good time? Why do you always say that...Look, I appreciate you finding us shelter, but at this rate, if we aren't able to get out soon so I can find food, I might die."

    "{i}Dragonfly looks to Hummingbird, their eyes shimmering as they glimpse the future [[Foresight].{i}"
    df "I don't think you'll be dying anytime soon. {i} They say, with an air of finality.{i}"

    "{i}Hummingbird huffs, and hops over to the opposite side of the stump from Dragonfly.{i}"

    "{i}After some time passes, Hummingbird starts shivering.{i}"

    hb "This isn't good for me. I need to keep moving to stay warm, but how on earth am I supposed to do that from in here. {i}They grumble to themselves, hopping from one foot to the other.{i}"

    "{i}Hummingbird hops back over to where Coyote and Dragonfly are.{i}"

    hb "Hey Coyote. I can't stay in this stump. We have to keep traveling. We need you to carry us on your back, and make your way through the rain, without letting us get rained on."

    "{i}Coyote looks down nervously.{i}" 
    c "Are you sure? I-I mean, I've never had to do anything like that before."

    hb "Well, neither have we. Look, it's not a great option, but it's the only one we have."

    c "But what if I can't do it? What if you get hurt?"

    hb "Well, then I guess it would be your fault then."

    "{i}Coyote whimpers and puts their head down, covering their eyes with their paws. Dragonfly looks over to Hummingbird with a somewhat disapproving expression.{i}"

    hb "Err...I mean...look, we're all in this together. So we'll help you out the best we can, and if something goes wrong...well then I guess it won't just be your fault."

    df "What I think Hummingbird means to say is that you are the right one to lead us through this situation. We'll be right behind you."

    hb "{i}scoffs{i} Literally."

    "{i}Coyote stands up straight, the rain continuing to fall all around them.{i}"
    menu:
        "Carry them.":
            jump yes_carry

        "Don't carry them.":
            jump no_carry

    label yes_carry:
        c "{i}Coyote nods, looking at them.{i} I think I can do it." 

        "{i}They move right next to the stump.{i}"

        if HBsighting < 1:
            hb "{i}sighs{i} I wasn't sure if you'd actually do it. Alright then, I guess this is happening."
        else:
            hb "Ok bud, just try to hold steady and...don't drop us. {i}They gulp nervously.{i}"

        "{i}Dragonfly and Hummingbird quickly make their way onto Coyote's back, holding onto their fur.{i}"

        c "O-ok. Hold on tight. {i}Coyote looks towards the direction they're traveling in nervously.{i}"

        df "Trust your instincts Coyote. You can do this."

        "{i}Coyote takes a deep breath, then takes off at a gentle run through the forest.{i}"

        "{i}Water falls around the Pack as Coyote darts between the trees, trying to stay within treecover to avoid the rain falling directly on them.{i}"

        df "Make to the right! There should be a thick patch of trees over there [[Foresight]."

        "{i}Coyote obliges, and heads through the bushes in that direction. As they break through a line of trees, rather than finding a lush grove, the Pack is met with a glen of tree stumps. Coyote pauses.{i}"

        df "I don't understand...there should be trees right here..."

        hb "Nevermind that! We'll just have to go back the way we came. Quickly Coyote!"

        "{i}Coyote stands there, staring at the clearing of stumps and roots, exposed by erosion. Tuning out the noise, they dash forward into the area. Hummingbird protests, but Coyote seems wholly concentrated on their movements.{i}"

        "{i}Coyote ducks around and under the roots and short tunnels, moving deftly enough that the rain hardly touches them. Before any of them know it, they're on the other side of the once-glen.{i}"

        "{i}Coyote pants looking back at where they came from, the other two momentarily speechless.{i}"

        hb "How did you do that?"

        c "...I don't know. I just listened to something...something inside me. It told me what to do."

        "{i}They linger for just a moment more, before Coyote continues moving. They travel this way until the rain clears.{i}"

    label no_carry:
        c "{i}Coyote shakes their head.{i} I just don't think I can do it. I'm sorry. {i}They whine.{i}"

        if HBsighting >= 1:
            "{i}Hummingbird shakes their head, but bites their tongue before they say anything to Coyote, electing instead to hop back over to the far side of the stump.{i}"
        else:
            hb "Typical. {i}Chirps disapprovingly.{i} This is why it hardly does any good to travel with others."

        df "There there, it's all right Coyote. It's ok to be afraid."

        c "But I let you all down! I'm not a leader. I can't help anyone."

        df "That's not true! Sometimes we are faced with things that we don't feel ready for. It is ok to rely on others for strength when we feel uncertain. But you are also strong by yourself, and when the time comes for you to act, I'm sure you'll be ready. {i}smiles.{i}"

        "{i}Coyote sniffs and nods.{i}"

        df "Besides, the rain will surely be over soon [[Foresight]. All we need to do is wait."

        hb "Doesn't seem very likely to me."

        "{i}As they sit in the stump, the rain shows no signs of letting up. With each hour that passes, Hummingbird looks more smug, and Dragonfly looks more confused. After most of the day has passed, the rain finally stops, and the Pack continues onward.{i}"
        jump dragon_transition_fiveA

label dragon_tile_fiveB:

    "{i}As the Pack continues, they spot the nearby figure of a resting animal. As they get closer, they realize that it isn't resting. It's dead.{i}"

    b "{i}Bear stops suddenly.{i} Everyone stop!"

    r "Uh oh. I'm about to be sick. {i} looking away from the half-eaten carcass of the elk.{i}"

    df "It appears that this one was killed no more than a couple days ago [[Compound Eyes]."

    b "And that's a great reason to just leave it alone. Where there's meat, there's bound to be predators, and we don't want to deal with that. Just keep moving."

    r "Predators? You're scared of other animals? But you're the biggest animal in the whole forest."

    b "I'm not scared. Just don't want to mess with things unnecessarily."

    r "Well, don't worry Bear. If any mean creatures show up, I'll scare them off!"

    "{i}Raccoon pulls a long stick out of their pocket and starts waving it around [[Magic Pocket].{i}"

    r "I'll defend you. I'll defend everyone, hah!"

    b "Hey, be careful. And stop making so much noise."

    df "Now now. Raccoon won't cause any harm. I'm sure the danger is long past now [[Foresight]."

    "{i}Raccoon turns around to face Bear, swinging the stick wildly and clipping Dragonfly in the process. Dragonfly spirals towards the ground, but rights themselves at the last second, managing to fly up mostly unharmed.{i}"

    b "WATCH IT! {i}Bear roars.{i}"

    "{i}Raccoon shrinks away as Bear storms up to them, putting one paw on their back and steering them around to face the dead elk that's now behind them.{i}"

    b "Do you want to end up like that animal?! Do you?! There are hundreds of things in this forest that want to rip you limb from limb, and you seem to have no intention of protecting yourself from them! Not only that, but you become a danger for others too! You need to learn when to calm down and stay quiet!"

    "{i}Raccoon stares at the dead elk in the distance, and then down at the ground.{i}"

    if Bsighting >= 1:
        b "{i}Sigh.{i} Look, just be more careful, ok? Stay behind me."
    else:
        b "If you have nothing to say for yourself, then just stay back and let me navigate in peace."

    b "We've already made too much noise."
    
    "{i}Bear starts moving again, with Raccoon and Dragonfly trailing behind them.{i}"

    "{i}Raccoon walks for a while in silence, before quietly piping up to Dragonfly.{i}"

    r "Sorry for hitting you with the stick."

    df "No worries my friend. I should've been able to see it coming. {i}Dragonfly looks a little perturbed.{i}"

    r "Well still, they're right. I should probably be a bit more careful."

    df "...perhaps. I would definitely appreciate not getting hit again."

    "{i}The two of them chuckle nervously.{i}"

    r "I just want to be able to be helpful. I want to be a knight and a comedian. Protect people, and make them laugh. But Bear doesn't get it. They're already strong enough to protect people easily."

    "{i}Dragonfly thinks for a moment.{i}"

    df "You are right, Bear is certainly very strong. At least physically. But you are also strong."

    r "What do you mean?"

    df "I think there are many different kinds of strength. There are strong stumps and hard rocks, but there are also tree branches that bend but do not break, and tiny fruits that contain the most juice."

    df "There's always more than one kind of strength. I just don't know if Bear remembers that all the time."

    "{i}Dragonfly looks up towards Bear with a kind expression, as Raccoon realizes Bear has been silently listening to their conversation this whole time. Bear looks somewhat embarrassed, and moves forward in silence.{i}"
    jump dragon_transition_fiveB

label dragon_transition_fiveA:
    if MapNumber == 5.1:
        scene map5_1 onlayer master
    elif MapNumber == 5.2:
        scene map5_2 onlayer master
    elif MapNumber == 5.3:
        scene map5_3 onlayer master
    elif MapNumber == 5.4:
        scene map5_4 onlayer master

    menu:
        "Take upper route" if MapNumber > 5.1:
            if MapNumber == 5.2:
                $ MapNumber = 6.1
            elif MapNumber == 5.3:
                $ MapNumber = 6.2
            elif MapNumber == 5.4:
                $ MapNumber = 6.3
            jump dragon_tile_sixA
        
        "Take lower route" if MapNumber < 5.4:
            if MapNumber == 5.1:
                $ MapNumber = 6.1
            elif MapNumber == 5.2:
                $ MapNumber = 6.2
            elif MapNumber == 5.3:
                $ MapNumber = 6.3
            jump dragon_tile_sixA

label dragon_transition_fiveB:
    if MapNumber == 5.1:
        scene map5_1 onlayer master
    elif MapNumber == 5.2:
        scene map5_2 onlayer master
    elif MapNumber == 5.3:
        scene map5_3 onlayer master
    elif MapNumber == 5.4:
        scene map5_4 onlayer master

    menu:
        "Take upper route" if MapNumber > 5.1:
            if MapNumber == 5.2:
                $ MapNumber = 6.1
            elif MapNumber == 5.3:
                $ MapNumber = 6.2
            elif MapNumber == 5.4:
                $ MapNumber = 6.3
            jump dragon_tile_sixB
        
        "Take lower route" if MapNumber < 5.4:
            if MapNumber == 5.1:
                $ MapNumber = 6.1
            elif MapNumber == 5.2:
                $ MapNumber = 6.2
            elif MapNumber == 5.3:
                $ MapNumber = 6.3
            jump dragon_tile_sixB

label dragon_tile_sixA:
    "{i}As the Pack makes their way down a small hill, they find themselves facing a large patch of brambles. The sharp thorns look very intimidating.{i}"

    df "Interesting. Will you all be ok crossing this?"

    hb "{i}rolls eyes.{i} Sure I can. Just make sure we're not going to be slowed down by the pup."

    c "Umm...I'm not sure. It looks dangerous..."

    c "Hold on, what did you say Hummingbird?"

    df "Quiet down everyone! Let us focus on the task at hand."

    "{i}As the Pack approaches the briar, there's a sudden low rumbling noise. In a flash, the animals are all thrown backward, as dirt and earth explodes out from under them. The plants roil for a moment, as emerging from the tangle is a walking mass of thorns and bushes, an angry Briar Elemental.{i}"

    hb "Ack! You couldn't have seen this coming, huh Dragonfly?!"

    c "Oh man. What do we do? What do we do?"

    menu:

        "Squeeze through the briar and make a run for it.":
            jump briar_squeezeA

        "Goad the elemental into leaving the thorn patch.":
            jump briar_goadA

        "Blow the vines aside and run through [[Wind Gale].":
            jump briar_galeA

    label briar_squeezeA:
        df "Quickly! Everyone make a run for it!"

        "{i}The Pack manages to squeeze, trample, or fly their way through the brush, with the elemental right on their heels. They get pricked and poked, but ultimately make it out ok.{i}"
        jump dragon_transition_sixA

    label briar_goad:
        df "We need to get it away from the briar patch! Then it'll be out of our way!"

        "{i}Coyote looks nervous, but starts yipping at the elemental.{i}" 
        
        c "C-come and get us! I b-bet you can't catch me!"

        "{i}As the elemental takes a step out of the briar patch to pursue the animals, it starts to lose its form, as it disconnects from the vines and bushes. Seizing the moment, the Pack makes a quick getaway through the briar patch.{i}"
        jump dragon_transition_sixA


    label briar_galeA:
        "{i}Dragonfly looks stunned and overwhelmed. Hummingbird looks between all the animals and the elemental, and huffs.{i}"

        hb "All right everyone, stay back!"

        "{i}As the others take a step back, Hummingbird starts beating their wings faster and faster. As they do, large gusts of wind start to blow out from them, until they become almost gale force [[Wind Gale].{i}" 
        
        "{i}Hummingbird directs these winds towards the patch of brambles, blowing them out of the way and creating a clear path around the elemental.{i}"

        hb "Go! Quickly!"

        "{i}Coyote looks at Dragonfly, then back at Hummingbird, seeming nervous. Then they take a deep breath, and start running through the path created. Dragonfly quickly follows behind them, and Hummingbird brings up the rear of the Pack, as they safely clear the brush.{i}"
        jump dragon_transition_sixA

label dragon_tile_sixB:
    "{i}As the Pack makes their way down a small hill, they find themselves facing a large patch of brambles. The sharp thorns look very intimidating.{i}"

    df "Interesting. Will you all be ok crossing this?"

    r "This looks like a job for a professional squeezer! Put me in coach, I'm ready."

    b "Slow and steady, Raccoon. Let's all make sure we stick together."

    df "Quiet down everyone! Let us focus on the task at hand."

    "{i}As the Pack approaches the briar, there's a sudden low rumbling noise. In a flash, the animals are all thrown backward, as dirt and earth explodes out from under them. The plants roil for a moment, as emerging from the tangle is a walking mass of thorns and bushes, an angry Briar Elemental.{i}"

    b "Get back everyone! Do your best to stay out of its range."

    r "No way! I can handle this. Trust me!"

    menu:

        "Squeeze through the briar and make a run for it.":
            jump briar_squeezeB

        "Goad the elemental into leaving the thorn patch.":
            jump briar_goadB

        "Fight the elemental [[Strength].":
            jump briar_strengthB

        "Run around the elemental quickly to confuse it [[Agility].":
            jump briar_agilityB

    label briar_squeezeB:
        df "Quickly! Everyone make a run for it!"

        "{i}The Pack manages to squeeze, trample, or fly their way through the brush, with the elemental right on their heels. They get pricked and poked, but ultimately make it out ok.{i}"
        jump dragon_transition_sixB

    label briar_goadB:
        df "We need to get it away from the briar patch! Then it'll be out of our way!"

        r "Don't worry! I'm a master of distraction! Hey you big ugly blackberry bush! Over here!"

        "{i}As the elemental takes a step out of the briar patch to pursue the animals, it starts to lose its form, as it disconnects from the vines and bushes. Seizing the moment, the Pack makes a quick getaway through the briar patch.{i}"
        jump dragon_transition_sixB

    label briar_strengthB:
        df "Go Bear! We'll be right behind you!"

        "{i}Bear rushes forward into the brambles, flattening them down as they run. They rear onto their hind legs, and slam their front paws into the elemental with all their might [[Strength].{i}"

        "{i}The others take this opportunity to run past the elemental, while Bear growls and grapples with it. Once they're through, Raccoon calls out to Bear.{i}"

        r "We're good! Get out of there Bear!"

        "{i}Bear manages to untangle themselves from the grasp of the elemental, and runs after the others, as they run until the elemental is far from sight.{i}"
        jump dragon_transition_sixB

    label briar_agilityB:
        df "Raccoon, go show it your strength!"

        r "Aye aye!"

        "{i}Raccoon runs into the patch, easily dodging the strikes from the elemental’s thorny arms. They run around the elemental over and over again, weaving in and out of its reach [[Agility].{i}" 
        
        "{i}After a few minutes, the elemental seems sufficiently tangled up and confused. Raccoon grins proudly to the others, and they all quickly make their way through the briar patch, past the dazed elemental.{i}"
        jump dragon_transition_sixB

label dragon_transition_sixA:
    if MapNumber == 6.1:
        scene map6_1 onlayer master
    elif MapNumber == 6.2:
        scene map6_2 onlayer master
    elif MapNumber == 6.3:
        scene map6_3 onlayer master
        
    menu:
        "Take upper route" if MapNumber > 6.1:
            if MapNumber == 6.2:
                $ MapNumber = 7.1
            elif MapNumber == 6.3:
                $ MapNumber = 7.2
            jump dragon_tile_sevenA
        
        "Take lower route" if MapNumber < 6.3:
            if MapNumber == 6.1:
                $ MapNumber = 7.1
            elif MapNumber == 6.2:
                $ MapNumber = 7.2
            jump dragon_tile_sevenA

label dragon_transition_sixB:
    if MapNumber == 6.1:
        scene map6_1 onlayer master
    elif MapNumber == 6.2:
        scene map6_2 onlayer master
    elif MapNumber == 6.3:
        scene map6_3 onlayer master
        
    menu:
        "Take upper route" if MapNumber > 6.1:
            if MapNumber == 6.2:
                $ MapNumber = 7.1
            elif MapNumber == 6.3:
                $ MapNumber = 7.2
            jump dragon_tile_sevenB
        
        "Take lower route" if MapNumber < 6.3:
            if MapNumber == 6.1:
                $ MapNumber = 7.1
            elif MapNumber == 6.2:
                $ MapNumber = 7.2
            jump dragon_tile_sevenB

label dragon_tile_sevenA:
    "{i}The Pack have settled around a campfire for the night, preparing themselves for what's in store tomorrow.{i}"

    "{i}Dragonfly stares into the fire thoughtfully.{i}"

    df "Tomorrow will likely be the end of our journey [[Foresight]."

    c "{i}Coyote looks to Dragonfly.{i} Are you alright?"

    df "Sort of. It's just that...I always rely on my sight to warn me. To guide me. But recently it's felt a bit more...unreliable."

    hb "So, what? You're not happy because your little unrealistic predictions turned out to not come true?"

    df "I suppose that's one way of putting it. I see us reaching the end of our journey tomorrow, and everything being all right. But for the first time in a while I guess I feel...worried."

    "{i}Hummingbird remains quiet for a moment.{i}" 
    
    hb "Yeah, well there's a lot to be worried about."

    df "You would certainly know best about that. It's just that..."

    if DFsighting < 1:
        df "...I've never needed worry to stay alive so far. I enjoy that, and I want to hold onto it. I don't think I'm ready to let that go."
    else:
        df "...I miss when I knew everything would turn out fine. It's hard to deal with worry. But I DO want to help everyone be safe. So I suppose I'll have to rely a bit more on the present, and a bit less on the future."

    "{i}The other animals nod in acknowledgement, then sit back a bit and enjoy the heat of the fire. Dragonfly starts to flutter their wings gently against each other, creating a low humming sound.{i}"

    hb "And they call me the one who hums. You encroaching on my turf?  {i}they say tauntingly.{i}"

    "{i}Dragonfly brings their hum so low that only they can hear it.{i}"

    hb "{i}sigh{i} Jeez, it was just a joke. You can do whatever you want, I don't care."

    df "You did well earlier. I was very glad to have you with us."

    hb "Well...I guess you helped as well. I just wanted to make sure everyone wasn't being dumb."

    df "{i}Chuckles.{i} Yes. And you played a vital role in keeping everyone safe."

    df "I just think that maybe you don't realize how what you say affects others."

    hb "...how do you mean exactly?"

    df "Just that, sometimes even if something is true, saying it can lead to the ones we care about getting hurt. You don't want to hurt any of us, right?"

    hb "...no. I don't. I just want others to-"

    df "-to think like you, right?"

    hb "I guess. I just think it would be easier if everyone was objective all the time."

    df "But does it seem like it's been easier for them to do that? {i} Dragonfly gestures to Coyote.{i}"

    hb "...I guess not."

    hb "...sorry."

    df "{i}Dragonfly smiles.{i} Thank you."

    "{i}Coyote bounds over to Dragonfly and Hummingbird.{i}"

    c "Are you guys talking about the big elemental? That was reeeeal scary! Ooh, and when the rain came down!"

    "{i}Coyote is eating a clutch of small berries pulled off of a nearby bush, deep, blood-red juice smeared all over their snout.{i}"

    "{i}Hummingbird looks at Coyote uneasily.{i}" 
    
    hb "Are those...good?"

    c "{i}They nod vigorously.{i}  Suuuper poisonous though. You wouldn't like them [[Poison Immunity]."

    df "{i}Nods.{i} Listen, Coyote. We're quite proud of you. Despite these scary situations, you handled yourself pretty well throughout."

    "{i}Coyote looks up at Dragonfly, awe on their face.{i}" 
    
    c "Really?"

    df "Yes. You were decisive, and knew what you had to do."

    if HBsighting < 2:
        hb "I suppose if you call just looking at everyone else 'being decisive', then sure."

        "{i}Dragonfly looks back at Hummingbird, looking a bit disappointed.{i}"
    else:
        "{i}Hummingbird clucks their tongue disapprovingly at Dragonfly's statement, but seems to hold back from saying anything.{i}"

    df "And at any rate, you're a lot more adult than you would believe."

    c "I was just listening to myself instead of others. Is that what you're talking about?"

    df "Yes, that's it exactly! Trust yourself, and you can act independently when the moment calls for it."

    if Csighting < 1:
        c "hmm...I'm not sure I could do that for a lot of the time. I think I might still need others for help."
    else:
        c "I think I can do that. I think I can do that! I can be independent! I can help others figure things out!"

    df "{i}Chuckles.{i} All in good time, all in good time."

    "{i}Dragonfly looks around the campfire at the other two animals beside them.{i}"

    df "All right everyone. Tomorrow..."
    menu:

        "Be open.":
            jump fire_openA

        "Be careful.":
            jump fire_carefulA

    label fire_openA:
        df "...be open to whatever we find. Tomorrow our journey ends, so take in whatever the universe has in store for us."

    label fire_carefulA:
        df "...be careful when we approach. Tomorrow our journey ends, and we must greet whatever awaits us with alert and undulled senses."

    "{i}The rest of the animals murmur in agreement, before going to sleep by the warmth of the campfire.{i}"
    jump dragon_transition_sevenA

label dragon_tile_sevenB:
    "{i}The Pack have settled around a campfire for the night, preparing themselves for what's in store tomorrow.{i}"

    "{i}Dragonfly stares into the fire thoughtfully.{i}"

    df "Tomorrow will likely be the end of our journey [[Foresight]."

    "{i}Bear nods, sniffing the air.{i}" 

    "They're right. We're close. [[Pathsense]."

    r "That's a good thing, right?"

    df "Sort of. It's just that...I always rely on my sight to warn me. To guide me. But recently it's felt a bit more...unreliable."

    r "Wait, so your eyes aren't working right?"

    df "I suppose that's one way of putting it. I see us reaching the end of our journey tomorrow, and everything being all right. But for the first time in a while I guess I feel...worried."

    b "It's natural to be worried. That's what keeps us alive, nothing wrong with it."

    df "You would certainly know best about that. It's just that..."

    if DFsighting < 1:
        df "...I've never needed worry to stay alive so far. I enjoy that, and I want to hold onto it. I don't think I'm ready to let that go."
    else:
        df "...I miss when I knew everything would turn out fine. It's hard to deal with worry. But I DO want to help everyone be safe. So I suppose I'll have to rely a bit more on the present, and a bit less on the future."

    "{i}The other animals nod in acknowledgement, then sit back a bit and enjoy the heat of the fire. Dragonfly starts to flutter their wings gently against each other, creating a low humming sound.{i}"

    b "Must you do that? I'm trying to keep watch."

    "{i}Dragonfly brings their hum so low that only they can hear it.{i}"

    r "I thought it was nice." 
    
    "{i}Raccoon pulls a marshmallow and stick out of their pocket and starting to roast it by the fire [[Magic Pocket].{i}"

    df "You did well earlier. I was very glad to have you with us."

    r "Really?! {i} Raccoon gets so excited they almost drop their marshmallow in the fire.{i}"

    df "{i}Chuckles.{i} Yes. And you played a vital role in keeping everyone safe."

    df "I just think that maybe a certain animal was right about you loving to charge into danger a little too much."

    "{i}Raccoon looks over towards where Bear is.{i}"
    r "Well, they're always saying that."

    df "Why do you think they're doing that?"

    r "I don't know...I guess because they care about me."

    df "They do indeed. We all do. And that's why we try to help each other make good decisions. Do you understand?"

    "{i}Raccoon nods quietly.{i}"
    menu:
        "{i}Share marshmallow with Dragonfly{i}":
            jump dragon_mallow

        "{i}Share marshmallow with Bear{i}":
            jump bear_mallow

    label dragon_mallow:
        "{i}Raccoon takes a bite from the melty marshmallow, then moves the stick over to where Dragonfly is. Dragonfly flies nearer to it, and graciously takes a bite.{i}"

    label bear_mallow:
        "{i}Raccoon takes a bite from the melty marshmallow, then offers it over to Bear.{i}"

        r "Want some?"

        "{i}Bear obliges, licking a big chunk off of the marshmallow.{i}"

    if Rsighting >= 2:
        r "I think...I think I'll listen more to you all from now on. Can never be too careful, right? Hopefully there will be less accidents this way, and...and I'm very glad to be traveling together."

    "{i}Bear and Dragonfly nod.{i}"

    df "{i}Dragonfly smiles.{i} Thank you."

    "{i}Bear grumbles to themselves as they shift in front of the fire. Dragonfly flies over to them.{i}"

    df "Well, this has been a lovely night. It's been nice to see what our friends are capable of, when they set their minds to it. Wouldn't you agree?"

    "{i}Bear continues to grumble, but does look over to Raccoon, before giving a nod of approval.{i}"

    "{i}Dragonfly hums happily to themselves.{i}"

    "{i}Raccoon looks over to Bear{i}"

    r "You know, if it wasn't for your strength, I don't think we woulda gotten as far as we have."

    b "{i}sighs.{i} Well, this strength is impressive, it's true. But I'm just happy that I can use it to protect you all."

    r "{i}Raccoon nods, and stays silent for a moment, before piping up.{i}"
    
    r "I know you heard our conversation before. So I know that you know that I want to do the same. I want to help protect others."

    b "Yes...I do know that. And I think you're doing...well, you're certainly trying. And I know that's important."

    if Bsighting < 2:
        b "Listen. Just leave the protecting to me. There are plenty of other things you're good at."
    else:
        b "I've seen your strength now. I know that you care, and I think you'll do a great job and protecting people and being strong, in your own way."

    r "Really? You mean it? {i} they beam.{i}"

    b "Yes, I do," 
    
    "{i}Bear can't help but crack a grin{i}"

    b "Now pipe down and finish your marshmallow."

    df "{i}Chuckles.{i} All in good time, all in good time."

    "{i}Dragonfly looks around the campfire at the other two animals beside them.{i}"

    df "All right everyone. Tomorrow..."
    menu:

        "Be open.":
            jump fire_openB

        "Be careful.":
            jump fire_carefulB

    label fire_openB:
        df "...be open to whatever we find. Tomorrow our journey ends, so take in whatever the universe has in store for us."

    label fire_carefulB:
        df "...be careful when we approach. Tomorrow our journey ends, and we must greet whatever awaits us with alert and undulled senses."

    "{i}The rest of the animals murmur in agreement, before going to sleep by the warmth of the campfire.{i}"
    jump dragon_transition_sevenB

label dragon_transition_sevenA:
    if MapNumber == 7.1:
        scene map7_1 onlayer master
    elif MapNumber == 7.2:
        scene map7_2 onlayer master

    menu:
        "Take upper route" if MapNumber == 7.2:
            $ MapNumber = 8
            jump dragon_tile_eightA
        
        "Take lower route" if MapNumber == 7.1:
            $ MapNumber = 8
            jump dragon_tile_eightA

label dragon_transition_sevenB:
    if MapNumber == 7.1:
        scene map7_1 onlayer master
    elif MapNumber == 7.2:
        scene map7_2 onlayer master

    menu:
        "Take upper route" if MapNumber == 7.2:
            $ MapNumber = 8
            jump dragon_tile_eightB
        
        "Take lower route" if MapNumber == 7.1:
            $ MapNumber = 8
            jump dragon_tile_eightB

label dragon_tile_eightA:
    "{i}The Pack emerges through the tree line, coming across a shimmering lake. The air feels oddly inviting, the surrounding forest growing quiet.{i}"

    df "...we're here."

    c "Oh boy! We made it to the Lake!"

    "{i}The animals all move closer to the lake, stopping right at the water's edge. Dragonfly looks at the others.{i}"

    df "Whatever comes next friends, it has been an honor to travel with you all."

    "{i}Hummingbird crackles a smile, but tries to hide it by rolling their eyes.{i}"
     
    hb "Wow, any sweeter and I would be able to get nectar from you."

    "{i}They all stand there, a lingering question in the air: What now?{i}"

    "{i}Dragonfly takes a deep breath, and then starts flying close over the Lake, brushing their legs against the water's surface here and there.{i}"

    "{i}Hummingbird sighs and shivers slightly, before also starting to slowly fly over the lake. Seeing the other two moving, Coyote quickly joins in, swimming the doggie paddle.{i}"

    "{i}As they journey out to the center of the Lake, an ominous feeling that something else is under the water starts to creep through them. Reaching the center, the fly or tread water in silence. Just waiting.{i}"

    "{i}The animals in the water are the first to feel it. The water underneath them, slowly but surely being sucked downward.{i}"
    
    "{i}They try to swim upward, but the vacuum of water only grows strong. Then those above the lake feel it as well, as even the air is being sucked into the center of this lake.{i}"

    "{i}As the animals try to fight it, it seems to be no use. Dragonfly tries to escape the force by flying up with all their might, but at the peak of their arc, seems to have some sort of realization.{i}" 
    
    "{i}They stop buzzing their wings, and let themselves be moved downward. Down, down, down, into the depths of the Lake. Whether they like it or not, the rest of the Pack soon follows them.{i}"
    "{i}As they all sink down, the cold water enveloping them, they're taken by an all-encompassing darkness.{i}"

    $ DFsighting += 1
    $ Csighting += 1
    $ HBighting += 1
    $ RunCount += 1
    $ DragonflyBranch = False
    
    scene black with fade
    
    jump ending

label dragon_tile_eightB:
    "{i}The Pack emerges through the tree line, coming across a shimmering lake. The air feels oddly inviting, the surrounding forest growing quiet.{i}"

    df "...we're here."

    b "Be careful. We don't know what will happen here."

    "{i}The animals all move closer to the lake, stopping right at the water's edge. Dragonfly looks at the others.{i}"

    df "Whatever comes next friends, it has been an honor to travel with you all."

    r "Here here!" 
    
    "{i}Raccoon smiles a laughs loudly.{i}"

    "{i}They all stand there, a lingering question in the air: What now?{i}"

    "{i}Dragonfly takes a deep breath, and then starts flying close over the Lake, brushing their legs against the water's surface here and there.{i}"

    "{i}Bear and Raccoon quickly follow, Bear faring quite well in the water. Raccoon behind them momentarily struggles to swim, but quickly finds their stride and follows after, using their tail as a propeller.{i}"

    "{i}As they journey out to the center of the Lake, an ominous feeling that something else is under the water starts to creep through them. Reaching the center, the fly or tread water in silence. Just waiting.{i}"

    "{i}The animals in the water are the first to feel it. The water underneath them, slowly but surely being sucked downward.{i}"
    
    "{i}They try to swim upward, but the vacuum of water only grows strong. Then those above the lake feel it as well, as even the air is being sucked into the center of this lake.{i}"

    "{i}As the animals try to fight it, it seems to be no use. Dragonfly tries to escape the force by flying up with all their might, but at the peak of their arc, seems to have some sort of realization.{i}" 
    
    "{i}They stop buzzing their wings, and let themselves be moved downward. Down, down, down, into the depths of the Lake. Whether they like it or not, the rest of the Pack soon follows them.{i}"
    "{i}As they all sink down, the cold water enveloping them, they're taken by an all-encompassing darkness.{i}"
    
    $ DFsighting += 1
    $ Rsighting += 1
    $ Bsighting += 1
    $ RunCount += 1
    $ DragonflyBranch = False
    
    scene black with fade
    
    jump ending

label ending:
    if RunCount == 1:
        "..."

        "\"Who are you?\""

        "{i}In the darkness, a pinprick of light appears.{i}"

        "Who asked that question?"

        "{i}The light feels warm amidst the cold darkness.{i}"

        "{i}The light grows and grows, and with it the warmth, until you are amidst a white hot burning expanse of bright light.{i}"

        "{i}The heat doesn't burn you. You're not even sure you can be burned. But it feels…hostile.{i}"

        "\"I still recognize you, defiler,\" {i}comes a voice. It rumbles like an earthquake and whips around you like a tornado.{i}"

        "\"You have not been forgiven.\""

        "{i}You feel a pressure exerted on you, on whatever representation of yourself exists in this strange dreamscape.{i}"

        "\"Bring me more memories, and we shall see.\""

        "{i}You feel yourself being torn apart and spread, spread across the vast expanse of sky that shimmers above the forest. As the Lake fades into the distance, everything goes black.{i}"
        
        scene black with fade

        jump starting_choice

    elif RunCount == 2:
        "..."

        "\"Who are you?\""

        "Did that question come from someone else? Or did you whisper it to yourself?"

        "{i}You lie in darkness once more. You try to see, try to feel, but are unable to distinguish sensation and memory.{i}"

        "{i}You wait.{i}"

        "{i}...{i}"

        "\"You have changed your scent.\""

        "{i}You look down, and see a massive koi fish with shimmering butterfly wings. It swims through the dark expanse below, emitting a hot light that cuts through and pierces your soul.{i}"

        "\"But I can still recognize you.\""

        "{i}The light swells from the Fish Fairy, reaching a blinding point.{i}"

        "\"I remember you being there. At the scene where one of my own was slain.\""
        
        "\"How dare you show yourself here!\""

        "{i}The Fish Fairy lunges upwards towards you, mouth agape.{i}"

        "\"Bring me more memories!\""

        "{i}In one quick motion, the mouth of the koi Fish closes around you, leaving you once again in darkness.{i}"

        "{i}You feel yourself being broken, being shattered and spread once more.{i}"

        "What will the Lake have in store next?"
        
        scene black with fade

        jump starting_choice

    elif RunCount == 3:
        "..."
        "..."
        "{i}You've never felt quite so alone.{i}"

        "{i}As you soak in the familiar cold darkness, you lie in wait. Just waiting and waiting.{i}"

        "{i}After a while, You start reflecting on your journey.{i}"

        "You have come so far. Your Pack has come so far."

        "Are the two even different?"

        "Because of course, without You there would be no Pack. And if not for your Pack, You wouldn't be here."

        "You've all been growing and learning, creating new memories together."

        "And you don't have any other memories. So these ones must be yours."

        "\"At last.\""

        "{i}You turn around, coming face to face with the Fish Fairy again. This time, they are a much smaller size, only a little larger than you.{i}"

        "\"You are…different. I no longer recognize you as what you once were.\""

        "{i}The Fish Fairy holds out their fins, and you see a small mote of light held in them. A memory.{i}"

        "{i}The light rises into the air, and grows larger. Within the light you see an image.{i}"

        "{i}You see yourself. You had forgotten what you used to be, what you used to look like.{i}"

        "{i}A dead animal lies nearby, with you standing over it. Why is it there? What were you doing?{i}"

        "{i}As you look at your own expression, you fail to remember what you were doing there. Did you kill that animal? If so, why? Or did you just come across it, having nothing to do with its death?{i}"

        "{i}Whatever the answer was, it certainly didn't change the outcome.{i}"

        "{i}You look back at the Fish Fairy.{i}"

        "\"You have changed. The person who was there is gone. In their place, stands you. That seems reason enough to let you go.\""

        "{i}The light grows brighter and brighter, as a more gentle warmth washes over you. As everything fades to white, the last thing you remember is the smell of soil and pine.{i}"

        scene white with fade

        jump epilogue

label epilogue:
    scene white
    "..."
    
    "\"Who are you?\""

    "{i}This question is the first thing you think as you wake up.{i}"

    "{i}You are a person, a whole soul within your own body.{i}"

    "{i}But You are not the same as before. Your Pack has changed You. You remember what they remember, and you are as they were.{i}"

    "{i}In our own way, we all have a Pack within us. That group of creatures that talk and snarl and love.{i}"

    "{i}But you are You. Wholly, unique You. And You are here.{i}"

    "{i}Time to go make some more memories.{i}"

    "Thank you for playing!"

    return


#------------------------------------------
#- End Dragonfly Branch
#------------------------------------------




# Using return ends the game but I forgot how change it so it ends depending on a route
   


