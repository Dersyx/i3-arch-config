# Configure system-wide theme colors, and sets the wallpaper
wal -i /home/dersyx/background/wallhaven-31235.jpg

# Merges .Xresources with system-wide configuration, to ensure
# that urxvt actually *works*
xrdb -merge ~/.Xresources

## Launch Polybar

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch bar main
polybar main --config=$HOME/.cache/wal/polybar-config
