# The script of the game goes in this file.

##################### Declare characters used by this game. The color argument colorizes the #####################
######################################## name of the character. ##################################################

define h = Character('Hammett' , color="#ac28ed")
define e = Character('Ethan Alterberth' , color="#0be663")

define Y = Character("You")
define y = Character("[povname]")

define persistent.ethan_cg_1_unlocked = False  

############################################## Declare images needed #############################################

#================================================= CHAR: Hammett ================================================#
#_______________________________________________  OUTFIT: Doctor  _______________________________________________#
#----------------------------------------------- POSE: pose_normal ----------------------------------------------#
#++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: smiling +++++++++++++++++++++++++++++++++++++++++++++#
image Hammett_pose_normal = Image("Hammett_pose_normal.png")
image Hammett_pose_normal_slight_smile = Image("Hammett_pose_normal_slight_smile.png")
image Hammett_pose_normal_big_smile = Image("Hammett_pose_normal_big_smile.png")
image Hammett_pose_normal_smile_talking = Image("Hammett_pose_normal_smile_talking.png")
image Hammett_pose_normal_slight_smile_talking = Image("Hammett_pose_normal_slight_smile_talking.png")
image Hammett_pose_normal_big_smile_talking = Image("Hammett_pose_normal_big_smile_talking.png")

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: akward +++++++++++++++++++++++++++++++++++++++++++++#
image Hammett_pose_normal_akward = Image("Hammett_pose_normal_akward.png")
image Hammett_pose_normal_akward_panic = Image("Hammett_pose_normal_akward_panic.png")
image Hammett_pose_normal_akward_talking = Image("Hammett_pose_normal_akward_talking.png")

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: funny ++++++++++++++++++++++++++++++++++++++++++++++#
image Hammett_pose_normal_funny_face1 = Image("Hammett_pose_normal_funny_face1.png")
image Hammett_pose_normal_funny_face2 = Image("Hammett_pose_normal_funny_face2.png")

#================================================ CHAR: Ethan ===================================================#
#______________________________________________  OUTFIT: casual  ________________________________________________#
#---------------------------------------------- POSE: normal_pose -----------------------------------------------#
image Ethan_normal_pose = Image("Ethan_normal_pose.png")

#___________________________________________  OUTFIT: hospital gown _____________________________________________#
image Ethan_normal_pose_ingown = Image("Ethan_normal_pose_ingown.png")
image Ethan_normal_pose_ingown_talking = Image("Ethan_normal_pose_ingown_talking.png")

#---------------------------------------------- POSE: questioning -----------------------------------------------#
image Ethan_questioning_ingown_talking = Image("Ethan_questioning_ingown_talking.png")
image Ethan_questioning_ingown_suspicious = Image("Ethan_questioning_ingown_suspicious.png")

#================================================= CG: Hammett =================================================#
#================================================== CG: Ethan ==================================================#
image Ethan_D1_CG1a_shock = Image("CGs/Ethan_D1_CG1a_shock.png")
image Ethan_D1_CG1b_shy = Image("CGs/Ethan_D1_CG1b_shy.png")

#============================================ CG: pastmemory_hammett ============================================#
image pastmemory_hammett1 = Image("pastmemory_hammett1.png")

#============================================= CG: pastmemory_ethan =============================================#

#================================================== Background ==================================================#
image bg Hospital_room_night = Image("bg_byouin000shade_night000-studio.jpg")
image bg Hospital_room_afternoon = Image("bg_byouin000shade-studio.jpg")
image bg Hospital_room_morning = Image("bg_byouin000-studio.jpg")
image bg Hospital_counter = Image("bg_nurce_st-studio.jpg")
image bg Hospital_infirmary = Image("bg_sinryousitu-studio.jpg")

#Credit--: Gutari Nyanko from itch.io

image bg black_screen = Image("bg_black_screen.png")
image warningscreen = Image("warningscreen.png")

################################################## Define images #################################################

#================================================= CHAR: Hammett ================================================#
#_______________________________________________  OUTFIT: Doctor  _______________________________________________#
#----------------------------------------------- POSE: pose_normal ----------------------------------------------#
#++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: smiling +++++++++++++++++++++++++++++++++++++++++++++#
image Hammett_pose_normal:
    "Hammett_pose_normal.png"
    zoom 0.45

image Hammett_pose_normal_smile_talking:
    "Hammett_pose_normal_smile_talking.png"
    zoom 0.45

image Hammett_pose_normal_slight_smile_talking:
    "Hammett_pose_normal_slight_smile_talking.png"
    zoom 0.45

image Hammett_pose_normal_slight_smile:
    "Hammett_pose_normal_slight_smile.png"
    zoom 0.45

image Hammett_pose_normal_big_smile_talking:
    "Hammett_pose_normal_big_smile_talking.png"
    zoom 0.45

image Hammett_pose_normal_big_smile:
    "Hammett_pose_normal_big_smile.png"
    zoom 0.45

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: akward +++++++++++++++++++++++++++++++++++++++++++++#
image Hammett_pose_normal_akward:
    "Hammett_pose_normal_akward.png"
    zoom 0.45

image Hammett_pose_normal_akward_panic:
    "Hammett_pose_normal_akward_panic.png"
    zoom 0.45

image Hammett_pose_normal_akward_talking:
    "Hammett_pose_normal_akward_talking.png"
    zoom 0.45

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: funny ++++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_pose_normal_funny_face1:
    "Hammett_pose_normal_funny_face1.png"
    zoom 0.45

image Hammett_pose_normal_funny_face2:
    "Hammett_pose_normal_funny_face2.png"
    zoom 0.45

#================================================ CHAR: Ethan ===================================================#
#______________________________________________  OUTFIT: casual  ________________________________________________#
#---------------------------------------------- POSE: normal_pose -----------------------------------------------#
image Ethan_normal_pose:
    "Ethan_normal_pose.png"
    zoom 0.45

#___________________________________________  OUTFIT: hospital gown _____________________________________________#
image Ethan_normal_pose_ingown:
    "Ethan_normal_pose_ingown.png"
    zoom 0.45

image Ethan_normal_pose_ingown_talking:
    "Ethan_normal_pose_ingown_talking.png"
    zoom 0.45

#---------------------------------------------- POSE: questioning -----------------------------------------------#
image Ethan_questioning_ingown_talking:
    "Ethan_questioning_ingown_talking.png"
    zoom 0.45

image Ethan_questioning_ingown_suspicious:
    "Ethan_questioning_ingown_suspicious.png"
    zoom 0.45

#================================================== CG: Ethan ==================================================#
image Ethan_D1_CG1a_shock:
    "CGs/Ethan_D1_CG1a_shock.png"

image Ethan_D1_CG1b_shy:
    "CGs/Ethan_D1_CG1b_shy.png"


#============================================ CG: pastmemory_hammett ============================================#
image pastmemory_hammett1:
    "pastmemory_hammett1.png"

#============================================= CG: pastmemory_ethan =============================================#

#================================================== Background ==================================================#
image bg Hospital_room_night:
    "bg_byouin000shade_night000-studio.jpg"
    zoom 1.5

image bg Hospital_room_afternoon:
    "bg_byouin000shade-studio.jpg"
    zoom 1.5

image bg Hospital_room_morning:
    "bg_byouin000-studio.jpg"
    zoom 1.5

image bg Hospital_counter:
    "bg_nurce_st-studio.jpg"
    zoom 3.0

image bg Hospital_infirmary:
    "bg_sinryousitu-studio.jpg"
    zoom 1.5

image bg black_screen:
    "bg_black_screen.png"

image warningscreen:
    "warningscreen.png"
#================================================== CGs ==================================================#


image CG_a_red = "CGs/a_red.png"
image CG_a_orange = "CGs/a_orange.png"
image CG_a_yellow = "CGs/a_yellow.png"
image CG_a_green = "CGs/a_green.png"
image CG_a_blue = "CGs/a_blue.png"
image CG_a_indigo = "CGs/a_indigo.png"


image CG_b_red = "CGs/b_red.png"
image CG_b_orange = "CGs/b_orange.png"
image CG_b_yellow = "CGs/b_yellow.png"
image CG_b_green = "CGs/b_green.png"
image CG_b_blue = "CGs/b_blue.png"
image CG_b_indigo = "CGs/b_indigo.png"

################################################## Define transition #################################################

transform offscreenbottomleft:
    xpos 0.0 xanchor 1.0 ypos 2.0 yanchor 1.0

define leftside = MoveTransition(
                    delay=0.3,
                    enter =offscreenbottomleft,
                    leave =offscreenbottomleft,
                    old =False,
                    layers =['master'],
                    time_warp =ease,
                    enter_time_warp =None,
                    leave_time_warp =None)

transform slide_left:
    xalign 0.0  # Move character to the left side
    yalign 1.0
    linear 0.5 xalign 0.0  # Move smoothly over 0.5 seconds

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform bounce_once:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform moving_closer:
    xpos 0.3888
    ypos 0.0933
    pause 0.15
    ease 1.0 zoom 4.0 xpos 0.06 ypos 0.0


############################################## The game starts here. #############################################
#==================================================== Day 1 =====================================================#

label start:

    $ quick_menu = False
    window hide
    show warningscreen with dissolve
    $ renpy.pause(2.0)
    scene black
    hide warningscreen with dissolve
    #start of the story
    $ quick_menu = True
    play music "audio/spotidownloader.com - rainy day - Stream Cafe.mp3" volume 0.5
    scene black

    "One day at night, you are driving your car at a highway, heading to your born city which brings you the joyful childhood memory." 
    "The highway you are driving on was pitch black as there's no street lamp beside the highway."
    "You feel loneliness as it was only black around except the road showed by the ligh of your car"
    Y "Not supprise that the highway didn't get any upgrade."
    "Just then, you notice a shine of light, it was the light from your born city, the Morphas City." 
    Y "(Not gonna lie, the city has getting better now.)"
    Y "I hope just a few more minutes then I'll arrive to my apartment and get a nice nap."
    "Your housemate, Calvia has been waiting for your arrival in her apartment." 
    "You two have known each other since middle school. She had advice you to come to this city with her and you have been looking foward to be together with her again."
    "So, you took this sweet oppurtunity, and also a chance to say goodbye to your upsetting past job experience." 
    "You feel excitement in your brain as you are getting close to the city."
    Y "Speeding a little more might not hurt. It's not like someone's going to standing in the middle of the highway at night."
    "After thinking of that, you speed up your car."
    play sound "audio/notification-sound.mp3" volume 0.8
    "Your phone had recieve a new message."
    "You glance at your phone, which was placed on the co-pilot's seat."
    "It's an message from your housemate."
    "Have you arrive yet?"
    play sound "audio/notification-sound.mp3" volume 0.8
    "I'm going to doze off. (sleeping emoji)"
    Y "(She's funny.)"
    stop music fadeout 2.0
    "When you turn back to your driving, you realise there's a green hair guy standing in the middle of the highway, it's too late to stop the car." 
    "The green guy also notice you, but it is also too late for him to avoid you." 
    "You quickly turn the steering wheel to the right." 
    play sound "audio/237375__squareal__car-crash.mp3" 
    "Then, your car had crash into the woods beside the road." 
    "The recoil of the crash made you hit your head towards the steering wheel before recoiling back to the seat."
    Y "(That's a close call.)"
    "The recoil is too hard, so you fall into a coma."
    show text "You have a car crash..." at truecenter
    with dissolve
    pause 2
    hide text "You have a car crash..."
    hide black
    play music "audio/569865__theojt__peaceful-ambiance-theme-2.mp3" volume 0.5
    show pastmemory_hammett1 with dissolve
    Y "Can you read the story book for me? Pleassseeee."
    "A little boy" "O..Okay."
    "A little boy" "Once upon a time, there's a poor girl who is being made things difficult by her cruel stepmother and her stepsister."
    "A little boy" "One day, an old lady come to the house and ask for a glass of water, the kind girl offers a glass of water and a freshly made slice of pie for the old lady."
    "A little boy" "The old lady was very grateful for the offer and thank the kind girl."
    "A little boy" "But the stepmother and the stepsister does not like the girl, they assign the girl with impossible task."
    "A little boy" "The stepmother had assign the girl to clean 5 kilograms of dirty feathers, drain water of a lake and build a castle, or else she will be locked in the storage room and straved."
    "A little boy" "The girl felt hopeless as it was impossible for her to accomplish such diffcult task."
    "A little boy" "The old lady from before had known the unfair task given to the kind girl, to repay the kindness of the girl."
    "A little boy" "The old lady help the girl achieve the task."
    hide pastmemory_hammett1 with dissolve
    stop music fadeout 1.0
    
    scene bg Hospital_room_night
    "You woke up in a hospital room."
    Y "Arghhh, my head hurts...."
    Y "And what is that weird dream, kinda familiar..."
    Y "Oh shoot, I think I crash into someone with a green hair!"
    Y "Is he the one who called the ambulance?"
    menu:
        "Find the green hair guy":
            hide Hospital_room_night
            scene bg Hospital_counter
            play music "audio/spotidownloader.com - study time - Stream Cafe.mp3" volume 0.5
            play sound "audio/Sound Effects - Footsteps.mp3" volume 0.8
            "You come to the counter, to know who's the one save you and the green hair guy's condition."
            "At the counter, there's a lady with nurse uniform, greeting you with a smile."
            Y "Hi miss."
            "Nurse" "Hi there sweetie, how should I address you?"
            jump pronounce
        "Stay in the room":
            play music "audio/spotidownloader.com - study time - Stream Cafe.mp3" volume 0.5
            jump hammett_day1_1

label pronounce:

    $ povpronouce = renpy.input("What is your pronounce? (He/She/They)", length = 10)

    $ povgendertitle = ""
    
    if povpronouce in ["He" , "Him" , "he" , "him"]:
        $ povgendertitle = "Mr. "
        
    elif povpronouce in ["She" , "Her" , "she" , "her"]:
        $ povgendertitle = "Ms. "
        
    elif povpronouce in ["They" , "Them" , "they" , "them"]:
        $ povgendertitle = "Mx. "
       
    else:
        "Invailable pronounce. Please try again."
        jump pronounce
    "Nurse" "Okay, [povgendertitle] please tell me your name, I need to do a little registration for visitor at this counter."
    jump naming

label naming:

    $ povname = renpy.input("What is your name?", length = 32)
    jump naming_double_checking

label naming_double_checking:
    y "I'm [povname]."
    "Nurse" "[povgendertitle][povname], am I right?"
    menu:
        "Yes":
            jump ethan_day1_1
        "No":
            jump pronounce


#------------------------------------------------ Route: Ethan --------------------------------------------------#

label ethan_day1_1:
    "Nurse" "So what would you like to ask, sweetie?"
    y "Do you know a guy with light green hair, recently get involve into a car crash?"
    "Nurse" "Oh, I think there he is."
    "???" "Hey that [povgendertitle] over there"
    "You heard a voice of a man, it's seems like he is calling for your attention."
    show Ethan_normal_pose_ingown at center
    with moveinleft
    "A tall green curly mullet hair man with bandages come into your view. He is that one guy you almost crash into from yesterday."
    y "Oh gosh, he got scratches all over him."
    "???" "Are you [povgendertitle][povname]?"
    menu:
        "Admit":
            hide Ethan_normal_pose_ingown
            jump ethan_day1_2
        "Deny":
            hide Ethan_normal_pose_ingown
            jump ethan_day1_deny

label ethan_day1_deny:
    show Ethan_questioning_ingown_talking

    "???" "Is that so?"
    "The green hair guy looks into your eyes, questioning you for the truthness of the answer you just gave him"
    "He seems to in disbelif of your answer and start to grew suspicious to you."
    hide Ethan_questioning_ingown_talking
    show Ethan_questioning_ingown_suspicious
    "???" "Huh... Care to explain why are you asking about my information? Who are you? And what is your purpose?"
    y "Okay okay, I'm sorry, I'm [povgendertitle][povname]."
    hide Ethan_questioning_ingown_suspicious
    show Ethan_questioning_ingown_talking
    "He seems have know you are lying to him."
    "???" "That's more likely."
    hide Ethan_questioning_ingown_talking
    show Ethan_normal_pose_ingown at slide_left
    jump Hammett_Ethan_day1_1

label ethan_day1_2:

    stop music fadeout 2.0
    "The guilt feeling in your heart burst out as you feel sorry for hurting him because of your careless behaviour while driving."
    show Ethan_D1_CG1a_shock
    y "I'M SO SO SORRY SIR!!! I'LL TAKE FULL RESPONSIBLE OF YOU!!!!!!!!!"
    hide Ethan_D1_CG1a_shock
    play music "audio/spotidownloader.com - matcha mochi - Stream Cafe.mp3" volume 0.5
    show Ethan_D1_CG1b_shy
    $ persistent.ethan_cg_1_unlocked = True  # Unlock the CG
    "To your suprise, the green hair guy seem shock for a while and the redness come to his cheek."
    "???" "sh.. shush...you will get everyone here misunderstood the situation..."
    Y "Misunderstood...?"
    "Did he get the wrong idea? Or there's some story that I didn't know yet?"
    
    hide Ethan_D1_CG1b_shy
    stop music fadeout 1.0
    show Ethan_normal_pose_ingown at slide_left
    jump Hammett_Ethan_day1_1


#------------------------------------------------ Route: Hammett -------------------------------------------------#

label hammett_day1_1:
    
    play sound "audio/440499__christutorials__light-switch-turn-off-sound.mp3" volume 0.8
    scene bg Hospital_room_afternoon
    "A dark purple hair man with losen pony tail show up in the room. "
    show Hammett_pose_normal at center
    with moveinright
    "The dark purple hair man was wearing a medical gown, he must be your doctor."
    "???" "Good day, how should i pronounce you?"
    

label hammett_day1_2:
    
    $ povpronouce = renpy.input("What is your pronounce? (He/She/They)", length = 10)

    $ povgendertitle = ""
    
    if povpronouce in ["He" , "Him" , "he" , "him"]:
        $ povgendertitle = "Mr. "
        
    elif povpronouce in ["She" , "Her" , "she" , "her"]:
        $ povgendertitle = "Ms. "
        
    elif povpronouce in ["They" , "Them" , "they" , "them"]:
        $ povgendertitle = "Mx. "
       
    else:
        "Invailable pronounce. Please try again."
        jump hammett_day1_2
    jump hammett_day1_3

label hammett_day1_3:
    hide Hammett_pose_normal
    show Hammett_pose_normal_slight_smile at center

    "???" "So [povgendertitle], can you still remember your name?"

    $ povname = renpy.input("What is your name?", length = 32)

    jump hammett_day1_4

label hammett_day1_4:
    y "I'm [povname]."
    hide Hammett_pose_normal_slight_smile
    show Hammett_pose_normal_big_smile at center

    "???" "[povgendertitle][povname], am I right?"
    menu:
        "Yes":
            jump hammett_day1_5
        "No":
            jump hammett_day1_2
    
label hammett_day1_5:
    hide Hammett_pose_normal_big_smile
    show Hammett_pose_normal at center

    "???" "Okay now back to the topic..."
    y "Wait."
    
    "He seem very confused."
    hide Hammett_pose_normal
    show Hammett_pose_normal_big_smile_talking at center

    "???" "Yes? Is there any confusion?"
    y "Can I know your name?"
    hide Hammett_pose_normal_big_smile_talking
    stop music fadeout 2.0
    show Hammett_pose_normal_akward at center, bounce_once
    "After you had ask this question, the man frozed infront of you."
    "???" "..."
    y "..."
    hide Hammett_pose_normal_akward
    show Hammett_pose_normal_akward_talking at center
    "He seem very akward."
    "???" "Did I ... never introduce myself?"
    hide Hammett_pose_normal_akward_talking
    show Hammett_pose_normal_akward_panic at center

    show Hammett_pose_normal_akward_panic at bounce, center
    play music "audio/spotidownloader.com - honey's waltz - Stream Cafe.mp3" volume 0.5
    "Then, the purple hair man was panic."
    h "I...I'm very sorry for my late self introduction."
    h "The name's Hammett, call me Dr Hammett or Hammett. Feel free to call me through the bell when you need me."
    h "And... a small request for you..."
    y "Yes?"
    h "Please forgot that please."
    "The man named Hammett seems to akwardly please you to forget that embarrassed scene he just made."
    menu:
        "Never":
            jump teasing_hammett_1

        "Ok":
            jump teasing_hammett_1_false

define teasing_hammett = False
label teasing_hammett_1:
    hide Hammett_pose_normal_akward_panic
    show Hammett_pose_normal_funny_face1 at center, bounce_once
    h "Aww come on!"
    show Hammett_pose_normal_funny_face1 at center, bounce_once
    h "Pleeeeeaaaaaseeeeeeeeeeee!"
    y "Not a chance."
    hide Hammett_pose_normal_funny_face1
    show Hammett_pose_normal_funny_face2 at center, bounce_once

    h "I guess that'll be haunting in my dream tonight."
    y "This guy is kinda funny."
    $ teasing_hammett = True
    hide Hammett_pose_normal_funny_face2
    jump hammett_day1_6

label teasing_hammett_1_false:
    hide Hammett_pose_normal_akward_panic
    show Hammett_pose_normal_akward_talking at center

    h "Thank you for your kindness."
    "He is relieved. Does that really mean that much to him?"
    hide Hammett_pose_normal_akward_talking
    jump hammett_day1_6

label hammett_day1_6:
    stop music fadeout 2.0
    show Hammett_pose_normal_big_smile at center

    play music "audio/spotidownloader.com - study time - Stream Cafe.mp3" volume 0.5
    h "Now back to the topic." 
    if teasing_hammett == True:
        Y "(What's with this guy?)"
    
    h "You have bump your head into the driver panel, after the pain killer have went out, you will facing some headpain. If the pain was too strong, do call me throught the bell." 
    h "And we suspect you have slight concussion on your brain, so we need to observe you for a while before releasing you."
    hide Hammett_pose_normal_big_smile
    jump condition_flag

label condition_flag:
    $ condition_flag = 0
    $ condition_self_flag = 0
    jump hammett_day1_7

label hammett_day1_7:
    show Hammett_pose_normal at center

    h "Do you have any concern or question?"
    menu:
        "Ask about when can you leave.":
            $ condition_flag += 1
            $ condition_self_flag += 1
            jump hammett_day1_condition
        "Ask about the person you crash into's condition.":
            $ condition_flag += 1
            jump hammett_day1_condition_ethan
        "I think you look familiar.":
            
            jump teasing_hammett_2
        "I have nothing to ask for now.":
            if condition_flag == 0:
                h "You are not going to aknowledge any other things?"
                menu:
                    "Yeah":
                        y "Yeah, I want some rest please."
                        h "Alright, do call me through the bell if you need me and wish you have a good rest."
                        hide Hammett_pose_normal
                        jump day1_end
                    "(Back to previous selection)":
                        hide Hammett_pose_normal
                        jump hammett_day1_7
            else:
                h "Alright, do call me through the bell if you need me and wish you have a good rest."
                hide Hammett_pose_normal
                jump day1_end




label hammett_day1_condition:
    h "You have no serious injuries, since its very late we will start the examination tommorow." 
    h "And a small reminder, your friend will arrive tommorrow, she's very worried about your condition."
    hide Hammett_pose_normal
    jump hammett_day1_7

label hammett_day1_condition_ethan:
    if condition_self_flag == 0:
        h "You are not going to acknowledge your own condition first?"
        menu:
            "Yeah":
                h "Well, if you insists, His name is Ethan Alterberth and he has wounds all over his left hand and a few scratches on other part of his body."
                y "That sounds painful."
                hide Hammett_pose_normal
                jump hammett_day1_7
            "(Back to previous selection)":
                hide Hammett_pose_normal
                jump hammett_day1_7
    else:
        h "His name is Ethan Alterberth and he has wounds all over his left hand and a few scratches on other part of his body."
        y "That sounds painful."
        hide Hammett_pose_normal
        jump hammett_day1_7

label teasing_hammett_2:
    hide Hammett_pose_normal
    show Hammett_pose_normal_big_smile at center

    h "Is this some sort of pickup line?"
    "You don't know why but he seems happy about it."
    hide Hammett_pose_normal_big_smile
    jump hammett_day1_7

#------------------------------------------------ Route: Ethan->Hammett -------------------------------------------------#
label Hammett_Ethan_day1_1:
    

    show Hammett_pose_normal at center
    with moveinright
    play music "audio/spotidownloader.com - study time - Stream Cafe.mp3" volume 0.5
    "???" "So [povgendertitle][povname], you have meet your involved party in the car accident."
    "A dark purple hair man with lossen pony tail show up infront of you. "
    "The dark purple hair man was wearing a medical gown, he must be one of the doctor in this hospital."
    y "Who are you?"
    h "I'm Doctor Hammett, the doctor that'll supervising your condition."
    h "Mr. Ethan, please go back to your room, your doctor will be meeting you there soon."
    e "Okay..."
    e "[povgendertitle][povname], please meet me at room 39, we will discuss the accident tommorrow at 3 p.m."
    play sound "audio/Sound Effects - Footsteps.mp3" volume 0.8
    hide Ethan_normal_pose_ingown with moveoutleft
    "After saying that, the tall green hair man named Ethan went back to his room."

    "Where do you want to go?"
    hide Hammett_pose_normal
    stop music 
    show Hammett_pose_normal_slight_smile at moving_closer
    
    h "{cps=*3}Oh, darling, you are not going anywhere, you and I need to have a talk.{/cps}{w=1}{nw}"
    hide Hammett_pose_normal_slight_smile
    hide Hospital_counter
    scene bg Hospital_room_afternoon
    jump condition_flag

#------------------------------------------------- Route: Free Time --------------------------------------------------#

label day1_end:
    hide Hospital_room_afternoon
    scene bg Hospital_room_night
    play sound "audio/440499__christutorials__light-switch-turn-off-sound.mp3" volume 0.8
    play music "audio/spotidownloader.com - rainy day - Stream Cafe.mp3" volume 0.5 fadein 1.0
    "After the light swtich off, the darkness fills the room."
    "But you still thinking."
    y "What a 'good' start in this city."
    "You made an undeniable complaint about your unlucky encounter."
    "After a while, you felt a strong feeling of tiredness strucks your head and you fell into slumber."
    scene bg black_screen
    hide Hospital_room_night
    stop music 
    "???" "{sc=5}I'm happy that we meet again...{/sc}"
    "???" "{sc=2}Even though you don't seem to remember me...{/sc}"
    "???" "{sc=5}But,{w=0.5} I will make sure you dont forget me {b}again{/b}.{/sc}"
    "Demo ends here."
    jump credits

label credits:
    scene black
    $ quick_menu = False
    window hide
    $ credits_speed = 15  # Speed of scrolling

    show theend:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2.0)
    hide theend

    show endcred at credits_scroll
    with dissolve
    $ renpy.pause(credits_speed)

    scene black
    with dissolve

    show thanks:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2.0)

    return

init python:
    credits = [('Backgrounds', 'Gutari Nyanko')]
    credits_s = "{size=80}Credits\n\n"
    c1 = ""
    for c in credits:
        if c1 != c[0]:
            credits_s += "\n{size=50}" + c[0] + "\n"
        credits_s += "{size=30}" + c[1] + "\n"
        c1 = c[0]
    credits_s += "\n{size=50}Engine\n{size=30}Ren'Py (8.3.6)"

init:
    image endcred = Text(credits_s, text_align=0.5, size=40, color="#FFFFFF")
    image theend = Text("{size=40}The End", text_align=0.5, color="#FFFFFF")
    image thanks = Text("{size=40}Thanks for Playing the Demo!! Stay tuned for the future update!!", text_align=0.5, color="#FFFFFF")

    transform credits_scroll:
        xalign 0.5
        ypos 1.2  # Start BELOW the screen (off-screen)
        linear 15.0 ypos -0.2  # Move UPWARDS off-screen over 15 seconds





