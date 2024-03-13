#!/usr/bin/node
const { argv } = require('process');
const fArg = argv[2] || NaN;
const sArg = argv[3] || NaN;

function add (a, b) {
  a = parseFloat(fArg);
  b = parseFloat(sArg);

  if (!isNaN(a) && !isNaN(b)) {
    const result = a + b;
    console.log(result);
  } else {
    console.log('NaN');
  }
}

add(fArg, sArg);
