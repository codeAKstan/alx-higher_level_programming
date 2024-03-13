#!/usr/bin/node
const { argv } = require('node:process');

const fArg = argv[2];

const intValue = parseInt(fArg);
let i = 0;
const message = 'C is fun';

if (!isNaN(intValue)) {
  while (i < intValue) {
    console.log(message);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
