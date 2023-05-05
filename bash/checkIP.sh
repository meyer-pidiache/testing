#!/bin/bash
#
# Author: Meyer Pidiache <github.com/meyer-pidiache>
#

set -euo pipefail

greenColour="\e[0;32m\033[1m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
endColour="\033[0m\e[0m"

if [ "$(id -u)" == "0" ]; then
  # Getting arguments
  declare -i parameter_counter=0;
  while getopts ":h:" arg; do
    case $arg in
      h) host=$OPTARG; let parameter_counter+=1;;
    esac
  done

  if [ $parameter_counter -ne 1 ]; then
    echo -e "\n${redColour}[*]${endColour} Use: checkIP -h [IP address]"
  else
    # Process
    echo -e "[${greenColour}*${endColour}] Starting"
    echo -e "\n[${blueColour}*${endColour}] Nmap: all open ports\n"
    nmap -p- --open -sS --min-rate 500m -vvv -n -Pn $host -oG allOpenPorts
    ports="$(cat allOpenPorts | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"

    if [ -n "$ports" ]; then
      echo -e "\n[${blueColour}*${endColour}] Scanning target\n"
      nmap -sCV -O -p$ports $host -oN targeted
    else
      echo -e "\n[${redColour}*${endColour}] No ports found"
      rm allOpenPorts
    fi
  fi

else
  echo -e "\n[${yellowColour}*${endColour}] Execute as root\n"
fi
