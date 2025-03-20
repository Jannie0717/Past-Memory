screen gallery_c:
    tag menu
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation

        grid 3 2:
            spacing 25

            add gallery.make_button("c_red", unlocked = im.Scale("CGs/c_red.png",234,132), locked = "locked.jpg")
            add gallery.make_button("c_orange", unlocked = im.Scale("CGs/c_orange.png",234,132), locked = "locked.jpg")
            add gallery.make_button("c_yellow", unlocked = im.Scale("CGs/c_yellow.png",234,132), locked = "locked.jpg")
            add gallery.make_button("c_green", unlocked = im.Scale("CGs/c_green.png",234,132), locked = "locked.jpg")
            add gallery.make_button("c_blue", unlocked = im.Scale("CGs/c_blue.png",234,132), locked = "locked.jpg")
            add gallery.make_button("c_indigo", unlocked = im.Scale("CGs/c_indigo.png",234,132), locked = "locked.jpg")
           