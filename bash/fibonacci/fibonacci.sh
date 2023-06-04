echo -n "Type Fibonacci Length: "
read -r position

getFibonacci () {
  number=$1
  if [[ $number == 0 ]]; then
    return 0
  elif [[ $number == 1 ]]; then
    return 1
  else
    return $(( getFibonacci($number - 2) + getFibonacci($number - 1) ))
  fi
}

getByRecursion () {
  position=$!
  sequence=()
  for ((i = 0; i < $position; i++)); do
    getFibonacci $i
    sequence+=( $? )
  done

  return "${sequence[@]}"
}

getByLineal () {
  position=$!
  sequence=()
  less2=0
  less1=1

  if [[ $position == 0 ]]; then
    return ($less2)
  elif [[ $position == 1 ]]; then
    return ($less2 $less1)
  else
    sequence=($less2 $less1)
    for ((_ = 2; _ < $position; _++)); do
      new=$(($less2+$less1))
      sequence+=$new

      less2=$less1
      less1=$new
    done

    return "${sequence[@]}"
  fi
}

if [[ $position -ge 31 ]]; then
  x=$(( getByLineal "$position" ))
  echo -e "${x[@]}\nLineal mode implement"
else
  x=$(( getByRecursion $position ))
  echo "${x[@]}"
  echo "Recursion mode implement"
fi
