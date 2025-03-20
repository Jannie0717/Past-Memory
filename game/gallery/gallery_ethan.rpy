screen gallery_ethan:
    tag menu
    add "CustomUI/bg_gallery_ethan.png"

    fixed:
        use gallery_navigation
        
         # Check if the CG has been unlocked
        if persistent.ethan_cg_1_unlocked:
            imagebutton:
                idle "CGs/ethan_cg_nav_button1.png"
                hover "CGs/ethan_cg_nav_button1.png"
                action ShowMenu("ethan_cg_display")
                xpos 298 ypos 181
        
        else:
            add "CGs/ethan_locked1.png" xpos 298 ypos 181  # Show locked image
        
# Screen to display CGs in sequence
screen ethan_cg_display():
    tag menu

    default cg_index = 0  # Variable to track which CG is being displayed
    default cg_list = ["CGs/Ethan_D1_CG1a_shock.png", "CGs/Ethan_D1_CG1b_shy.png"]

    add cg_list[cg_index]  # Display the current CG

    textbutton "Return":
        xpos 0.9 ypos 0.9
        action Return()

    # Clicking anywhere progresses the CGs
    button:
        action If(cg_index == 0, SetScreenVariable("cg_index", 1), ShowMenu("gallery_ethan"))
        style "empty"        
        
        #grid 3 2:
        #    spacing 25
#
        #    add gallery.make_button("b_red", unlocked = im.Scale("CGs/b_red.png",234,132), locked = "locked.jpg")
        #    add gallery.make_button("b_orange", unlocked = im.Scale("CGs/b_orange.png",234,132), locked = "locked.jpg")
        #    add gallery.make_button("b_yellow", unlocked = im.Scale("CGs/b_yellow.png",234,132), locked = "locked.jpg")
        #    add gallery.make_button("b_green", unlocked = im.Scale("CGs/b_green.png",234,132), locked = "locked.jpg")
        #    add gallery.make_button("b_blue", unlocked = im.Scale("CGs/b_blue.png",234,132), locked = "locked.jpg")
        #    add gallery.make_button("b_indigo", unlocked = im.Scale("CGs/b_indigo.png",234,132), locked = "locked.jpg")
           