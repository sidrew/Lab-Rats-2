screen serum_trade_ui(inventory_1,inventory_2, name_1="Player", name_2="Business", trade_requirement = None, hide_instead = False, inventory_2_max = -1): #Lets you trade serums back and forth between two different inventories. Inventory 1 is assumed to be the players.
    modal True
    add "Science_Menu_Background.png"
    viewport:
        xsize 1010
        ysize 800
        xalign 0.5
        yalign 0.1
        scrollbars "vertical"
        mousewheel True
        frame:
            background "#888888"
            xalign 0.5
            xanchor 0.5
            yalign 0.1
            vbox:
                yalign 0.0
                spacing 20
                text "Trade Serums Between Inventories." style "menu_text_style" size 25 xalign 0.5 xanchor 0.5
                $ the_set = set(inventory_1.get_serum_type_list()) | set(inventory_2.get_serum_type_list())
                for serum in sorted(the_set, key=attrgetter("name")): #Gets a unique entry for each serum design that shows up in either list. Doesn't duplicate if it's in both.
                    # has a few things. 1) name of serum design. 2) count of first inventory, 3) arrows for transfering, 4) count of second inventory.
                    frame:
                        background "#777777"
                        xalign 0.5
                        xanchor 0.5
                        yalign 0.0
                        yanchor 0.0
                        vbox:
                            xalign 0.5
                            xanchor 0.5
                            xsize 600
                            $ trade_sensitive = True
                            if trade_requirement:
                                $ trade_sensitive = trade_requirement(serum)

                            $ move_all_amount = inventory_1.get_serum_count(serum)
                            if inventory_2_max >= 0 and move_all_amount + inventory_2.get_any_serum_count() > inventory_2_max:
                                $ move_all_amount =inventory_2_max - inventory_2.get_any_serum_count()
                            hbox:
                                textbutton serum.name + ": " style "textbutton_style" text_style "menu_text_style" action NullAction() hovered Show("serum_tooltip",None,serum, given_align = (0.02,0.02)) unhovered Hide("serum_tooltip") #displays the name of this particular serum
                                null width 10
                                text name_1 + "\nhas: " + str(inventory_1.get_serum_count(serum)) style "menu_text_style"#The players current inventory count. 0 if there is nothing in their inventory
                                textbutton "|<":
                                    action [Function(inventory_1.change_serum,serum,inventory_2.get_serum_count(serum)),Function(inventory_2.change_serum,serum,-inventory_2.get_serum_count(serum))]
                                    sensitive (inventory_2.get_serum_count(serum) > 0) and trade_sensitive style "textbutton_style" text_style "textbutton_text_style"
                                textbutton "<<":
                                    action [Function(inventory_1.change_serum,serum,5),Function(inventory_2.change_serum,serum,-5)]
                                    sensitive (inventory_2.get_serum_count(serum) > 4) and trade_sensitive style "textbutton_style" text_style "textbutton_text_style"
                                textbutton "<":
                                    action [Function(inventory_1.change_serum,serum,1),Function(inventory_2.change_serum,serum,-1)]
                                    sensitive (inventory_2.get_serum_count(serum) > 0) and trade_sensitive style "textbutton_style" text_style "textbutton_text_style"
                                #When pressed, moves 1 serum from the business inventory to the player. Not active if the business has nothing in it.
                                null width 10
                                textbutton ">":
                                    action [Function(inventory_2.change_serum,serum,1),Function(inventory_1.change_serum,serum,-1)]
                                    sensitive (inventory_1.get_serum_count(serum) > 0) and inventory_2.get_any_serum_count()+1 <= inventory_2_max and trade_sensitive style "textbutton_style" text_style "textbutton_text_style"
                                textbutton ">>":
                                    action [Function(inventory_2.change_serum,serum,5),Function(inventory_1.change_serum,serum,-5)]
                                    sensitive (inventory_1.get_serum_count(serum) > 4) and inventory_2.get_any_serum_count()+5 <= inventory_2_max and trade_sensitive style "textbutton_style" text_style "textbutton_text_style"
                                textbutton ">|":
                                    action [Function(inventory_2.change_serum,serum, move_all_amount),Function(inventory_1.change_serum,serum,-move_all_amount)]
                                    sensitive (move_all_amount > 0) and trade_sensitive style "textbutton_style" text_style "textbutton_text_style"
                                text name_2 + "\nhas: " + str(inventory_2.get_serum_count(serum)) style "menu_text_style"


    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            if hide_instead:
                action Hide("serum_trade_ui")
            else:
                action Return()
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
