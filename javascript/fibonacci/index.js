const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Type Fibonacci Length: ', name => {
  console.log(`Length ${name}`);
  readline.close();
});



let x = "Lineal mode implement"
