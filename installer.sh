#!/bin/bash

# don't run with sudo
if [ "$(id -u)" = 0 ]; then
	echo "This script MUST NOT be run as root user."
	exit 1
fi

echo "installing necessary packages"
sudo pacman -S linux-headers base base-devel nano os-prober networkmanager dhcpcd netctl wpa_supplicant dialog xf86-video-intel intel-ucode xorg xorg-xinit xorg-server mesa mesa-demos icedtea-web gst-libav xdg-user-dirs --noconfirm

echo "installing Fonts"
sudo pacman -S ttf-bitstream-vera adobe-source-sans-pro-fonts ttf-droid ttf-ubuntu-font-family ttf-anonymous-pro ttf-dejavu ttf-liberation noto-fonts noto-fonts-emoji

echo "Packages required before using a WindowManager ('Qtile' and/or 'Bspwm')"
sudo pacman -S lightdm lightdm-gtk-greeter alacritty firefox-developer-edition rofi which nitrogen pavucontrol pulseaudio pulseaudio-bluetooth pamixer arandr udiskie ntfs-3g network-manager-applet volumeicon cbatticon git curl wget zsh thunar ranger glib2 gvfs lxappearance picom geeqie vlc libmtp android-file-transfer --noconfirm

echo "installing yay"
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R $USER:$USER yay-git/
cd yay-git
makepkg -si

logo "Preparing Folders"
if [ ! -e $HOME/.config/user-dirs.dirs ]; then
	xdg-user-dirs-update
	echo "Creating xdg-user-dirs"
else
	echo "user-dirs.dirs already exists"
fi
sleep 2
clear

echo "update pacman and yay"
sudo pacman -Syu && yay -Syu
sleep 2
clear

echo "Cool Packages"
yay -S simple-mtpfs emote
sleep 2
clear

while true; do
	read -rp "Do you want to install bspwm? [y/N]: " yn
	case $yn in
	[Yy]*) curl https://raw.githubusercontent.com/gh0stzk/dotfiles/master/RiceInstaller -o $HOME/RiceInstaller && chmod +x $HOME/RiceInstaller && cd $HOME && ./RiceInstaller && break ;;
	[Nn]*) exit ;;
	*) printf " Error: just write 'y' or 'n'\n\n" ;;
	esac
done
clear
