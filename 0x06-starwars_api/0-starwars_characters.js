#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:

// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const options = { json: true };
function printCharacters (error, response, body) {
  if (response.statusCode === 404) {
    console.log('Movie not found');
  } else if (!error && response.statusCode === 200) {
    for (const character of body.characters) {
      request(character, options, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          console.log(body.name);
        }
      });
    }
  }
}
request(url, options, printCharacters);
