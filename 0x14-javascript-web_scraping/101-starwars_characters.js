#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, resp, body) => {
  if (err) console.log(err);
  else if (resp.statusCode === 200) {
    const film = JSON.parse(body);
    const promises = [];
    for (const ch of film.characters) {
      promises.push(new Promise((resolve, reject) => {
        request.get(ch, (err, resp, body) => {
          if (err) {
            reject(err);
          } else if (resp.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(Error('Unknown'));
          }
        });
      }));
    }
    Promise.all(promises).then((names) => names.forEach((name) => console.log(name)));
  }
});
