init python early hide:
    import renpy
    if 'tl_font_dic' not in globals():
        global tl_font_dic
        tl_font_dic = dict()
        global old_load_face
        old_load_face = renpy.text.font.load_face

        def my_load_face(fn, *args):
            renpy.text.font.free_memory()
            for key, value in tl_font_dic.items():
                if renpy.game.preferences.language == key:
                    fn = value[0]
                    renpy.config.rtl = value[1]
            return old_load_face(fn, *args)
        renpy.text.font.load_face = my_load_face
    global tl_font_dic
    tl_font_dic["Chinese"] = "fonts/YRDZST Semibold.ttf", False
    old_reload_all = renpy.reload_all
    def my_reload_all():
        renpy.text.font.free_memory()
        renpy.text.font.load_face = old_load_face
        ret = old_reload_all()
        renpy.reload_all = old_reload_all
        return ret
    renpy.reload_all = my_reload_all
