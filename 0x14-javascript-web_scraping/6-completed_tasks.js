#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, resp, body) => {
  if (err) console.log(err);
  else if (resp.statusCode === 200) {
    const todos = JSON.parse(body);
    const usersCompleted = {};
    for (const todo of todos) {
      if (todo.completed === true) {
        if (todo.userId in usersCompleted) {
          usersCompleted[todo.userId] += 1;
        } else {
          usersCompleted[todo.userId] = 1;
        }
      }
    }
    console.log(usersCompleted);
  }
});
