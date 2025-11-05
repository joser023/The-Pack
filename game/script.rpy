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
        "No":
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
        "No":
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
    menu:
        "Take the upper route":
            jump dragon_tile_two
        
        "Take the lower route":
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
    menu:
        "Take the upper route":
            jump dragon_tile_three
        
        "Take the lower route":
            jump dragon_tile_three

label dragon_tile_three:
    "{i}Slightly ruffled from the previous gale, Dragonfly travels onward through the forest.{i}"

    df "Mmm...it's good to be able to fly without issue again. Hopefully this weather holds up."

    df "I wonder why I didn't feel that it would be that windy..."

<<<<<<< Updated upstream
    df "I guess it just wasn't important enough for me to see it through [[Foresight]."

    df "After all, I got through those winds alright. So it all worked out in the end."

    df "I'm sure if there's something really bad to worry about, the universe would let me know somehow."

    df "Although, perhaps I should be a little more cautious in the future."

    df "Winds like those make me wish that Hummingbird was around. Even if they always seem so upset."

    df "A little insect like me could surely use some company on this lone journey."

    df "Well, I'm sure I'll run into someone eventually. All in good time."

    jump dragon_transition_three

label dragon_transition_three:
    menu:
        "Take the upper route":
            jump dragon_tile_four
        
        "Take the lower route":
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

            r "Well...I guess I could've asked you first before jumping in...sorry about that..."

            r "Bah! I knew exactly what I was doing."
            jump bear_raccoon

        label look_fine:
            df "You both look perfectly fine to me!"

            r "Thank you! See what I was saying Bear about being a little more positive?"
            jump bear_raccoon

        label bear_raccoon:
            b "All right, whatever. We lost a lot of light thanks to your stunt earlier, so we should keep moving."

            df "As you wish. I'm just so glad I came across you two. I think this will be a wonderful journey together."
            jump dragon_transition_four

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

            hb "{i}shrugs{i} Not entirely sure what there is to be happy about, but you're right. We're stuck together, whether I like it or not."

            hb "{i}shrugs{i} The more the merrier, I suppose. Thats what they say, at least."

            c "Then it's settled! We travel!"
            jump dragon_transition_four

label dragon_transition_four:
    menu:
        "Take the upper route":
            jump dragon_tile_five
        
        "Take the lower route":
            jump dragon_tile_five

label dragon_tile_five:
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

        hb "{i}sighs{i} I wasn't sure if you'd actually do it. Alright then, I guess this is happening."

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

        "{i}Hummingbird shakes their head, but bites their tongue before they say anything to Coyote, electing instead to hop back over to the far side of the stump.{i}"

        hb "Typical. {i}Chirps disapprovingly.{i} This is why it hardly does any good to travel with others."

        df "There there, it's all right Coyote. It's ok to be afraid."

        c "But I let you all down! I'm not a leader. I can't help anyone."

        df "That's not true! Sometimes we are faced with things that we don't feel ready for. It is ok to rely on others for strength when we feel uncertain. But you are also strong by yourself, and when the time comes for you to act, I'm sure you'll be ready. {i}smiles.{i}"

        "{i}Coyote sniffs and nods.{i}"

        df "Besides, the rain will surely be over soon [[Foresight]. All we need to do is wait."

        hb "Doesn't seem very likely to me."

        "{i}As they sit in the stump, the rain shows no signs of letting up. With each hour that passes, Hummingbird looks more smug, and Dragonfly looks more confused. After most of the day has passed, the rain finally stops, and the Pack continues onward.{i}"
        jump dragon_transition_five

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

    b "{i}Sigh.{i} Look, just be more careful, ok? Stay behind me."

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
    jump dragon_transition_five

label dragon_transition_five:
    menu:
        "Take the upper route":
            jump dragon_tile_six
        
        "Take the lower route":
            jump dragon_tile_six

label dragon_tile_six:
    "{i}As the Pack makes their way down a small hill, they find themselves facing a large patch of brambles. The sharp thorns look very intimidating.{i}"

    df "Interesting. Will you all be ok crossing this?"

    hb "{i}rolls eyes.{i} Sure I can. Just make sure we're not going to be slowed down by the pup."

    c "Umm...I'm not sure. It looks dangerous..."

    c "Hold on, what did you say Hummingbird?"

    r "This looks like a job for a professional squeezer! Put me in coach, I'm ready."

    b "Slow and steady, Raccoon. Let's all make sure we stick together."

    df "Quiet down everyone! Let us focus on the task at hand."

    "{i}As the Pack approaches the briar, there's a sudden low rumbling noise. In a flash, the animals are all thrown backward, as dirt and earth explodes out from under them. The plants roil for a moment, as emerging from the tangle is a walking mass of thorns and bushes, an angry Briar Elemental.{i}"

    hb "Ack! You couldn't have seen this coming, huh Dragonfly?!"

    c "Oh man. What do we do? What do we do?"

    b "Get back everyone! Do your best to stay out of its range."

    r "No way! I can handle this. Trust me!"

    menu:

        "Squeeze through the briar and make a run for it.":
            jump briar_squeeze

        "Goad the elemental into leaving the thorn patch.":
            jump briar_goad

        "Fight the elemental [[Strength].":
            jump briar_strength

        "Run around the elemental quickly to confuse it [[Agility].":
            jump briar_agility

        "Blow the vines aside and run through [[Wind Gale].":
            jump briar_gale

    label briar_squeeze:
        df "Quickly! Everyone make a run for it!"

        "{i}The Pack manages to squeeze, trample, or fly their way through the brush, with the elemental right on their heels. They get pricked and poked, but ultimately make it out ok.{i}"
        jump dragon_transition_six

    label briar_goad:
        df "We need to get it away from the briar patch! Then it'll be out of our way!"

        r "Don't worry! I'm a master of distraction! Hey you big ugly blackberry bush! Over here!"

        "{i}Coyote looks nervous, but starts yipping at the elemental.{i}" 
        
        c "C-come and get us! I b-bet you can't catch me!"

        "{i}As the elemental takes a step out of the briar patch to pursue the animals, it starts to lose its form, as it disconnects from the vines and bushes. Seizing the moment, the Pack makes a quick getaway through the briar patch.{i}"
        jump dragon_transition_six

    label briar_strength:
        df "Go Bear! We'll be right behind you!"

        "{i}Bear rushes forward into the brambles, flattening them down as they run. They rear onto their hind legs, and slam their front paws into the elemental with all their might [[Strength].{i}"

        "{i}The others take this opportunity to run past the elemental, while Bear growls and grapples with it. Once they're through, Raccoon calls out to Bear.{i}"

        r "We're good! Get out of there Bear!"

        "{i}Bear manages to untangle themselves from the grasp of the elemental, and runs after the others, as they run until the elemental is far from sight.{i}"
        jump dragon_transition_six

    label briar_agility:
        df "Raccoon, go show it your strength!"

        r "Aye aye!"

        "{i}Raccoon runs into the patch, easily dodging the strikes from the elemental’s thorny arms. They run around the elemental over and over again, weaving in and out of its reach [[Agility].{i}" 
        
        "{i}After a few minutes, the elemental seems sufficiently tangled up and confused. Raccoon grins proudly to the others, and they all quickly make their way through the briar patch, past the dazed elemental.{i}"
        jump dragon_transition_six

    label briar_gale:
        "{i}Dragonfly looks stunned and overwhelmed. Hummingbird looks between all the animals and the elemental, and huffs.{i}"

        hb "All right everyone, stay back!"

        "{i}As the others take a step back, Hummingbird starts beating their wings faster and faster. As they do, large gusts of wind start to blow out from them, until they become almost gale force [[Wind Gale].{i}" 
        
        "{i}Hummingbird directs these winds towards the patch of brambles, blowing them out of the way and creating a clear path around the elemental.{i}"

        hb "Go! Quickly!"

        "{i}Coyote looks at Dragonfly, then back at Hummingbird, seeming nervous. Then they take a deep breath, and start running through the path created. Dragonfly quickly follows behind them, and Hummingbird brings up the rear of the Pack, as they safely clear the brush.{i}"
        jump dragon_transition_six

label dragon_transition_six:
    menu:
        "Take the upper route":
            jump dragon_tile_seven
        
        "Take the lower route":
            jump dragon_tile_seven

label dragon_tile_seven:
    "{i}The Pack have settled around a campfire for the night, preparing themselves for what's in store tomorrow.{i}"

    "{i}Dragonfly stares into the fire thoughtfully.{i}"

    df "Tomorrow will likely be the end of our journey [[Foresight]."

    "{i}Bear nods, sniffing the air.{i}" 

    "They're right. We're close. [[Pathsense]."

    c "{i}Coyote looks to Dragonfly.{i} Are you alright?"

    r "That's a good thing, right?"

    df "Sort of. It's just that...I always rely on my sight to warn me. To guide me. But recently it's felt a bit more...unreliable."

    hb "So, what? You're not happy because your little unrealistic predictions turned out to not come true?"

    r "Wait, so your eyes aren't working right?"

    df "I suppose that's one way of putting it. I see us reaching the end of our journey tomorrow, and everything being all right. But for the first time in a while I guess I feel...worried."

    "{i}Hummingbird remains quiet for a moment.{i}" 
    
    hb "Yeah, well there's a lot to be worried about."

    b "It's natural to be worried. That's what keeps us alive, nothing wrong with it."

    df "You would certainly know best about that. It's just that..."

    df "...I've never needed worry to stay alive so far. I enjoy that, and I want to hold onto it. I don't think I'm ready to let that go."

    df "...I miss when I knew everything would turn out fine. It's hard to deal with worry. But I DO want to help everyone be safe. So I suppose I'll have to rely a bit more on the present, and a bit less on the future."

    "{i}The other animals nod in acknowledgement, then sit back a bit and enjoy the heat of the fire. Dragonfly starts to flutter their wings gently against each other, creating a low humming sound.{i}"

    hb "And they call me the one who hums. You encroaching on my turf?  {i}they say tauntingly.{i}"

    b "Must you do that? I'm trying to keep watch."

    "{i}Dragonfly brings their hum so low that only they can hear it.{i}"

    hb "{i}sigh{i} Jeez, it was just a joke. You can do whatever you want, I don't care."

    r "I thought it was nice." 
    
    "{i}Raccoon pulls a marshmallow and stick out of their pocket and starting to roast it by the fire [[Magic Pocket].{i}"

    df "You did well earlier. I was very glad to have you with us."

    hb "Well...I guess you helped as well. I just wanted to make sure everyone wasn't being dumb."

    r "Really?! {i} Raccoon gets so excited they almost drop their marshmallow in the fire.{i}"

    df "{i}Chuckles.{i} Yes. And you played a vital role in keeping everyone safe."

    df "I just think that maybe you don't realize how what you say affects others."
    df "I just think that maybe a certain animal was right about you loving to charge into danger a little too much."

    hb "...how do you mean exactly?"

    "{i}Raccoon looks over towards where Bear is.{i}"
    r "Well, they're always saying that."

    df "Just that, sometimes even if something is true, saying it can lead to the ones we care about getting hurt. You don't want to hurt any of us, right?"
    df "Why do you think they're doing that?"

    hb "...no. I don't. I just want others to-"

    r "I don't know...I guess because they care about me."

    df "-to think like you, right?"
    df "They do indeed. We all do. And that's why we try to help each other make good decisions. Do you understand?"


    hb "I guess. I just think it would be easier if everyone was objective all the time."

    df "But does it seem like it's been easier for them to do that? {i} Dragonfly gestures to Coyote.{i}"

    hb "...I guess not."

    hb "...sorry."

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

    b "Listen. Just leave the protecting to me. There are plenty of other things you're good at."

    b "I've seen your strength now. I know that you care, and I think you'll do a great job and protecting people and being strong, in your own way."

    r "Really? You mean it? {i} they beam.{i}"

    b "Yes, I do," 
    
    "{i}Bear can't help but crack a grin{i}"

    b "Now pipe down and finish your marshmallow."

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

    hb "I suppose if you call just looking at everyone else 'being decisive', then sure."

    "{i}Dragonfly looks back at Hummingbird, looking a bit disappointed.{i}"

    "{i}Hummingbird clucks their tongue disapprovingly at Dragonfly's statement, but seems to hold back from saying anything.{i}"

    df "And at any rate, you're a lot more adult than you would believe."

    c "I was just listening to myself instead of others. Is that what you're talking about?"

    df "Yes, that's it exactly! Trust yourself, and you can act independently when the moment calls for it."

    c "hmm...I'm not sure I could do that for a lot of the time. I think I might still need others for help."

    c "I think I can do that. I think I can do that! I can be independent! I can help others figure things out!"

    df "{i}Chuckles.{i} All in good time, all in good time."

    "{i}Dragonfly looks around the campfire at the other two animals beside them.{i}"

    df "All right everyone. Tomorrow..."
    menu:

        "Be open.":
            jump fire_open

        "Be careful.":
            jump fire_careful

    label fire_open:
        df "...be open to whatever we find. Tomorrow our journey ends, so take in whatever the universe has in store for us."

    label fire_careful:
        df "...be careful when we approach. Tomorrow our journey ends, and we must greet whatever awaits us with alert and undulled senses."

    "{i}The rest of the animals murmur in agreement, before going to sleep by the warmth of the campfire.{i}"
    jump dragon_transition_seven

label dragon_transition_seven:
    menu:
        "Take the upper route":
            jump dragon_tile_eight
        
        "Take the lower route":
            jump dragon_tile_eight

label dragon_tile_eight:
    "{i}The Pack emerges through the tree line, coming across a shimmering lake. The air feels oddly inviting, the surrounding forest growing quiet.{i}"

    df "...we're here."

    c "Oh boy! We made it to the Lake!"

    b "Be careful. We don't know what will happen here."

    "{i}The animals all move closer to the lake, stopping right at the water's edge. Dragonfly looks at the others.{i}"

    df "Whatever comes next friends, it has been an honor to travel with you all."

    "{i}Hummingbird crackles a smile, but tries to hide it by rolling their eyes.{i}"
     
    hb "Wow, any sweeter and I would be able to get nectar from you."

    r "Here here!" 
    
    "{i}Raccoon smiles a laughs loudly.{i}"

    "{i}They all stand there, a lingering question in the air: What now?{i}"

    "{i}Dragonfly takes a deep breath, and then starts flying close over the Lake, brushing their legs against the water's surface here and there.{i}"

    "{i}Bear and Raccoon quickly follow, Bear faring quite well in the water. Raccoon behind them momentarily struggles to swim, but quickly finds their stride and follows after, using their tail as a propeller.{i}"

    "{i}Hummingbird sighs and shivers slightly, before also starting to slowly fly over the lake. Seeing the other two moving, Coyote quickly joins in, swimming the doggie paddle.{i}"

    "{i}As they journey out to the center of the Lake, an ominous feeling that something else is under the water starts to creep through them. Reaching the center, the fly or tread water in silence. Just waiting.{i}"

    "{i}The animals in the water are the first to feel it. The water underneath them, slowly but surely being sucked downward.{i}"
    
    "{i}They try to swim upward, but the vacuum of water only grows strong. Then those above the lake feel it as well, as even the air is being sucked into the center of this lake.{i}"

    "{i}As the animals try to fight it, it seems to be no use. Dragonfly tries to escape the force by flying up with all their might, but at the peak of their arc, seems to have some sort of realization.{i}" 
    
    "{i}They stop buzzing their wings, and let themselves be moved downward. Down, down, down, into the depths of the Lake. Whether they like it or not, the rest of the Pack soon follows them.{i}"
    "{i}As they all sink down, the cold water enveloping them, they're taken by an all-encompassing darkness.{i}"






#------------------------------------------
#- End Dragonfly Branch
#------------------------------------------


# Using return ends the game but I forgot how change it so it ends depending on a route
    return
