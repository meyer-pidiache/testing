const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

function getFibonacci(number) {
  if (number == 0) {
    return 0;
  } else if (number == 1) {
    return 1;
  } else {
    let a = getFibonacci(number - 2);
    let b = getFibonacci(number - 1);
    return a + b
  }
}

function getByRecursion(position) {
  let sequence = new Array();
  for (let i = 0; i < position; i++) {
    sequence.push(getFibonacci(i));
  }

  return sequence;
}

readline.question('Type Fibonacci Length: ', position => {
  if (position > 15) {
    console.log("\nLineal mode implement");
  } else {
    console.log(getByRecursion(position));
    console.log("\nRecursion mode implement");
  }
  readline.close();
});

