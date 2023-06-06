# Qtile keybindings

from libqtile.config import Key, Click, Drag
from libqtile.command import lazy
import os

home = os.path.expanduser('~')
mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "down", lazy.layout.down()),
    ([mod], "up", lazy.layout.up()),
    ([mod], "left", lazy.layout.left()),
    ([mod], "right", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "control"], "left", lazy.layout.grow_left()),
    ([mod, "control"], "right", lazy.layout.grow_right()),
    ([mod, "control"], "down", lazy.layout.grow_down()),
    ([mod, "control"], "up", lazy.layout.grow_up()),
    ([mod], "n", lazy.layout.normalize()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "left", lazy.layout.shuffle_left()),
    ([mod, "shift"], "right", lazy.layout.shuffle_right()),
    ([mod, "shift"], "down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "up", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    #([mod], "Tab", lazy.next_layout()),
    #([mod, "shift"], "Tab", lazy.prev_layout()),
    
    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # Toggle Bar
    ([mod], "b", lazy.hide_show_bar(position='all')),

    # Toggle between split and unsplit sides of stack
    # ([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Switch focus of monitors
    # ([mod], "period", lazy.next_screen()),
    # ([mod], "comma", lazy.prev_screen()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "space", lazy.spawn("rofi -show drun")),
    #([mod], "space", lazy.spawn("~/.config/rofi/launchers/type-7/launcher.sh")),

    # Window Nav
    #([mod], "Tab", lazy.spawn("rofi -show window")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Web Browsers
    ([mod], "f", lazy.spawn("firefox-developer-edition")),
    ([mod], "c", lazy.spawn("google-chrome-stable")),

    # ScreenShot
    ([], "Print", lazy.spawn('gnome-screenshot -i')),
    ([mod], "Print", lazy.spawn("scrot -e 'mv $f ~/Pictures/ScreenShots/%b%d-%H%M%S.png'")),
    ([mod, "shift"], "Print", lazy.spawn('xfce4-screenshooter')),
    # ([mod], "Print", lazy.spawn("scrot -s scrot -e 'mv $f ~/Pictures/ScreenShots/%b%d-%H%M%S.png'")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Color Picker
    ([mod], "p", lazy.spawn('kcolorchooser')),

    # ------------ Hardware Configs ------------

    # Volume
    # ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    # ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    # ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    ([], "XF86AudioLowerVolume", lazy.spawn(f"{home}/.config/qtile/scripts/Volume.sh --dec")),
    ([], "XF86AudioRaiseVolume", lazy.spawn(f"{home}/.config/qtile/scripts/Volume.sh --inc")),
    ([], "XF86AudioMute", lazy.spawn(f"{home}/.config/qtile/scripts/Volume.sh --toggle")),

    # Pause/Play/Nex/Previous Track
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Brightness
    # ([], "F7", lazy.spawn("xbacklight -inc 1")),
    # ([], "F6", lazy.spawn("xbacklight -dec 1")),
    ([], "F7", lazy.spawn(f"{home}/.config/qtile/scripts/Brightness.sh up")),
    ([], "F6", lazy.spawn(f"{home}/.config/qtile/scripts/Brightness.sh down")),
    ([], "XF86MonBrightnessUp", lazy.spawn(f"{home}/.config/qtile/scripts/Brightness.sh up")),
    ([], "XF86MonBrightnessDown", lazy.spawn(f"{home}/.config/qtile/scripts/Brightness.sh down")),
]]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
