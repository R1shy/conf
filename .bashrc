<<<<<<< HEAD
alias ls='ls -a'
alias ll='ls -al'
eval "$(zoxide init bash)"
alias cd='z'
PS1='\u@\h-> '
export PATH="/home/rishy/.local/bin:$PATH"
export PATH="/home/rishy/.cargo/bin:$PATH"
. "$HOME/.cargo/env"
alias g='git'
alias gaa='git add .'
alias gcm='git commit -m'
alias gm='git merge'
alias gst='git status'
alias gco='git checkout'
alias gp='git push'
alias gpl='git pull'
alias sysup='sudo xbps-install -Syu'
alias sysad='sudo xbps-install -S'
alias sysrm='sudo xbps-remove'
alias pacls='sudo xbps-query -m'
alias reboot='sudo reboot'
alias shutdown='sudo shutdown'
alias pyin='pip install --break-system-packages'
=======
set -o vi # set vi(m) binds in bash
alias ls='ls -a' # don't hide hidden files
alias ll='ls -al' # like above but also show ownership
eval "$(zoxide init bash)" # start zoxide
alias cd='z' # make cd use zoxide
PS1='\u@\h-> ' # fancy shmansy prompt
export PATH="/home/rishy/.local/bin:$PATH" # locally compiled stuff goes in path
export PATH="/home/rishy/.cargo/bin:$PATH" # cargo install puts binaries here
. "$HOME/.cargo/env" # cargo helper stuff
alias g='git'
alias gaa='git add .'  # git alias
alias gcm='git commit -m' # git alias
alias gm='git merge' # git alias
alias gst='git status' # git alias
alias gco='git checkout' # git alias
alias gp='git push' # git alias
alias gpl='git pull' # git alias
alias sysup='sudo xbps-install -Syu' # universal updates
alias sysad='sudo xbps-install -S' # universal adding
alias sysrm='sudo xbps-remove' # universal removing
alias reboot='sudo reboot' # most distros make reboot
alias shutdown='sudo shutdown' # and shutdown only usable by root
alias pyin='pip install --break-system-packages' # FUCK PYTHON
alias sysclean='sudo xbps-remove -oO', # remove uneeded deps but only on void linux
>>>>>>> f078f7b (.)
