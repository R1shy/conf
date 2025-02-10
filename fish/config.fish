source /home/rishy/.config/fish/tokyonight_night.fish
alias ls='ls -a'
alias clock='tty-clock -stcB -C5'
alias reset='kill waybar && hyprctl dispatch exec waybar'
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
