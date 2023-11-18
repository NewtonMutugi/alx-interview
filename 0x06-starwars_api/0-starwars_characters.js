#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:

// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const options = { json: true };
if (!process.argv[2]) {
  console.log('Usage: ./0-starwars_characters.js movieId');
  process.exit(1);
}
request(url, async (error, response, body) => {
  error && console.error('Error: ', error);
  body = JSON.parse(body);
  for (const char of body.characters) {
    await new Promise((resolve, reject) => {
      request(char, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
request(url, options, printCharacters);
