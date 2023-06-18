from libqtile import bar, widget
from libqtile.config import Screen
from .variables import *

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = ACTIVE_COLOR,
                    border_width = 1,
                    disable_drag = True,
                    fontsize = ICONS_SIZE,
                    foreground = FG_COLOR_DARK,
                    highlight_method = 'block', #text
                    inactive = INACTIVE_COLOR,
                    margin_x = 0, #0
                    margin_y = 2, #5
                    other_current_screen_border = DARK_COLOR,
                    other_screen_border = DARK_COLOR,
                    padding_x = 4,#0
                    padding_y = 2,#10
                    this_current_screen_border = LIGHT_COLOR,
                    this_screen_border = LIGHT_COLOR,
                    urgent_alert_method = 'block',
                    urgent_border = URGENT_COLOR,
                ),

                # Agregamos un separador 
                addSeparator("l"),

                widget.Prompt(),

                widget.WindowName(
                    foreground = BG_COLOR,
                    background = BG_COLOR,
                    max_chars = 1,
                    empty_group_string = 'こんにちは',
                ),

                # addSeparator(205),

                # Group MUSIC START
                    # CMUS area
                widget.Cmus(
                    background = BG_COLOR,
                    fontsize = FONT_SIZE,
                    play_color = FG_COLOR_LIGHT,
                    noplay_color = TEXT_COLOR1,
                    max_chars = 40,
                ),
                addSeparator(15),
                # Group MUSIC END

                # Group1 START
                addHalfCirle(GROUP1_COLOR, "left"),

                    # RAM area
                createNewText(" ", GROUP1_COLOR, "dark"),
                widget.Memory(
                    foreground = FG_COLOR_DARK,
                    background = GROUP1_COLOR,
                ),
                
                addHalfCirle(GROUP1_COLOR, "right"),
                addSeparator("s"),
                # Group1 END

                # Group2 START
                # addHalfCirle(GROUP2_COLOR, "left"),

                    # Wifi speed Area 
                # createNewText("龍 ", GROUP2_COLOR, "dark"),
                # widget.Net(
                #     foreground = FG_COLOR_DARK,
                #     background = GROUP2_COLOR,
                #     # format = '{down}   {up}',
                #     format = '{down} ↓↑ {up}',
                #     interface = WIFI_NETWORK_DEVICE,
                #     # use_bits = 'true', # 'true'
                # ),
                
                # addHalfCirle(GROUP2_COLOR, "right"),
                # addSeparator("s"),
                # END Group2

                # Group3 START
                addHalfCirle(GROUP3_COLOR, "left"),
                    # Date Area
                createNewText(" ", GROUP3_COLOR, "dark"),
                widget.Clock(
                    background = GROUP3_COLOR,
                    foreground = FG_COLOR_DARK,
                    format="%d/%b/%y %-I:%M %p",
                ),
                
                addHalfCirle(GROUP3_COLOR, "right"),
                addSeparator("s"),
                # END Group3

                # Group System START
                addHalfCirle(GROUP_SYSTEM_COLOR, "left"),

                    # Icons System Area
                widget.Systray(
                    background = GROUP_SYSTEM_COLOR,
                    icon_size = ICONS_SIZE,
                    # background = BG_COLOR,
                ),

                    # Backlight Area
                createNewText(" ", GROUP_SYSTEM_COLOR, FG_COLOR_SYSTEM),
                widget.Backlight(
                    background = GROUP_SYSTEM_COLOR,
                    foreground = FG_COLOR_SYSTEM,
                    backlight_name = BACKLIGHT_NAME,
                    # format = '{percent:2.0%}',
                    step = 0.5,
                ),

                addHalfCirle(GROUP_SYSTEM_COLOR, "right"),
                # Agregamos un separador 
                addSeparator("l"),
                # Group System END
            ],
            BAR_SIZE,
            background=BAR_COLOR,
            # spacer in bar side
            # Up, Right, Down, Left
            margin = [14, 40, 14, 40],
            # border_width=[1, 1, 1, 1],  # Draw top and bottom borders
            # border_color=[ACTIVE_COLOR, "000000", ACTIVE_COLOR, "000000"]  # Borders are magenta
        ),
    ),
]

# Widgets Listos para usar
# CheckUpdates Area
    # createNewText(" ", GROUP2_COLOR),
    # widget.CheckUpdates(
    #     background = GROUP2_COLOR,
    #     colour_have_updates = UPDATES_COLOR,
    #     colour_no_updates = FG_COLOR_DARK,
    #     no_update_string = '0',
    #     display_format = '{updates}',
    #     update_interval = UPDATE_INTERVAL_TIME,
    #     distro = 'Arch_checkupdates',
    # ),

    # Temperature area
        # createNewText(" ", GROUP1_COLOR),
        # widget.ThermalSensor(
        #     foreground = FG_COLOR_DARK,
        #     background = GROUP1_COLOR,
        #     threshold = 50,
        #     tag_sensor = "Core 0",
        #     fmt = 'Core: {}',
        # ),

# Group5 START
    # addHalfCirle(GROUP4_COLOR, "left"),

    # widget.CurrentLayoutIcon(
    #     background = GROUP4_COLOR,
    #     scale = 0.7,
    # ),

    # widget.CurrentLayout(
    #     background = GROUP4_COLOR,
    # ),

    # addHalfCirle(GROUP4_COLOR, "right"),
# END Group5

# widget.BatteryIcon(
    #     padding = 0,
    #     scale = 0.9,
    #     y_poss = 2,
    #     # theme_path = home + '/.config/qtile/icons/battery_icons_horiz/', #TODO
    #     update_interval = 5,
    #     background = GROUP3_COLOR,
    # ),

# widget.WindowName(
#     foreground = FG_COLOR_DARK,
#     background = GROUP1_COLOR,
#     format = '{state}{name}',
# ),

# Group MUSIC START
    # addHalfCirle(GROUP_MUSIC_COLOR, "left"),

    # widget.Cmus(
    #     background = BG_COLOR,
    #     fontsize = FONT_SIZE,
    #     play_color = TEXT_COLOR1,
    #     noplay_color = TEXT_COLOR1,
    #     max_chars = 22,
    # ),

    # addHalfCirle(GROUP_MUSIC_COLOR, "right"),
    # addSeparator("s"),
# Group MUSIC END

# Group4 START
    # addHalfCirle(GROUP4_COLOR, "left"),
        # Volume Area
    # createNewText(" ", GROUP4_COLOR),
    # widget.PulseVolume(
    #     foreground = FG_COLOR_DARK,
    #     background = GROUP4_COLOR,
    #     limit_max_volume = True,
    #     fontsize = FONT_SIZE,
    # ),

    #     # Backlight Area
    # createNewText("  ", GROUP4_COLOR),
    # widget.Backlight(
    #     background = GROUP4_COLOR,
    #     foreground = FG_COLOR_DARK,
    #     backlight_name = BACKLIGHT_NAME,
    #     # format = '{percent:2.0%}',
    #     step = 0.5,
    # ),

    # WIFI Area
    # widget.Wlan(
    #     background = GROUP4_COLOR,
    #     foreground = FG_COLOR_DARK,
    #     disconnected_message = '睊 ',
    #     # format='  {essid}',
    #     format='  ',
    #     # max_chars = 10,
    #     interface = WIFI_NETWORK_DEVICE,
    # ),
    
    # addHalfCirle(GROUP4_COLOR, "right"),
# END Group4
