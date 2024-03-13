#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 3) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);

  if (!isNaN(size)) {
    let i = 0;
    while (i < size) {
      let j = 0;
      let row = '';
      while (j < size) {
        row += 'X';
        j++;
      }
      console.log(row);
      i++;
    }
  } else {
    console.log('Missing size');
  }
}
