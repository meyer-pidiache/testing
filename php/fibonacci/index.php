<?php

$position = $_GET['position'];

function getFibonacci(int $number) {
  if ($number == 0) {
    return 0;
  } elseif ($number == 1) {
    return 1;
  } else {
    $a = getFibonacci($number - 2);
    $b = getFibonacci($number - 1);
    return $a + $b;
  }
}

function getByRecursion(int $position) {
  $sequence = array();
  for ($i=0; $i < $position; $i++) { 
    array_push($sequence, getFibonacci($i));
  }
  return $sequence;
}

if ($position > 15) {
  echo 1;
} else {
  echo "Type Fibonacci Lenght: " . $position . "<br><br>";
  $numbers = getByRecursion($position);
  foreach ($numbers as $key => $value) {
    $list = "$list $value, ";
  }
  $list = substr($list, 1, -2);
  echo "[$list]";
  echo "<br><br>Recursion mode implement";
}
