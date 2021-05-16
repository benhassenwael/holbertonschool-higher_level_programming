#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, resp, body) => {
  if (err) console.log(err);
  else if (resp.statusCode === 200) {
    const film = JSON.parse(body);
    for (const ch of film.characters) {
      request.get(ch, (err, resp, body) => {
        if (err) console.log(err);
        else if (resp.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
