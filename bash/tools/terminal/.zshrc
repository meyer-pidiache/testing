if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history

# Descomenta para Debian
export PATH="$PATH:/opt/nvim-linux64/bin"

alias cat='batcat' # Descomenta para Debian
# alias cat='bat' # Descomenta para Arch
alias icat='kitty +kitten icat' # Para mostrar imágenes por consola, se necesita Image Magick
alias vim='nvim'
# lsd
alias l='lsd --group-dirs=first'
alias la='lsd -a --group-dirs=first'
alias ll='lsd -lh --group-dirs=first'
alias lla='lsd -lha --group-dirs=first'
alias ls='lsd --group-dirs=first'

# Esta función nos ayudará a previsualizar archivos. 'search' desde la terminal para usarla.
function search(){
	if [ "$1" = "h" ]; then

		fzf -m --reverse --preview-window down:20 --preview '[[ $(file --mime {}) =~ binary ]] &&

 	                echo {} is a binary file ||

	                 (batcat --style=numbers --color=always {} ||

	                  highlight -O ansi -l {} ||

	                  coderay {} ||

	                  rougify {} ||

	                  cat {}) 2> /dev/null | head -500'

	else

	        fzf -m --preview '[[ $(file --mime {}) =~ binary ]] &&

	                         echo {} is a binary file ||

	                         (batcat --style=numbers --color=always {} ||

	                          highlight -O ansi -l {} ||

	                          coderay {} ||

	                          rougify {} ||

	                          cat {}) 2> /dev/null | head -500'

	fi
}

# Atajos
## Avanzar (alt+right)
bindkey "^[[1;3C" forward-word
## Retroceder (alt+left)
bindkey "^[[1;3D" backward-word
## Eliminar bloque adelante (alt+supr)
bindkey "^[[3;3~" delete-word

# FZF
## Descomenta para Debian
source /usr/share/doc/fzf/examples/key-bindings.zsh
source /usr/share/doc/fzf/examples/completion.zsh
## Descomenta para Arch
### source /usr/share/fzf/key-bindings.zsh
### source /usr/share/fzf/completion.zsh

source /usr/share/zsh/plugins/zsh-sudo/sudo.plugin.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

source ~/.powerlevel10k/powerlevel10k.zsh-theme

[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
