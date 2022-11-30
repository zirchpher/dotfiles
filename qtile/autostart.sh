#!/bin/sh

# Configurar teclado a español (Latam)
setxkbmap latam &

# Iconos del sistema
udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 10 &

# Load Wallpaper
nitrogen --restore &
