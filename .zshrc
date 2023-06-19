export ZSH="$HOME/.oh-my-zsh"

###################
# Theme
###################
ZSH_THEME="spaceship"

###################
# Plugins
###################
plugins=(git)

source $ZSH/oh-my-zsh.sh

###################
# Aliases
###################

# Essential
alias ls="lsd -a --group-directories-first"
alias l="lsd -la --group-directories-first"
alias cat="bat"
alias update="sudo pacman -Syu --noconfirm && yay -Syu"
alias instalar="sudo pacman -S"
alias desinstalar="sudo pacman -Rns"

# Cleaning
alias purga="sudo pacman -Rns $(pacman -Qtdq) ; sudo fstrim -av"
alias grub-update="sudo grub-mkconfig -o /boot/grub/grub.cfg"
alias clean="yay -Sc && sudo pacman -Scc"
 
# Nvim
alias v="nvim"
alias rmvim="rm -rf ~/.config/nvim ~/.local/share/nvim ~/.local/share/nvim ~/.local/state/nvim ~/.cache/nvim"
alias govim="cd ~/.config/nvim/lua/custom"

# Git aliases
alias gi="git init ."
alias gs="git status"
alias gc="git commit -m"
alias ga="git add ."
alias gpl="git pull origin main"
alias gps="git push origin main"
alias gl="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# tmux
alias t="tmux"
alias tso="tmux source ~/.config/tmux/tmux.conf"
alias tns="tmux new -s"
alias ta="tmux attach"

### Added by Zinit's installer
if [[ ! -f $HOME/.local/share/zinit/zinit.git/zinit.zsh ]]; then
    print -P "%F{33} %F{220}Installing %F{33}ZDHARMA-CONTINUUM%F{220} Initiative Plugin Manager (%F{33}zdharma-continuum/zinit%F{220})…%f"
    command mkdir -p "$HOME/.local/share/zinit" && command chmod g-rwX "$HOME/.local/share/zinit"
    command git clone https://github.com/zdharma-continuum/zinit "$HOME/.local/share/zinit/zinit.git" && \
        print -P "%F{33} %F{34}Installation successful.%f%b" || \
        print -P "%F{160} The clone has failed.%f%b"
fi

source "$HOME/.local/share/zinit/zinit.git/zinit.zsh"
autoload -Uz _zinit
(( ${+_comps} )) && _comps[zinit]=_zinit

# Load a few important annexes, without Turbo
# (this is currently required for annexes)
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

### End of Zinit's installer chunk

### Zinit Plugins
zinit light zdharma-continuum/fast-syntax-highlighting
zinit light zsh-users/zsh-autosuggestions
zinit light zsh-users/zsh-completions

### spaceship config
SPACESHIP_PROMPT_ORDER=(
    sudo        # Sudo indicatoruser        # Username section
    user        # Username section
    dir         # Current directory section
    host        # Hostname section
    git         # Git section (git_branch + git_status)
    hg          # Mercurial section (hg_branch  + hg_status)
    exec_time   # Execution time
    line_sep    # Line break
    jobs        # Background jobs indicator
    exit_code   # Exit code section
    char        # Prompt character
    venv        # virtualenv section
)
# SPACESHIP_<SECTION>_<OPTION>
SPACESHIP_USER_SHOW=always
SPACESHIP_PROMPT_ADD_NEWLINE=false
SPACESHIP_DIR_TRUNC_REPO=false  # when the path is long dont show the first folder
# SPACESHIP_CHAR_PREFIX="🛸"
### END spaceship config

### NVM Config
source /usr/share/nvm/init-nvm.sh

PATH="/home/remmian/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/home/remmian/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/remmian/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/remmian/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/remmian/perl5"; export PERL_MM_OPT;
