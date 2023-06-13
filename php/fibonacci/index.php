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

function getByLineal(int $position) {
  $sequence = array();

  $less2 = 0;
  $less1 = 1;

  array_push($sequence, $less2);
  array_push($sequence, $less1);

  for ($i=2; $i < $position ; $i++) { 
    $new_v = $less2 + $less1;
    array_push($sequence, $new_v);

    $less2 = $less1;
    $less1 = $new_v;
  }

  return $sequence;  
}

if ($position > 15) {
  echo "Type Fibonacci Lenght: " . $position . "<br><br>";

  $numbers = getByLineal($position);
  foreach ($numbers as $key => $value) {
    $list = "$list $value, ";
  }
  $list = substr($list, 1, -2);
  echo "&nbsp;&nbsp;[$list]";

  echo "<br><br>Lineal mode implement";
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
