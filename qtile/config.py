# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import subprocess
from libqtile import hook
from typing import List # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

# Own Variables
home = os.path.expanduser('~')

BAR_COLOR = "#282a36"
BAR_SIZE = 25

DEFAULT_FONT = "Ubuntu Mono Nerd Font"
# FONT_SIZE = 14
FONT_SIZE = 14

# Group Variables
ACTIVE_COLOR = "#f1fa8c"
ICONS_SIZE = 20
FG_COLOR_LIGHT = "#FFFFFF"
FG_COLOR_DARK = "#212121"
BG_COLOR = "#282a36"
INACTIVE_COLOR = "#6272a4"
DARK_COLOR = "#44475a"
LIGHT_COLOR = "#bd93f9"
URGENT_COLOR = "#ff5555"
TEXT_COLOR1 = "#bd93f9"

# GROUP SYSTEM
GROUP_SYSTEM_COLOR = "#150050"
FG_COLOR_SYSTEM = "#459eef"

# Grupo Music
GROUP_MUSIC_COLOR = "#1E3163"

# Grupo1 Variables
GROUP1_COLOR = "#FDFDBD"

# Grupo2 Variables
GROUP2_COLOR = "#C8FFD4"
UPDATES_COLOR = "#bc0000"
UPDATE_INTERVAL_TIME = 600
WIRED_NETWORK_DEVICE = 'enp2s0f1'
WIFI_NETWORK_DEVICE = 'wlp3s0'

# Grupo3 Variables
GROUP3_COLOR = "#B8E8FC"

# Grupo4 Variables
GROUP4_COLOR = "#B1AFFF"
BACKLIGHT_NAME = 'intel_backlight' # ls /sys/class/backlight/

# Functions
# Agrega un separador
def addSeparator(type):
    if type == "s":
        quantity = 2

    elif type == "m":
        quantity = 6

    elif type == "l":
        quantity = 10
    
    else:
        quantity = type
    
    return widget.Sep(
        linewidth = 0,
        padding = quantity,
        foreground = FG_COLOR_DARK,
        background = BG_COLOR
    )

# Agrega círculos medios
def addHalfCirle(color, type):
    if type == "left":
        icon = ""
    else:
        icon = ""

    return widget.TextBox(
        text = icon,
        fontsize = BAR_SIZE + 5,
        foreground = color,
        background = BG_COLOR,
        padding = -1,
    )

# Crea un nuevo texto o ícono
def createNewText(icon, groupColor, fb_color):
    if fb_color == "light":
        fb_color = FG_COLOR_LIGHT
    elif fb_color == "dark":
        fb_color = FG_COLOR_DARK
    else:
        fb_color = fb_color

    return widget.TextBox(
        text = icon,
        fontsize = ICONS_SIZE,
        foreground = fb_color,
        background = groupColor,
    )


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),

    # Abre la terminal
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    #Teclas para lanzar aplicaciones
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch Rofi menu"),
    # Key([mod], "space", lazy.spawn("ulauncher-toggle"), desc="Launch ulauncher menu"),

    #Teclas para lanzar navegadores web 
    Key([mod], "f", lazy.spawn("firefox-developer-edition"), desc="Launch firefox"),
    Key([mod], "c", lazy.spawn("google-chrome-stable"), desc="Launch chromium"),

    #Teclas para lanzar manejador de archivos Thunar 
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch Thunar"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"), desc="Decrease the volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"), desc="increase the volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute the volume"),

    # Pause/Play/Nex/Previous Track
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Screen brightness control
    Key([], "F7", lazy.spawn("xbacklight -inc 1")),
    Key([], "F6", lazy.spawn("xbacklight -dec 1")),

    # Screen brightness control with native key bindings
    # Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increases the screen brightness"),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease screen brightness"),
    
    # ScreenShot
    Key([], "Print", lazy.spawn('gnome-screenshot -i')),
    Key([mod], "Print", lazy.spawn("scrot -e 'mv $f ~/Pictures/%b%d-%H%M%S.png'")),
    Key([mod, "shift"], "Print", lazy.spawn('xfce4-screenshooter')),

    # Key([mod], "Print", lazy.spawn("scrot -s scrot -e 'mv $f ~/Pictures/%b%d-%H%M%S.png'")),

    # Toggle bars
    Key([mod], "b", lazy.hide_show_bar(position='all'), desc = "Toggle bars"),

    # Color Picker
    Key([mod], "p", lazy.spawn('kcolorchooser')),
]


# Group using icons
# Space Groups
# 1. Arch | 2.Firefox | 3. Code | 4.Chrome | 5. File | 6. Teams | 7. Ghost | 8. Music     
groups = [Group(i) for i in [
    " ", " ", " ", " ", " ", " ", " ", "阮 "
]]

# Group using Japanese characters
# groups = [Group(i) for i in [
#     "一", "二", "三", "四", "五", "六", "七", "八",
# ]]

for i, group in enumerate(groups):
    desktopNumber = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                desktopNumber,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                desktopNumber,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=DEFAULT_FONT,
    fontsize=FONT_SIZE,
    padding=1,
)
extension_defaults = widget_defaults.copy()

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
                addHalfCirle(GROUP2_COLOR, "left"),

                    # Wifi speed Area 
                createNewText("龍 ", GROUP2_COLOR, "dark"),
                widget.Net(
                    foreground = FG_COLOR_DARK,
                    background = GROUP2_COLOR,
                    # format = '{down}   {up}',
                    format = '{down} ↓↑ {up}',
                    interface = WIFI_NETWORK_DEVICE,
                    # use_bits = 'true', # 'true'
                ),
                
                addHalfCirle(GROUP2_COLOR, "right"),
                addSeparator("s"),
                # END Group2

                # Group3 START
                addHalfCirle(GROUP3_COLOR, "left"),
                    # Date Area
                createNewText(" ", GROUP3_COLOR, "dark"),
                widget.Clock(
                    background = GROUP3_COLOR,
                    foreground = FG_COLOR_DARK,
                    # format="%a %d/%b/%Y %H:%M",
                    format="%d/%b/%Y %H:%M",
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
            # Up, Right, Down, Left
            margin = [5, 10, 5, 10],
            # border_width=[1, 1, 1, 1],  # Draw top and bottom borders
            # border_color=[ACTIVE_COLOR, "000000", ACTIVE_COLOR, "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Autostart own
list_commands = [
    "picom --config ~/.config/picom/picom.conf &",
]

# Here I execute each command
for command in list_commands:
    os.system(command)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


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
