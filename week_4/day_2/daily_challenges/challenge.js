const gameInfo = [
  {
    username: "john",
    team: "red",
    score: 5,
    items: ["ball", "book", "pen"],
  },
  {
    username: "becky",
    team: "blue",
    score: 10,
    items: ["tape", "backpack", "pen"],
  },
  {
    username: "susy",
    team: "red",
    score: 55,
    items: ["ball", "eraser", "pen"],
  },
  {
    username: "tyson",
    team: "green",
    score: 1,
    items: ["book", "pen"],
  },
];

const usernames = [];
gameInfo.forEach((value) => usernames.push(`${value.username}!`));
console.log(usernames);

const scoredusers = [];
gameInfo.forEach((value) => scoredusers.push(value.score > 5));
console.log(scoredusers);

let totalScore = 0;
gameInfo.forEach((value) => (totalScore += value.score));
console.log(totalScore);
