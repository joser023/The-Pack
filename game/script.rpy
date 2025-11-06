# The script of the game goes in this file.

# Declare Character variables here so it is easier to call them when making the dialogue
# The color part changes the text color of that characters specifically so change it to what you like
define n = Character("Narrator")
define t = Character("Tree")
define p = Character("Pixies")


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
default HBighting = 0

# Checks to see how many time Coyote appears
default Csighting = 0

# Checks to see how many time Dragonfly appears
default DFsighting = 0


default RunCount = 0  #Tally how many branches the player has done or started

 # Use this to track which branches the players have completed or have not
default RaccoonBranch = False 
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

        "Follow the Raccoon" if RaccoonBranch is False:
            jump Choose_Raccoon
        "Follow the Bear" if BearBranch is False:
            jump BTR_Tile6
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
    "Do not be fooled however, the Raccoon is agile and acrobatic. Furthermore it carries the innate trait of{i} magic pocket{/i}"

    "Choose the Raccoon?"
    menu: 
        "Yes":
            jump Begin_Raccoon
        "No":
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
    
    " The Bear shoots a glance at the Bird. The bird mumbled the rest under its beak."
    
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
    b "Hey Bird, where have… You… Been…"
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

    "The Dragonfly, the aerial assassin of the insect kingdom"
    "The Dragonfly sees many things, its eyes can detect the motions of the unknown. Many call it{i} Future sight{/i}. "

    "Choose the Dragonfly"
    menu: 
        "Yes":
            jump Begin_Dragonfly
        "No":
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