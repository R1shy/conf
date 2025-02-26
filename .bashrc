# add my prompt
prompt="\u@\h-> "
export PS1=$prompt

alias ls='ls -a' # make ls more expressive
alias clock='tty-clock -sct -C4' # tty-clock config

# git aliases
alias g='git'
alias gaa='git add --all'
alias gst='git status'
alias gcm='git commit -m'
alias gp='git push'
alias gpl='git pull'
alias gco='git checkout'
alias gm='git merge'

# add to rust apps and local builds to path
export PATH="/home/rishy/.local/bin:$PATH"
export PATH="/home/rishy/.cargo/bin/:$PATH"

# add zoxide and make cd use it
eval "$(zoxide init bash)"
alias cd='z'
