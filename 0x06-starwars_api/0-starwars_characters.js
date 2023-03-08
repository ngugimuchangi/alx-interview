#!/usr/bin/node
/**
 * makeRequest - wrapper function for request
 * @url; (str): site url
 * Description: wraps around request object allowing it
 *              to work with async and await
 * Return: promise object that resolves with parsed JSON response
 *         and rejects with the request error.
 */
function makeRequest (url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * Main - entry point
 * Description: makes requests to Star Wars API for movie info based
 *              movie ID passed as a CLI arg. Retrieves movie character info
 *              then prints their names in order of appearance in the response.
 */
async function main () {
  const args = process.argv;

  if (args.length < 3) return;

  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  const movie = await makeRequest(movieUrl);

  if (movie.characters === undefined) return;
  for (const characterUrl of movie.characters) {
    const character = await makeRequest(characterUrl);
    console.log(character.name);
  }
}

main();
