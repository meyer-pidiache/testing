#!/bin/bash

interface=$(iw dev | awk '$1=="Interface"{print $2}')
new=$interface - ("wlan0")

echo $new
