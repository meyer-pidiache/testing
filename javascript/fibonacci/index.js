const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Type Fibonacci Length: ', position => {
  if (position > 15) {
    console.log("\nLineal mode implement");
  } else {
    console.log("\nRecursion mode implement");
  }
  readline.close();
});

