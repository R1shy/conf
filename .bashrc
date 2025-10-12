alias ls='ls -a'
alias ll='ls -alh'
alias g='git'
alias gaa='g add .'
alias gcm='g commit -m'
alias gp='git push'
alias gpl='git pull'
export EDITOR=nvim
export PATH="/home/rishy/.local/bin:$PATH"
export PS1="\u@\h-> "
export ROCM_PATH=/opt/rocm
export HSA_OVERRIDE_GFX_VERSION=10.3.0
export PATH="/opt/gradle/gradle-9.0.0/bin/:$PATH"
export PATH="/home/rishy/.cargo/bin/:$PATH"
eval "$(mise activate bash)"

. "$HOME/.cargo/env"
