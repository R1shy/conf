alias ls='ls -a'
alias ll='ls -alh'
alias g='git'
alias gaa='g add .'
alias gcm='g commit -m'
alias gp='git push'
alias gpl='git pull'
alias sysad='sudo emerge -va'
alias binad='sudo emerge -vaG'
alias sysrm='sudo emerge --unmerge'
alias sysup='sudo emerge -avuDN @world' # TODO: figure out how to also update binaries
. "$HOME/.cargo/env"
eval "$(zoxide init bash)"
alias cd='z'
