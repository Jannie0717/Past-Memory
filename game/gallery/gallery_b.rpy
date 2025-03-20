screen gallery_b:
    tag menu
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5

        use gallery_navigation

        grid 3 2:
            spacing 25

            add gallery.make_button("b_red", unlocked = im.Scale("CGs/b_red.png",234,132), locked = "locked.jpg")
            add gallery.make_button("b_orange", unlocked = im.Scale("CGs/b_orange.png",234,132), locked = "locked.jpg")
            add gallery.make_button("b_yellow", unlocked = im.Scale("CGs/b_yellow.png",234,132), locked = "locked.jpg")
            add gallery.make_button("b_green", unlocked = im.Scale("CGs/b_green.png",234,132), locked = "locked.jpg")
            add gallery.make_button("b_blue", unlocked = im.Scale("CGs/b_blue.png",234,132), locked = "locked.jpg")
            add gallery.make_button("b_indigo", unlocked = im.Scale("CGs/b_indigo.png",234,132), locked = "locked.jpg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
