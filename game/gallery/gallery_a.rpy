screen gallery_a:
    tag menu
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5

        use gallery_navigation

        grid 3 2:
            spacing 25

            add gallery.make_button("a_red", unlocked = im.Scale("CGs/a_red.png",234,132), locked = "locked.jpg")
            add gallery.make_button("a_orange", unlocked = im.Scale("CGs/a_orange.png",234,132), locked = "locked.jpg")
            add gallery.make_button("a_yellow", unlocked = im.Scale("CGs/a_yellow.png",234,132), locked = "locked.jpg")
            add gallery.make_button("a_green", unlocked = im.Scale("CGs/a_green.png",234,132), locked = "locked.jpg")
            add gallery.make_button("a_blue", unlocked = im.Scale("CGs/a_blue.png",234,132), locked = "locked.jpg")
            add gallery.make_button("a_indigo", unlocked = im.Scale("CGs/a_indigo.png",234,132), locked = "locked.jpg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
