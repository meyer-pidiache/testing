#!/bin/bash
#
# Author: Meyer Pidiache <github.com/meyer-pidiache>
#

set -euo pipefail

GREEN="\e[0;32m\033[1m"
RED="\e[0;31m\033[1m"
BLUE="\e[0;34m\033[1m"
YELLOW="\e[0;33m\033[1m"
ENDCOLOR="\033[0m\e[0m"

setManaged() {
  echo -e "[${GREEN}*${ENDCOLOR}] Restarting network..."
  ip link set $interface down
  # Deactivate monitor mode
  iw dev | grep "monitor" >/dev/null
  if [[ $(echo $?) -ne 1 ]]; then
    iw $interface set type managed
    if [[ "$?" -ne 0 ]]; then
      echo -e "[${RED}*${ENDCOLOR}] Failed to set managed interface"
    else
      echo -e "[${GREEN}*${ENDCOLOR}] $interface is now managed"
    fi
  fi

  # Restarting network services
  network_services=(wpa_supplicant.service NetworkManager.service dhcpcd.service)
  for service in "${network_services[@]}"; do
    systemctl restart $service 2>/dev/null
    if [[ "$?" -ne 0 ]]; then
      echo -e "[${RED}*${ENDCOLOR}]Failed to restart $service\n"
    else
      echo -e "[${GREEN}*${ENDCOLOR}] $service up"
    fi
  done

  # Set default MAC
  macchanger -p $interface
  if [[ "$?" -ne 0 ]]; then
    echo -e "[${RED}*${ENDCOLOR}] Failed to set default MAC"
  fi

  ip link set $interface up
  echo -e "[${BLUE}*${ENDCOLOR}] Done!"
}

if [ "$(id -u)" == "0" ]; then
  # Getting arguments
  declare -i parameter_counter=0
  while getopts ":i:" arg; do
    case $arg in
    i) interface=$OPTARG; let parameter_counter+=1;;
    esac
  done

  if [ $parameter_counter -ne 1 ]; then
    echo -e "\n[${RED}*${ENDCOLOR}] Use: resetNet -i [Default Interface]"
  else
    interfaces=($(iw dev | awk '$1=="Interface"{print $2}'))

    for i in "${interfaces[@]}"; do
      if [ "$i" != "$interface" ]; then
        # Process
        echo -e "[${GREEN}*${ENDCOLOR}] Deleting $i interface"
        ifconfig $i down && iw dev $i del
      fi
    done

    setManaged $interface
  fi
else
  echo -e "\n[${YELLOW}*${ENDCOLOR}] Execute as root\n"
fi
