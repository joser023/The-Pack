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
       "Follow the Bear" if BearBranch is False:
           jump Choose_Bear
       "Follow the Dragonfly" if DragonflyBranch is False:
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


    # Mark that the player has started the Raccoon branch
    $ RacoonBranch = True
    $ RunCount += 1


    # Tile 1


    "The forest hums softly in its slow awakening. Shafts of gold cut through the canopy, painting the moss in dancing patches of light."
    "The smell of wet bark and clover lingers in the air. Somewhere, a stream murmurs like a forgotten song."


    r "Mmm... another perfect day for heroics and snacks."


    "Raccoon stretches and yawns, then rolls onto their back, watching sunlight flicker between branches."


    r "Had the weirdest dream last night... there was a lake. Big, shiny, like a mirror that swallowed the sky."
    "They pause, squinting at the treetops."
    r "I think something was waiting for me there."


    "They brush leaves from their fur and grin."


    r "Or maybe it was just me admiring my reflection again. Hard to tell sometimes."


    "They hop upright and take a few steps toward the clearing, humming tunelessly."


    r "Anyway, dream or not, sounds like destiny's calling! And if destiny's shiny, then even better."


    "They look around, tail flicking eagerly."


    r "Now... which way was that lake again?"


    # Tile 2


    "Further down, the ground softens to mud. A glint of silver flashes beneath the surface, half-buried like treasure waiting to be found."


    r "Oh-ho-ho! Jackpot! The forest rewards those with impeccable taste."


    "They crouch, eyes bright."


    r "Careful... slow... stealth mode."


    "They leap forward."


    "WHOOSH!"


    r "Wha-AHHH! No! This is NOT treasure! It's-ugh-it's... sticky! Gross!"


    "They thrash as thick resin threads stretch between their paws."


    r "Why do all good things turn into bad ideas?"


    "They struggle, half-laughing, half-panicking."


    r "Okay, Raccoon. Think. Time to deploy your legendary training. Which you... definitely have."


    menu:
        "Use Agility to twist free":
            "Raccoon twists, somersaults, and pops free with a dramatic spin."
            r "Ha! And they said gymnastics class was pointless!"
        "Use Magic Pocket to escape":
            "They dig into a small satchel tied to their fur, pulling out a spoon, a feather, and finally a shiny pebble."
            r "Aha! The magic pebble of... goo-dissolving? Let's find out!"
            "They tap the sap with the pebble; it melts away like sugar in tea."
            r "Science!"


    "They stand, covered in flecks of mud and resin."


    r "Either the cleverest animal in the forest... or the dumbest."


    "They glance back at the sticky patch, where sunlight still glints off the sap."


    r "Still... that shine looked just like the one from my dream."


    "Their grin fades a little."


    r "Maybe not everything shiny wants to be found."


    # Tile 3


    "The air smells sweeter as the forest opens again. Light plays on the leaves; each rustle feels like a whisper from something watching kindly-or curiously."


    r "Note to self: shiny equals sticky. Got it. I totally learned my lesson. Probably."


    "They shake out their paws, pretending to march proudly forward."


    r "Bet Bear would've told me to 'use my head before my tail.'"


    "They lower their voice, mimicking Bear."


    r "\"Raccoon, you can't solve everything with jokes.\""


    r "Counterpoint: jokes make everything better."


    "They chuckle, then sigh."


    r "But... maybe they're right sometimes. I keep diving into things headfirst. One day that's gonna hurt someone else, not just me."


    if RunCount > 1:
        r "At least I'm starting to think before leaping. That's progress, right? Baby steps. Stylish baby steps."


    "They stop, hearing a rustle in the underbrush."


    r "Hmm? Sounds like company."


    "They perk up, ears twitching with excitement."


    r "Finally! Maybe someone who appreciates my charm."


    # Tile 4 - choose companion pair


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


    tl "You two arguing already? We just met."


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


    tl "We're always on our way somewhere. Hopefully not to our deaths."


    c "Don't say that! The forest is full of cool stuff! Maybe treasure! Maybe ghosts!"


    tl "That's not helping."


    r "Perfect. I like this dynamic already. Let's find out what shiny mistake waits for us next."


    # Tile 5A


    "The trio stops near a massive hollow tree whose center hums when they speak."


    c "Whoa, check this out!"


    r "Echo! Echo! Echooo!"


    "Their voice bounces back, slightly distorted."


    r "See? The forest loves my voice."


    tl "That... doesn't sound like just an echo."


    c "Maybe it's forest ghosts! Hi ghosts!"


    r "If they like jokes, they're welcome."


    "The echo replies faintly, barely more than a breath."


    "\"Welcome...\""


    tl "Okay, that's not funny."


    r "Maybe it's just memory. Forests remember laughter too."


    c "Creepy but poetic."


    tl "Let's move before the memories start answering back."


    r "You're no fun."


    "They move on, laughter fading into the hollow's hum."


    # Tile 6A


    "A roaring river cuts through the forest, water sparkling violently in moonlight."


    r "Finally! A natural water slide!"


    tl "Absolutely not."


    c "It does look fun..."


    tl "I take that back-absolutely not, for both of you."


    menu:
        "Raccoon leads, using Agility across the rocks":
            "Raccoon leaps from rock to rock, paws slipping on the spray but somehow keeping their balance."
        "Turtle leads, using Swimming to steady the current":
            "Turtle slips into the water, steady as stone, letting the others use their shell as a moving bridge."
        "Coyote leads, using Scent to find a calmer crossing":
            "Coyote lifts their nose, tracing the air until they find a narrower, calmer stretch of river to cross."


    "Midway, a wave almost knocks Raccoon off; Turtle shouts instructions while Coyote barks encouragement."


    r "Remind me to never underestimate physics again!"


    tl "Remind me to travel alone next time."


    c "But then who'd bring the snacks?"


    "They all laugh as they reach the opposite shore, dripping but alive."


    # Tile 7A


    "Later, the Pack settles by a quiet stream. Fireflies drift like embers from another world."


    r "Finally, the perfect atmosphere for reflection... or snacks. Probably both."


    c "You always think with your stomach."


    tl "And yet we're alive, somehow."


    "Raccoon grins, piling twigs into a bonfire."


    r "Alright, no moping tonight. We survived the sticky, the scary, and the soggy. We deserve a party."


    "They light the fire, sparks rising into the starlight. Someone laughs. Someone groans. But they stay."


    r "Look around, folks. For once, the forest doesn't feel like it's judging us."


    tl "Give it time."


    r "Nah. Tonight it listens."


    "Raccoon starts humming, spinning clumsily around the fire. The others eventually join-awkwardly, reluctantly, sincerely."


    "The laughter feels alive. Even the turtle relaxes a little."


    r "You know... I think laughter's like light. Doesn't matter how dark the forest gets-it still finds a way through."


       # Tile 8A - Ending


    "The Pack was able to navigate through the forest, following the faint pull of Turtle's {i}tidal memory{/i} as it tugged them down the trail."
    "In a short span of time, they emerged from the trees and stood in front of a giant lake."


    r "So this is it."
    tl "I remember this place. There should be a lake somewhere up ahead."
    r "Feeling lucky and wanting to dive?"
    tl "No. This one's different."
    c "Different how? Looks like free bath time to me."


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


    scene black with fade


    return






# -----------------------------------------
# Route B - Bear & Hummingbird
# -----------------------------------------
label Raccoon_RouteB:


    # Tile 4B


    "A deep rumble echoes from the trees, followed by a high-pitched complaint."


    hb "I swear, Bear, if we walk ten more steps without finding food, I'm going to combust."


    b "You say that every ten steps."


    r "Hey! Speaking of combusting-look who I ran into!"


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


    "Bear grumbles; Hummingbird mutters under their breath; Raccoon just laughs."


    r "Alright, grumpy squad, I'll lead. Someone's gotta bring personality to this trio."


    hb "We're doomed."


    # Tile 5B


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


    "They continue walking, light flickering underfoot. For a moment, all three are quiet-then Raccoon hums a tune, breaking the tension."


    r "If I die glowing, make sure I look fabulous."


    hb "You already look ridiculous."


    r "Close enough."


    # Tile 6B


    "A meadow of luminous flowers sways under a faint mist."


    hb "Pretty. Probably lethal."


    b "Stay back. The smell's off."


    r "Oh come on, they're just flowers. Friendly ones. Right?"


    b "No."


    hb "Definitely not."


    "Raccoon pulls a scrap of cloth from their magic pocket and ties it around their face."


    r "Mask time! Safety first-fashion second."


    hb "You're ridiculous."


    r "Ridiculously prepared."


    b "Hummingbird, clear the air with Wind Gale."


    "Wind surges through the meadow; the pollen scatters and the air clears."


    r "See? Teamwork! We're unstoppable."


    hb "Until the next stupid decision."


    b "At least they're learning."


    r "Was that a compliment?"


    b "Don't push it."


    # Tile 7B


    "Later, the Pack settles by a quiet stream. Fireflies drift like embers from another world."


    r "Finally, the perfect atmosphere for reflection... or snacks. Probably both."


    hb "Barely survived getting here."


    b "Could be worse."


    "Raccoon grins, piling twigs into a bonfire."


    r "Alright, no moping tonight. We survived the sticky, the scary, and the soggy. We deserve a party."


    "They light the fire, sparks rising into the starlight. Someone laughs. Someone groans. But they stay."


    r "Look around, folks. For once, the forest doesn't feel like it's judging us."


    b "Give it time."


    r "Nah. Tonight it listens."


    "Raccoon starts humming, spinning clumsily around the fire. The others eventually join-awkwardly, reluctantly, sincerely."


    "The laughter feels alive. Even Hummingbird smiles faintly. Even Bear relaxes."


    r "You know... I think laughter's like light. Doesn't matter how dark the forest gets-it still finds a way through."


           # Tile 8B - Ending


    "The Pack was able to navigate through the forest using Bear's {i}path sensing{/i} string, which had returned to them the night before."
    "The thread guides them through the last stretch of trees until the forest opens up around a wide, shimmering lake."


    r "We actually made it."
    hb "Yeah. And it feels wrong."
    b "Stay close. We don't know what will happen here."


    "They all move closer to the water's edge, stopping where damp earth gives way to sand."
    hb "Whatever comes next, I'd at least like to not drown."
    r "I'll do my best to keep us all fabulously afloat."


    "Bear wades in first, testing the depth. Raccoon follows, splashing nervously, while Hummingbird hovers just above the surface."
    "For a moment, the water around them is strangely calm."


    "Then they feel it-the water underneath them slowly, surely being pulled downward."
    hb "Do you feel that?"
    r "I'm trying, but I'm being pulled in! Bear, I think we're-"


    "The pull becomes a sudden, violent drag. The lake's surface warps, funneling everything toward its dark center."
    b "Get out of the water!"


    "They fight to swim back, but every stroke only drags them deeper into the invisible current."
    "One by one, they're swallowed by the lake, their shapes vanishing beneath the churning water."


    scene black with fade


    return


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


