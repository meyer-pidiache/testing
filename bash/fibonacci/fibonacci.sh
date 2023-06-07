echo -n "Type Fibonacci Length: "
read -r position

getFibonacci () {
  if [[ $1 == 0 ]]; then
    echo 0
  elif [[ $1 == 1 ]]; then
    echo 1
  else
    local a=$(getFibonacci $(($1 - 2)))
    local b=$(getFibonacci $(($1 - 1)))
    echo $((a + b))
  fi
}

getByRecursion () {
  local sequence=()
  for ((i = 0; i < $1; i++)); do
    sequence+="$(getFibonacci $i) "
  done
  
  echo $sequence | sed 's/ /, /g; s/^/[/; s/$/]/'
}

getByLineal () {
  local sequence=()
  local less2=0
  local less1=1

  sequence="$less2 $less1 "
  for ((i = 2; i < $1; i++)); do
    local new=$(($less2+$less1))
    sequence+="$new "

    less2=$less1
    less1=$new
  done

  echo $sequence | sed 's/ /, /g; s/^/[/; s/$/]/'
}

if [[ $position -ge 16 ]]; then
  echo -e "\n $(getByLineal $position)"
  echo -e "\nLineal mode implement"
else
  echo -e "\n $(getByRecursion $position)"
  echo -e "\nRecursion mode implement"
fi
