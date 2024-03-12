#!/usr/bin/node
const { argv } = require('node:process');

const farg = argv[2] || 'undefined';
const sarg = argv[3] || 'undefined';

console.log(`${farg} is ${sarg}`);
