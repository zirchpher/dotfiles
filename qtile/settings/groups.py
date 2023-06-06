# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys

# Group using icons
# 1. Arch | 2.Firefox | 3. Code | 4.Chrome | 5. File | 6. Teams | 7. Ghost | 8. Music     
groups = [Group(i) for i in [
    "一", "二", "三", "四", "五", "六"
    # " ", " ", " ", " ", " ", " ", " ", "阮 "
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
