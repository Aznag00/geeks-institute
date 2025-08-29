/*
// ===== Exercise 1
const h1 = document.querySelector("h1");
console.log(h1);

const article = document.querySelector("article");
const paragraphs = article.querySelectorAll("p");
if (paragraphs.length > 0) {
  paragraphs[paragraphs.length - 1].remove();
}

const h2 = document.querySelector("h2");
h2.addEventListener("click", function () {
  h2.style.backgroundColor = "red";
});

const h3 = document.querySelector("h3");
h3.addEventListener("click", function () {
  h3.style.display = "none";
});

const boldButton = document.createElement("button");
boldButton.textContent = "Make Paragraphs Bold";
document.body.appendChild(boldButton);

boldButton.addEventListener("click", function () {
  const allParagraphs = document.querySelectorAll("p");
  allParagraphs.forEach((p) => {
    p.style.fontWeight = "bold";
  });
});

h1.addEventListener("mouseover", function () {
  const randomSize = Math.floor(Math.random() * 101);
  h1.style.fontSize = `${randomSize}px`;
});

const secondParagraph = paragraphs[1];
if (secondParagraph) {
  secondParagraph.addEventListener("mouseover", function () {
    this.style.transition = "opacity 1s";
    this.style.opacity = "0";
  });

  secondParagraph.addEventListener("mouseout", function () {
    this.style.opacity = "1";
  });
}
*/
// ===== Exercise 2

const form = document.querySelector("form");
console.log(form);

const input1 = document.getElementById("fname");
const input2 = document.getElementById("lname");
console.log(input1);
console.log(input2);

const name_att1 = document.getElementsByName("firstname");
const name_att2 = document.getElementsByName("lastname");

console.log(name_att1);
console.log(name_att2);

const submit = document.getElementById("submit");
submit.addEventListener("click", function (event) {
  event.preventDefault();
  // to prevent the page from refreshing and sending data
  const fnameVal = input1.value.trim();
  const lnameVal = input2.value.trim();
  if (fnameVal & lnameVal) {
    const ul = document.querySelector(".usersAnswer");
    const li1 = document.createElement("li");
    li1.textContent = fnameVal;
    const li2 = document.createElement("li");
    li2.textContent = lnameVal;
    ul.appendChild(li1);
    ul.appendChild(li2);
  } else {
    console.log("inputs should not be empty");
  }
});

// ===== Exercise 3
let allBoldItems;
function getBoldItems() {
  allBoldItems = document.querySelectorAll("strong");

  allBoldItems.forEach((item) => console.log(item.textContent));
}

function highlight() {
  allBoldItems.forEach((item) => (item.style.color = "blue"));
}

function returnItemsToDefault() {
  allBoldItems.forEach((item) => {
    item.style.color = "black";
  });
}
getBoldItems();
highlight();
returnItemsToDefault();

// ===== Exercise 4
const myForm = document.getElementById("MyForm");
const radiusInput = document.getElementById("radius");
const volumeInput = document.getElementById("volume");

function calculateVol(radius) {
  return (4 / 3) * Math.PI * Math.pow(radius, 3);
}
myForm.addEventListener("submit", function (event) {
  event.preventDefault();
  const radius = parseFloat(radiusInput.value);
  if (!isNaN(radius) && radius > 0) {
    const volume = calculateVol(radius).toFixed(2);
    const result = document.createElement("p");
    document.body.appendChild(result);
    result.textContent = volume;
  } else {
    volumeInput.value = "Invalid radius!";
  }
});
