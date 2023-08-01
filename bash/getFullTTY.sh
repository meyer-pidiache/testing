#!/bin/bash

echo "
script /dev/null -qc /bin/bash
(inside the remote session) CTRL+Z;

stty raw -echo; fg;

reset xterm; ls; export SHELL=/bin/bash; export TERM=screen #or 'xterm-kitty'
stty rows 37 columns 135; reset;

# Get rows and columns
stty size
"

