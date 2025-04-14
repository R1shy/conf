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
