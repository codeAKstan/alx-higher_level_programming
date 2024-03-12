#!/usr/bin/node
const { argv } = require('node:process');

const fArg = argv[2];

const intValue = parseInt(fArg);

if (!isNaN(intValue)) {
  console.log(`My number: ${intValue}`);
} else {
  console.log('Not a number');
}
