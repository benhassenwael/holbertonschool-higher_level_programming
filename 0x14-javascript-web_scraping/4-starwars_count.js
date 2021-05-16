#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let num = 0;
    for (const film of films) {
      for (const ch of film.characters) {
        if (ch.endsWith('18/')) { num++; break; }
      }
    }
    console.log(num);
  }
});
