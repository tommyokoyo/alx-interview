#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error: ', error);
    } else if (response.statusCode !== 200){
      console.error('Api call failed - status: ', response.statusCode)
    } else {
      const movie_characters = body.characters;

      fetchAndPrintCharacters(movie_characters, 0);
    }
  });
}

function fetchAndPrintCharacters(characters, index) {
  if (index >= characters.length) {
    return [];
  }

  const characterUrl = characters[index];
  request(characterUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching character: ', error);
    } else if (response.statusCode !== 200) {
      console.error('API Request failed - status code: ', response.statusCode);
    } else {
      const characterName = body.name;
      console.log(characterName);
      fetchAndPrintCharacters(characters, index + 1);
    }
  })
}

const movieId = process.argv[2];
if (movieId) {
  try {
    getMovieCharacters(movieId);
  } catch (e) {
    console.log(`Connection Error: ${e}`);
  }
} else {
  console.error('Please provide a movie ID!.');
}
