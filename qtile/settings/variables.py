from libqtile import widget

BAR_COLOR = "#000000"
BAR_SIZE = 25

DEFAULT_FONT = "Ubuntu Mono Nerd Font"
FONT_SIZE = 14

# Group Variables
ACTIVE_COLOR = "#f1fa8c"
ICONS_SIZE = 20
FG_COLOR_LIGHT = "#FFFFFF"
FG_COLOR_DARK = "#212121"
BG_COLOR = "#00000000"
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
