#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] === undefined || argv[3] === undefined) {
  console.log('undefined is undefined');
} else {
  console.log(argv[2] + ' is ' + argv[3]);
}
