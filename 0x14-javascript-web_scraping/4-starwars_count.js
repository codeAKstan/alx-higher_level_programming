#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    return;
  }

  const movies = JSON.parse(body).results;
  const moviesWithWedge = movies.filter(movie =>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(moviesWithWedge.length);
});
