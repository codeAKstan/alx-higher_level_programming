#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch todo data. Status code: ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = todos.reduce((acc, todo) => {
    if (todo.completed) {
      if (acc[todo.userId]) {
        acc[todo.userId]++;
      } else {
        acc[todo.userId] = 1;
      }
    }
    return acc;
  }, {});

  console.log(completedTasksByUser);
});
