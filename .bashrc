alias ls='ls -a'
alias ll='ls -alh'
alias g='git'
alias gaa='g add .'
alias gcm='g commit -m'
alias gp='git push'
alias gpl='git pull'
. "$HOME/.cargo/env"
export PATH="/home/rishy/.cargo/bin/:$PATH"
export PATH="/home/rishy/.local/bin:$PATH"
export PATH="/opt/nvim/bin:$PATH"
export PATH="/opt/kitty/kitty/launcher:$PATH"
export PATH="/opt/cmake/bin:$PATH"
export PATH="/opt/zig/:$PATH"
export PATH="/home/rishy/Android/Sdk/emulator:$PATH"
export PATH="/opt/jdtls/bin:$PATH"
export PATH="/opt/gradle/bin:$PATH"
export PATH="/opt/vs/Vintagestory:$PATH"
export PS1="\u@\h-> "
eval "$(mise activate bash)"
export EDITOR=nvim
