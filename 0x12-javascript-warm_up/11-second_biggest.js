#!/usr/bin/node
const { argv } = require('process');

function secondBiggestInteger (args) {
  if (args.length <= 2) {
    return 0;
  }

  const numbers = args.slice(2).map(Number).sort((a, b) => b - a);

  const uniqueNumbers = Array.from(new Set(numbers));
  if (uniqueNumbers.length === 1) {
    return 0;
  }

  return uniqueNumbers[1];
}

console.log(secondBiggestInteger(argv));
