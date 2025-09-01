// ===== Exercise 1
// the data will appear in the url query

// ===== Exercise 2
// data shows in DevTools → Network tab → Form Data

// ===== Exercise 3
const marioGame = {
  detail: "An amazing game!",
  characters: {
    mario: {
      description: "Small and jumpy. Likes princesses.",
      height: 10,
      weight: 3,
      speed: 12,
    },
    bowser: {
      description: "Big and green, Hates princesses.",
      height: 16,
      weight: 6,
      speed: 4,
    },
    princessPeach: {
      description: "Beautiful princess.",
      height: 12,
      weight: 2,
      speed: 2,
    },
  },
};

const jsonMario = JSON.stringify(marioGame);
console.log(jsonMario);
// nested objects also converted

const prettyJSON = JSON.stringify(marioGame, null, 2);
console.log(prettyJSON);
