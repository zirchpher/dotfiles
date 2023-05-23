# Arch Linux Post Installation

### Pacman Config

```BASH
sudo nvim /etc/pacman.conf
##### Descomenta estas líneas
#Color
#ParallelDownloads = 5
##### Agrega esta línea
ILoveCandy
```

### Drivers Propietarios NVIDIA

```BASH
# Drivers Propietarios - 500.xx
sudo pacman -S nvidia nvidia-settings nvidia-utils lib32-nvidia-utils cuda opencl-nvidia lib32-opencl-nvidia vdpauinfo clinfo glxinfo nvidia-prime

# Más info, visita
https://codigocristo.github.io/driver_nvidia.html
```

### Create user directory folders

```BASH
sudo pacman -S xdg-user-dirs
xdg-user-dirs-update
```

### AUR

```BASH
sudo pacman -S base-devel git
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R remmian:remmian yay-git/
cd yay-git
makepkg -si
```

### Paquetes Base

```BASH
sudo pacman -S linux-headers base base-devel nano os-prober networkmanager dhcpcd netctl wpa_supplicant dialog xf86-video-intel intel-ucode xorg xorg-xinit xorg-server mesa mesa-demos ttf-bitstream-vera adobe-source-sans-pro-fonts ttf-droid icedtea-web gst-libav ttf-ubuntu-font-family ttf-anonymous-pro
```

### Paquetes necesarios antes de usar un WindowManager ('Qtile' y/o 'Bspwm')

```BASH
sudo pacman -S lightdm lightdm-gtk-greeter alacritty firefox-developer-edition rofi which nitrogen ttf-dejavu ttf-liberation noto-fonts pavucontrol pulseaudio pulseaudio-bluetooth pamixer arandr udiskie ntfs-3g network-manager-applet volumeicon cbatticon git curl wget zsh thunar ranger glib2 gvfs lxappearance picom geeqie vlc
```

### Lightdm config

```BASH
# Abrimos lightdm
sudo nvim /etc/lightdm/lightdm.conf
# Descomentamos esta línea y la editamos
#greeter-session=example-gtk-gnome
# La modificamos para que quede así
greeter-session=lightdm-gtk-greeter
# Habilitamos lightdm
sudo systemctl enable lightdm.service
```

### Media Transfer Protocol

```BASH
sudo pacman -S libmtp android-file-transfer
yay -S simple-mtpfs
```

### ZSH Config

```BASH
### Alias
alias ls="lsd"
alias l="lsd -la"
alias cat="bat"
alias v="nvim"
alias update="sudo pacman -Syu --noconfirm && yay -Syu"

### Zinit Plugins
zinit light zdharma-continuum/fast-syntax-highlighting
zinit light zsh-users/zsh-autosuggestions
zinit light zsh-users/zsh-completions

### spaceship config
SPACESHIP_PROMPT_ORDER=(
    sudo        # Sudo indicatoruser        # Username section
    user        # Username section
    dir         # Current directory section
    host        # Hostname section
    git         # Git section (git_branch + git_status)
    hg          # Mercurial section (hg_branch  + hg_status)
    exec_time   # Execution time
    line_sep    # Line break
    jobs        # Background jobs indicator
    exit_code   # Exit code section
    char        # Prompt character
    venv        # virtualenv section
)
# SPACESHIP_<SECTION>_<OPTION>
SPACESHIP_USER_SHOW=always
SPACESHIP_PROMPT_ADD_NEWLINE=false
SPACESHIP_DIR_TRUNC_REPO=false  # when the path is long dont show the first folder
# SPACESHIP_CHAR_PREFIX="🛸"
### END spaceship config
```

## WindowManager

### Qtile

```BASH
sudo pacman -S qtile
```

### Bspwm

```BASH
# Descarga el instalador
curl https://raw.githubusercontent.com/gh0stzk/dotfiles/master/RiceInstaller -o $HOME/RiceInstaller
# Le damos permisos de ejecución
chmod +x RiceInstaller
# Corremos el instalador
./RiceInstaller
```
