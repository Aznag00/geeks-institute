const form = document.getElementById("libform");
const storySpan = document.getElementById("story");

function generateStories(noun, adjective, person, verb, place) {
  return [
    `One day, ${person} found a ${adjective} ${noun} and decided to ${verb} with it in ${place}.`,
    `In ${place}, ${person} saw a ${noun} that was incredibly ${adjective}. They had to ${verb} immediately!`,
    `${person} always wanted to ${verb} a ${adjective} ${noun}, especially when visiting ${place}.`,
  ];
}

let stories = [];
let lastIndex = -1;
form.addEventListener("submit", function (event) {
  event.preventDefault();
  const noun = document.getElementById("noun").value.trim();
  const adjective = document.getElementById("adjective").value.trim();
  const person = document.getElementById("person").value.trim();
  const verb = document.getElementById("verb").value.trim();
  const place = document.getElementById("place").value.trim();

  if (!noun || !adjective || !person || !verb || !place) {
    alert("please fill in all the fields");
    return;
  }
  stories = generateStories(noun, adjective, person, verb, place);
  shuffleStr();
});
function shuffleStr() {
  if (stories.length === 0) return;
  let randomIndex;
  do {
    randomIndex = Math.floor(Math.random() * stories.length);
  } while (randomIndex === lastIndex && stories.length > 1);
  lastIndex = randomIndex;
  storySpan.textContent = stories[randomIndex];
}

const shuffleBtn = document.createElement("button");
shuffleBtn.textContent = "Shuffle story";
document.body.appendChild(shuffleBtn);

shuffleBtn.addEventListener("click", function (event) {
  event.preventDefault();
  shuffleStory();
});
