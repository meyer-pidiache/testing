#
# Author: Meyer Pidiache <github.com/meyer-pidiache>
#

set -euo pipefail

greenColour="\e[0;32m\033[1m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
endColour="\033[0m\e[0m"

function setManaged ()
{
  echo -e "[${greenColour}*${endColour}] Restarting network..."
  # Deactivate monitor mode
  iw dev | grep "monitor" >/dev/null
  if [[ $(echo $?) -ne 1 ]]; then
    ip link set wlan0 down
    iw wlan0 set type managed
    ip link set wlan0 up
  fi
  # Restarting network services
  systemctl restart wpa_supplicant.service NetworkManager.service dhcpcd.service
  iw dev
}

if [ "$(id -u)" == "0" ]; then
  # Getting arguments
  declare -i parameter_counter=0;
  while getopts ":i:" arg; do
    case $arg in
      i) interface=$OPTARG; let parameter_counter+=1;;
    esac
  done

  if [ $parameter_counter -ne 1 ]; then
    setManaged
    echo -e "\n[${redColour}*${endColour}] Use: resetNet -i [Interface Name]"
  else
    # Process
    echo -e "[${greenColour}*${endColour}] Deleting interface..."
    ifconfig $interface down && iw dev $interface del

    setManaged
  fi
else
  echo -e "\n[${yellowColour}*${endColour}] Execute as root\n"
fi
