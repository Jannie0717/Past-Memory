screen gallery_navigation():

    fixed:
        imagebutton auto "CustomUI/gallery_hammett_%s.png" xpos 49 ypos 175 focus_mask True action ShowMenu("gallery_hammett") hovered [Play("sound", "audio/click.mp3")]
        
        imagebutton auto "CustomUI/gallery_ethan_%s.png" xpos 49 ypos 355 focus_mask True action ShowMenu("gallery_ethan") hovered [Play("sound", "audio/click.mp3")]

        textbutton "Return":
            xpos 0.5 ypos 0.9
            anchor (0.5, 0.5)
            action Return()
