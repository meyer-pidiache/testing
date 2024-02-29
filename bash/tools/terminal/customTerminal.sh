#!/bin/bash
#
# Author: Meyer Pidiache <github.com/meyer-pidiache>
# Reference: https://meyer-pidiache.github.io/posts/terminal-customization/
#

GREEN="\e[0;32m\033[1m"
RED="\e[0;31m\033[1m"
BLUE="\e[0;34m\033[1m"
YELLOW="\e[0;33m\033[1m"
ENDCOLOR="\033[0m\e[0m"

programs=("curl" "git" "wget" "zsh" "kitty" "zsh-syntax-highlighting" "zsh-autosuggestions" "bat" "fzf" "lsd" "npm" "imagemagick")

print_message() {
    case $1 in
        "success")
            echo -e "${GREEN}[Hecho] $2${ENDCOLOR}"
            ;;
        "error")
            echo -e "${RED}[Error] $2${ENDCOLOR}"
            exit 1
            ;;
        "info")
            echo -e "${BLUE}[Información] $2${ENDCOLOR}"
            ;;
        "warning")
            echo -e "${YELLOW}[Advertencia] $2${ENDCOLOR}"
            ;;
    esac
}

run_as_user() {
    local command_to_run="$1"
    sudo -u "$USER_NAME" $command_to_run
}

plugins() {
    print_message "info" "Descargando extensión Sudo"
    mkdir -p /usr/share/zsh/plugins/zsh-sudo/
    wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh -P /usr/share/zsh/plugins/zsh-sudo/

    print_message "info" "Ordenando extensiones"
    mv /usr/share/zsh-syntax-highlighting /usr/share/zsh/plugins/
    mv /usr/share/zsh-autosuggestions /usr/share/zsh/plugins/

    print_message "success" "Extensiones configuradas"
}

tools() {
    print_message "info" "Descargando última versión de Neovim"
    curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
    rm -rf /opt/nvim
    tar -C /opt -xzf nvim-linux64.tar.gz
    export PATH="$PATH:/opt/nvim-linux64/bin"
    rm nvim-linux64.tar.gz

    print_message "info" "Instalando NvChad"
    run_as_user "git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim"
}

installP10K() {
    print_message "info" "Descargando Power Level 10K"
    run_as_user "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k"
    
    print_message "info" "Descargando archivo de configuración"
    run_as_user "wget https://raw.githubusercontent.com/meyer-pidiache/dotfiles/main/.p10k.zsh -O ~/.p10k.zsh"

    print_message "success" "Power Level 10K instalado"
}

kittyConfig() {
    print_message "info" "Configurando Kitty Terminal"
    KITTY_CONFIG_DIR=~/.config/kitty
    KITTY_CONFIG_FILE="$KITTY_CONFIG_DIR/kitty.conf"

    # Validar si el archivo ya existe
    if [ -e "$KITTY_CONFIG_FILE" ]; then
        print_message "info" "El archivo $KITTY_CONFIG_FILE ya existe. Haciendo copia de seguridad..."
        run_as_user "mv '$KITTY_CONFIG_FILE' '$KITTY_CONFIG_FILE.backup'"
    else
        run_as_user "mkdir -p '$KITTY_CONFIG_DIR'"
    fi

    run_as_user "wget https://raw.githubusercontent.com/meyer-pidiache/testing/main/bash/tools/terminal/kitty.conf -O '$KITTY_CONFIG_FILE'"

    print_message "success" "Se ha configurado Kitty Terminal"
}


zshConfig() {
    # Guardar copia de ~/.zshrc si ya existe
    print_message "info" "Configurando la ZSH"
    if [ -e ~/.zshrc ]; then
        run_as_user "mv ~/.zshrc ~/.zshrc.old"
    fi

    run_as_user "touch ~/.zsh_history"

    run_as_user "wget https://raw.githubusercontent.com/meyer-pidiache/testing/main/bash/tools/terminal/.zshrc -O ~/.zshrc"

    print_message "success" "ZSH configurado"
}

checkFontInstalled() {
    if fc-list | grep -q "hack"; then
        print_message "success" "Hack Nerd Font instalada correctamente."
    else
        print_message "error" "La instalación de Hack Nerd Font ha fallado."
    fi
}

installFont() {
    print_message "info" "Descargando Hack Nerd Font (TTF)"
    run_as_user "curl -LO https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Hack.zip"
    print_message "info" "Instalando Hack Nerd Font (TTF)"
    run_as_user "mkdir hack-nerd-font"
    run_as_user "unzip Hack.zip -d hack-nerd-font"
    rm Hack.zip
    mv hack-nerd-font/ /usr/share/fonts/truetype/
    fc-cache -f -v
    checkFontInstalled
}

isInstalled() {
    command -v $1 > /dev/null 2>&1
}

install_packages() {
    print_message "info" "Actualizando lista de paquetes..."
    sudo apt update

    for program in "${programs[@]}"; do
        if isInstalled "$program"; then
            print_message "success" "$program ya está instalado."
        else
            print_message "info" "Instalando $program..."
            sudo apt install $program -y
            print_message "success" "$program instalado correctamente."
        fi
    done
}

if [ "$(id -u)" == "0" ]; then
  if [ "$#" != "1" ]; then
    print_message "error" "Especifica el usuario a usar: sudo ./customTerminal.sh [USERNAME]"
  else
    USER_NAME="$1"

    install_packages
    installFont
    zshConfig
    kittyConfig
    installP10K
    plugins
    tools

    print_message "success" "¡Listo!"
  fi

else
  print_message "error" "Ejecuta el script como root (sudo)"
fi
