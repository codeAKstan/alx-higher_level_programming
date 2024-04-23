#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(new Error(error));
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character data. Status code: ${response.statusCode}`));
        return;
      }

      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
};

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie with ID ${movieId}. Status code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  const characterPromises = characterUrls.map(fetchCharacter);

  Promise.all(characterPromises)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => console.error(error));
});
