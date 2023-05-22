#!/bin/bash
#
# Author: Meyer Pidiache <github.com/meyer-pidiache>
#

GREEN="\e[0;32m\033[1m"
RED="\e[0;31m\033[1m"
BLUE="\e[0;34m\033[1m"
YELLOW="\e[0;33m\033[1m"
ENDCOLOR="\033[0m\e[0m"

# Function to check for open ports
check_ports () {
  nmap -p- --open -sS --min-rate 500m -vvv -n -Pn $1 -oG allOpenPorts
  ports="$(cat allOpenPorts | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"

  if [ -n "$ports" ]; then
    echo -e "\n[${BLUE}*${ENDCOLOR}] Scanning target\n"
    nmap -sCV -O -p$ports $1 -oN targeted
  else
    echo -e "\n[${RED}*${ENDCOLOR}] No ports found"
    rm allOpenPorts
  fi
}

# Function to check for open ports
if [ "$(id -u)" == "0" ]; then
  if [ "$#" != "1" ]; then
    echo -e "\n[${RED}*${ENDCOLOR}] Use: checkIP [IP address]"
  else
    # Process
    echo -e "[${GREEN}*${ENDCOLOR}] Starting"
    echo -e "\n[${BLUE}*${ENDCOLOR}] Nmap: all open ports\n"

    # Call check_ports function with IP address argument
    check_ports "$1"
  fi
else
  echo -e "\n[${YELLOW}*${ENDCOLOR}] Execute as root\n"
fi
