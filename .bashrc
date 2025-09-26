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

if [ $(nproc) -eq 16 ]; then
    export PATH="/opt/cross/bin:$PATH" # on main PC
else
  echo "" # on macbook just do nothing
fi
